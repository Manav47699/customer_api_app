from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.order_schemas import OrderCreate, OrderUpdate


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()


def get_order(db: Session, order_number: int):
    item = db.query(models.Order).filter(models.Order.orderNumber == order_number).first()
    if not item:
        not_found("Order", order_number)
    return item


def create_order(db: Session, data: OrderCreate):
    item = models.Order(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create order")
    db.refresh(item)
    return item


def update_order(db: Session, order_number: int, data: OrderUpdate):
    item = get_order(db, order_number)
    update_fields(item, data)
    commit_or_422(db, "Update order")
    db.refresh(item)
    return item


def delete_order(db: Session, order_number: int):
    item = get_order(db, order_number)
    db.delete(item)
    delete_commit_or_409(db, "Delete order")


def get_order_with_orderdetails(db: Session, order_number: int):
    order = get_order(db, order_number)
    return {"order": order, "orderdetails": order.orderdetails or []}


def get_orders_by_customer(db: Session, customer_number: int):
    return db.query(models.Order).filter(models.Order.customerNumber == customer_number).all()
