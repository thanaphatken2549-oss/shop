from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from enum import Enum

app = FastAPI()

# --- 1. Models & Schemas (ตาม Class Diagram) ---

class PaymentStatus(str, Enum):
    SUCCESS = "Success"
    PENDING = "Pending"
    FAILED = "Failed"

class PaymentChannel(str, Enum):
    CASH = "Cash"
    QR = "QR"

class Staff(BaseModel):
    staff_id: str
    name: str

class Order(BaseModel):
    order_id: str
    status: str
    payment_id: str

class Payment(BaseModel):
    payment_id: str
    status: PaymentStatus
    channel: PaymentChannel

# --- 2. Logic Services (จำลองฐานข้อมูล/Internal Logic) ---

def get_staff_from_db(staff_id: str) -> Optional[Staff]:
    # จำลองการหา Staff
    if staff_id == "staff123":
        return Staff(staff_id="staff123", name="Somchai")
    return None

def get_order_from_db(order_id: str) -> Optional[Order]:
    if order_id == "ord-001":
        return Order(order_id="ord-001", status="Processing", payment_id="pay-999")
    return None

def get_payment_from_db(payment_id: str) -> Optional[Payment]:
    if payment_id == "pay-999":
        return Payment(payment_id="pay-999", status=PaymentStatus.SUCCESS, channel=PaymentChannel.QR)
    return None

# --- 3. ShopController (FastAPI Endpoints) ---

@app.post("/transaction/create", status_code=status.HTTP_201_CREATED)
async def create_transaction(staff_id: str, order_id: str):
    
    # --- STEP 1: Validate Staff ---
    staff = get_staff_from_db(staff_id)
    if not staff:
        # ตรงกับส่วน alt: is Invalid Staff
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Error: Unauthorized Staff"
        )
    # else: Authorized Staff (ไปต่อ)

    # --- STEP 2: Fetch Order & Payment Info ---
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    payment = get_payment_from_db(order.payment_id)
    
    # Check Payment Status (ตรงกับ alt: Payment Success/Not Success)
    if not payment or payment.status != PaymentStatus.SUCCESS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Error: Cannot process unpaid order"
        )

    # Get Payment Channel
    channel = payment.channel # ดึงว่าเป็น Cash หรือ QR

    # --- STEP 3: Create Sale Transaction ---
    # ใน Logic จริงตรงนี้จะไปเรียก Class SaleTransaction()
    transaction_result = {
        "transaction_id": "TX-2024-001",
        "processed_by": staff.name,
        "order_details": order.order_id,
        "payment_method": channel,
        "receipt": f"RECEIPT_DATA_FOR_{order.order_id}",
        "status": "Transaction Completed"
    }

    return transaction_result

# Helper function
def get_order_by_id(order_id: str):
    return get_order_from_db(order_id)