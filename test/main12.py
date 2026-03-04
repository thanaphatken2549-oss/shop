from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
import uuid
import datetime

app = FastAPI()

# --- Mock Data ---
class PaymentMethod(str, Enum):
    CASH = "CASH"
    ONLINE = "ONLINE"

db = {
    "products": {
        "p1": {"name": "Coke", "price": 20, "stock": 100},
        "p2": {"name": "Lays", "price": 30, "stock": 50},
    },
    "members": {
        "0812345678": {"name": "สมชาย สายเปย์", "points": 100},
    },
    "baskets": {},
    "transactions": {} 
}

# --- Models ---
class AddItemRequest(BaseModel):
    product_id: str
    quantity: int

# Checkout: ขอแค่ตะกร้ากับเบอร์สมาชิก (ยังไม่จ่าย)
class CheckoutRequest(BaseModel):
    basket_id: str
    phone_number: Optional[str] = None

# Payment: จ่ายเงิน (ต้องมี ID ธุรกรรม และยอดเงินถ้าเป็นเงินสด)
class PaymentRequest(BaseModel):
    transaction_id: str
    payment_method: PaymentMethod
    cash_received: Optional[float] = 0.0 # ใส่เฉพาะตอนจ่ายเงินสด

# --- API Endpoints ---

@app.post("/basket/add")
def add_item(req: AddItemRequest, basket_id: str = "session1"):
    if req.product_id not in db["products"]:
        raise HTTPException(404, detail="หาของไม่เจอจ้า")
    
    if basket_id not in db["baskets"]:
        db["baskets"][basket_id] = []
    
    product = db["products"][req.product_id]
    db["baskets"][basket_id].append({
        "product_id": req.product_id,
        "name": product["name"],
        "price": product["price"],
        "quantity": req.quantity
    })
    
    return {"message": f"หยิบ {product['name']} ลงตะกร้า", "current_basket": db["baskets"][basket_id]}

# 1. Checkout (คำนวณยอดเฉยๆ)
@app.post("/checkout")
def checkout_process(req: CheckoutRequest):
    items = db["baskets"].get(req.basket_id, [])
    if not items:
        raise HTTPException(400, detail="ตะกร้าว่างเปล่า!")
    
    total = sum(i["price"] * i["quantity"] for i in items)
    
    # เช็คสมาชิก (แค่ดึงชื่อมาโชว์ ยังไม่บวกแต้ม)
    member = db["members"].get(req.phone_number)
    customer_name = member['name'] if member else "ลูกค้าทั่วไป"
    
    # สร้าง Transaction รอจ่ายเงิน (Status: PENDING)
    tx_id = f"TAX-{uuid.uuid4().hex[:5].upper()}"
    
    db["transactions"][tx_id] = {
        "status": "PENDING", # รอจ่าย
        "timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "customer_name": customer_name,
        "member_phone": req.phone_number, # เก็บเบอร์ไว้รอให้แต้มตอนจ่ายเสร็จ
        "items": items,
        "total": total
    }

    # เคลียร์ตะกร้า (ย้ายไปอยู่ใน Transaction แล้ว)
    db["baskets"][req.basket_id] = []

    return {
        "message": "สรุปยอดเรียบร้อย กรุณาชำระเงิน",
        "transaction_id": tx_id,   # <--- เอาอันนี้ไปจ่ายเงิน
        "total_amount": total,
        "customer": customer_name
    }

# 2. Payment (จ่ายเงิน + ตัดสต็อก + ออกใบเสร็จ)
@app.post("/payment", response_class=PlainTextResponse)
def process_payment(req: PaymentRequest):
    # ดึงข้อมูล Transaction
    tx = db["transactions"].get(req.transaction_id)
    
    if not tx:
        return "ERROR: ไม่พบรายการนี้ (Transaction ID ผิด)"
    if tx["status"] == "PAID":
        return "ERROR: รายการนี้จ่ายเงินไปแล้วครับ!"

    total = tx["total"]
    change = 0.0

    # --- Logic การจ่ายเงิน ---
    if req.payment_method == PaymentMethod.CASH:
        # ถ้าจ่ายสด ต้องเช็คเงินที่รับมา
        if req.cash_received < total:
            return f"ERROR: เงินไม่พอครับ! (ยอด {total} บาท แต่ให้มา {req.cash_received} บาท)"
        change = req.cash_received - total
    
    elif req.payment_method == PaymentMethod.ONLINE:
        # จ่ายออนไลน์ สำเร็จเลย (สมมติว่าตัดบัตรผ่าน)
        pass

    # --- จ่ายเงินสำเร็จแล้ว ทำการตัดสต็อกและให้แต้ม ---
    tx["status"] = "PAID"
    
    # 1. ตัดสต็อกจริง
    for item in tx["items"]:
        db["products"][item["product_id"]]["stock"] -= item["quantity"]

    # 2. ให้แต้มสมาชิก
    points = 0
    if tx["member_phone"]:
        points = int(total / 10)
        if tx["member_phone"] in db["members"]:
            db["members"][tx["member_phone"]]["points"] += points

    # --- รวมสินค้าซ้ำเพื่อพิมพ์ใบเสร็จ ---
    grouped_items = {}
    for item in tx["items"]:
        pid = item["product_id"]
        if pid in grouped_items:
            grouped_items[pid]["quantity"] += item["quantity"]
        else:
            grouped_items[pid] = item.copy()

    # --- สร้างใบเสร็จ ---
    line = "-" * 35
    double_line = "=" * 35
    
    receipt = f"""
{double_line}
    ร้านบังคร67 (สาขา 67)
{double_line}
ใบเสร็จเลขที่: {req.transaction_id}
วันที่: {tx['timestamp']}
ลูกค้า: {tx['customer_name']}
{line}
รายการสินค้า:
"""
    for pid, item in grouped_items.items():
        item_total = item['price'] * item['quantity']
        receipt += f"{item['name']:<15} x{item['quantity']:<3} {item_total:>8} บาท\n"

    receipt += f"""{line}
ยอดรวมสุทธิ: {total:>18} บาท
ชำระโดย: {req.payment_method:>20}
"""

    if req.payment_method == PaymentMethod.CASH:
        receipt += f"รับเงินสด: {req.cash_received:>19} บาท\n"
        receipt += f"เงินทอน:   {change:>19} บาท\n"
    
    receipt += f"""{line}
แต้มที่ได้: {points} คะแนน
{double_line}
   ขอบคุณที่อุดหนุนครับ! (Thank You)
{double_line}
"""
    return receipt