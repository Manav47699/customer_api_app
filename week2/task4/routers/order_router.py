from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import order_crud
from schemas.order_schemas import OrderCreate, OrderOut, OrderUpdate

router = APIRouter()


@router.get("/", response_model=list[OrderOut])
def list_orders(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return order_crud.get_orders(db, skip, limit)


@router.get("/{orderNumber}", response_model=OrderOut)
def get_order(orderNumber: int, db: Session = Depends(database.get_db)):
    return order_crud.get_order(db, orderNumber)


@router.get("/{orderNumber}/orderdetails")
def get_order_orderdetails(orderNumber: int, db: Session = Depends(database.get_db)):
    return order_crud.get_order_with_orderdetails(db, orderNumber)


@router.get("/customer/{customerNumber}", response_model=list[OrderOut])
def get_customer_orders(customerNumber: int, db: Session = Depends(database.get_db)):
    return order_crud.get_orders_by_customer(db, customerNumber)


@router.post("/", response_model=OrderOut)
def create_order(data: OrderCreate, db: Session = Depends(database.get_db)):
    return order_crud.create_order(db, data)


@router.put("/{orderNumber}", response_model=OrderOut)
def update_order(orderNumber: int, data: OrderUpdate, db: Session = Depends(database.get_db)):
    return order_crud.update_order(db, orderNumber, data)


@router.delete("/{orderNumber}")
def delete_order(orderNumber: int, db: Session = Depends(database.get_db)):
    order_crud.delete_order(db, orderNumber)
    return {"message": "Deleted"}
