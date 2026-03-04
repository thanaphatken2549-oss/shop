
class Store:
    def __init__(self):
        self.products = []
        self.member_system = MemberSystem()
        self.employees = []

class Person:
    def __init__(self, person_id: str, name: str, phone: str = None):
        self.person_id = person_id
        self.name = name
        self.phone = phone

    def update_contact_info(self, phone: str):
        self.phone = phone

class Customer(Person):
    def __init__(self, person_id: str, name: str, phone: str = None):
        super().__init__(person_id, name, phone)

    def provide_phone(self):
        return self.phone

class Employee(Person):
    def __init__(self, person_id: str, name: str, phone: str, employee_id: str):
        super().__init__(person_id, name, phone)
        self.employee_id = employee_id

    def clock_in(self):
        pass

    def clock_out(self):
        pass

class Cashier(Employee):
    def __init__(self, person_id, name, phone, employee_id, member_system):
        super().__init__(person_id, name, phone, employee_id)
        self.member_system = member_system

    def ask_phone(self, customer):
        return customer.provide_phone()

    def checkout(self, customer, basket, payment_type):
        transaction = SaleTransaction(basket)
        total = transaction.calculate_total()
        phone = self.ask_phone(customer)
        member = None
        phone = customer.provide_phone()
        if phone:
            member = self.member_system.check_member(phone)
            if member:
                member.add_points(total)

        if payment_type == "CASH":
            payment = CashPayment(total, cash_received=500)
        else:
            payment = OnlinePayment(total)

        payment_result = payment.process()

        for item in basket.items:
            item.deduct_stock()

        receipt = Receipt(transaction, payment_result, member)
        receipt.print_receipt()

class Member:
    def __init__(self, phone: str, points: int = 0):
        self.phone = phone
        self.points = points

    def add_points(self, amount: float):
        earned = int(amount // 10)
        self.points += earned
        return earned
    
class MemberSystem:
    def __init__(self):
        self.members = {
            "0812345678": Member("0812345678", 120)
        }

    def check_member(self, phone: str):
        return self.members.get(phone)

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock_qty: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_qty = stock_qty

    def deduct_stock(self, qty: int):
        if self.stock_qty < qty:
            raise ValueError("Stock not enough")
        self.stock_qty -= qty


class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, product: Product):
        self.items.append(product)

class SaleTransaction:
    def __init__(self, basket: Basket):
        self.basket = basket
        self.total = 0.0

    def calculate_total(self):
        self.total = sum(item.price for item in self.basket.items)
        return self.total

class Payment:
    def __init__(self, amount: float):
        self.amount = amount

    def process(self):
        raise NotImplementedError

class CashPayment(Payment):
    def __init__(self, amount: float, cash_received: float):
        super().__init__(amount)
        self.cash_received = cash_received

    def process(self):
        if self.cash_received < self.amount:
            raise ValueError("เงินสดไม่พอ")
        return {
            "status": "PAID",
            "change": self.cash_received - self.amount
        }

import uuid

class OnlinePayment(Payment):
    def __init__(self, amount: float):
        super().__init__(amount)
        self.slip_id = None

    def process(self):
        self.slip_id = str(uuid.uuid4())
        return {
            "status": "PAID",
            "slip": self.slip_id
        }

class Receipt:
    def __init__(self, transaction, payment_result, member=None):
        self.transaction = transaction
        self.payment_result = payment_result
        self.member = member

    def print_receipt(self):
        print("====== RECEIPT ======")
        for item in self.transaction.basket.items:
            print(f"{item.name} {item.price} บาท")

        print(f"TOTAL: {self.transaction.total} บาท")

        if "change" in self.payment_result:
            print(f"CHANGE: {self.payment_result['change']} บาท")

        if "slip" in self.payment_result:
            print(f"SLIP ID: {self.payment_result['slip']}")

        if self.member:
            print(f"POINT BALANCE: {self.member.points}")

        print("=====================")
