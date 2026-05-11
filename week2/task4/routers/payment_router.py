from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import payment_crud
from schemas.payment_schemas import PaymentCreate, PaymentOut, PaymentUpdate

router = APIRouter()


@router.get("/", response_model=list[PaymentOut])
def list_payments(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return payment_crud.get_payments(db, skip, limit)


@router.get("/{customerNumber}/{checkNumber}", response_model=PaymentOut)
def get_payment(customerNumber: int, checkNumber: str, db: Session = Depends(database.get_db)):
    return payment_crud.get_payment(db, customerNumber, checkNumber)


@router.get("/customer/{customerNumber}", response_model=list[PaymentOut])
def get_customer_payments(customerNumber: int, db: Session = Depends(database.get_db)):
    return payment_crud.get_payments_by_customer(db, customerNumber)


@router.post("/", response_model=PaymentOut)
def create_payment(data: PaymentCreate, db: Session = Depends(database.get_db)):
    return payment_crud.create_payment(db, data)


@router.put("/{customerNumber}/{checkNumber}", response_model=PaymentOut)
def update_payment(
    customerNumber: int,
    checkNumber: str,
    data: PaymentUpdate,
    db: Session = Depends(database.get_db),
):
    return payment_crud.update_payment(db, customerNumber, checkNumber, data)


@router.delete("/{customerNumber}/{checkNumber}")
def delete_payment(customerNumber: int, checkNumber: str, db: Session = Depends(database.get_db)):
    payment_crud.delete_payment(db, customerNumber, checkNumber)
    return {"message": "Deleted"}
