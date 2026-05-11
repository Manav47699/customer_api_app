from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.orderdetail_schemas import OrderDetailCreate, OrderDetailUpdate


def get_orderdetails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderDetail).offset(skip).limit(limit).all()


def get_orderdetail(db: Session, order_number: int, product_code: str):
    item = (
        db.query(models.OrderDetail)
        .filter(
            models.OrderDetail.orderNumber == order_number,
            models.OrderDetail.productCode == product_code,
        )
        .first()
    )
    if not item:
        not_found("OrderDetail", f"{order_number}/{product_code}")
    return item


def create_orderdetail(db: Session, data: OrderDetailCreate):
    item = models.OrderDetail(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create orderdetail")
    db.refresh(item)
    return item


def update_orderdetail(db: Session, order_number: int, product_code: str, data: OrderDetailUpdate):
    item = get_orderdetail(db, order_number, product_code)
    update_fields(item, data)
    commit_or_422(db, "Update orderdetail")
    db.refresh(item)
    return item


def delete_orderdetail(db: Session, order_number: int, product_code: str):
    item = get_orderdetail(db, order_number, product_code)
    db.delete(item)
    delete_commit_or_409(db, "Delete orderdetail")


def get_orderdetails_by_order(db: Session, order_number: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.orderNumber == order_number).all()


def get_orderdetails_by_product(db: Session, product_code: str):
    return db.query(models.OrderDetail).filter(models.OrderDetail.productCode == product_code).all()
