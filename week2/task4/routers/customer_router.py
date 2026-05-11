from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import customer_crud
from schemas.customer_schemas import CustomerCreate, CustomerOut, CustomerUpdate

router = APIRouter()


@router.get("/", response_model=list[CustomerOut])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return customer_crud.get_customers(db, skip=skip, limit=limit)


@router.get("/{customerNumber}", response_model=CustomerOut)
def read_one(customerNumber: int, db: Session = Depends(database.get_db)):
    return customer_crud.get_customer(db, customerNumber)


@router.post("/", response_model=CustomerOut)
def create(customer: CustomerCreate, db: Session = Depends(database.get_db)):
    return customer_crud.create_customer(db, customer)


@router.put("/{customerNumber}", response_model=CustomerOut)
def update(customerNumber: int, customer: CustomerUpdate, db: Session = Depends(database.get_db)):
    return customer_crud.update_customer(db, customerNumber, customer)


@router.delete("/{customerNumber}")
def delete(customerNumber: int, db: Session = Depends(database.get_db)):
    customer_crud.delete_customer(db, customerNumber)
    return {"message": "Deleted"}
