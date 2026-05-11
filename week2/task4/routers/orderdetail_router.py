from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import orderdetail_crud
from schemas.orderdetail_schemas import OrderDetailCreate, OrderDetailOut, OrderDetailUpdate

router = APIRouter()


@router.get("/", response_model=list[OrderDetailOut])
def list_orderdetails(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return orderdetail_crud.get_orderdetails(db, skip, limit)


@router.get("/{orderNumber}/{productCode}", response_model=OrderDetailOut)
def get_orderdetail(orderNumber: int, productCode: str, db: Session = Depends(database.get_db)):
    return orderdetail_crud.get_orderdetail(db, orderNumber, productCode)


@router.get("/order/{orderNumber}", response_model=list[OrderDetailOut])
def get_order_orderdetails_list(orderNumber: int, db: Session = Depends(database.get_db)):
    return orderdetail_crud.get_orderdetails_by_order(db, orderNumber)


@router.get("/product/{productCode}", response_model=list[OrderDetailOut])
def get_product_orderdetails_list(productCode: str, db: Session = Depends(database.get_db)):
    return orderdetail_crud.get_orderdetails_by_product(db, productCode)


@router.post("/", response_model=OrderDetailOut)
def create_orderdetail(data: OrderDetailCreate, db: Session = Depends(database.get_db)):
    return orderdetail_crud.create_orderdetail(db, data)


@router.put("/{orderNumber}/{productCode}", response_model=OrderDetailOut)
def update_orderdetail(
    orderNumber: int,
    productCode: str,
    data: OrderDetailUpdate,
    db: Session = Depends(database.get_db),
):
    return orderdetail_crud.update_orderdetail(db, orderNumber, productCode, data)


@router.delete("/{orderNumber}/{productCode}")
def delete_orderdetail(orderNumber: int, productCode: str, db: Session = Depends(database.get_db)):
    orderdetail_crud.delete_orderdetail(db, orderNumber, productCode)
    return {"message": "Deleted"}
