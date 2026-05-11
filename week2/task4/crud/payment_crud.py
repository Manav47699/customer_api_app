from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.payment_schemas import PaymentCreate, PaymentUpdate


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Payment).offset(skip).limit(limit).all()


def get_payment(db: Session, customer_number: int, check_number: str):
    item = (
        db.query(models.Payment)
        .filter(
            models.Payment.customerNumber == customer_number,
            models.Payment.checkNumber == check_number,
        )
        .first()
    )
    if not item:
        not_found("Payment", f"{customer_number}/{check_number}")
    return item


def create_payment(db: Session, data: PaymentCreate):
    item = models.Payment(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create payment")
    db.refresh(item)
    return item


def update_payment(db: Session, customer_number: int, check_number: str, data: PaymentUpdate):
    item = get_payment(db, customer_number, check_number)
    update_fields(item, data)
    commit_or_422(db, "Update payment")
    db.refresh(item)
    return item


def delete_payment(db: Session, customer_number: int, check_number: str):
    item = get_payment(db, customer_number, check_number)
    db.delete(item)
    delete_commit_or_409(db, "Delete payment")


def get_payments_by_customer(db: Session, customer_number: int):
    return db.query(models.Payment).filter(models.Payment.customerNumber == customer_number).all()
