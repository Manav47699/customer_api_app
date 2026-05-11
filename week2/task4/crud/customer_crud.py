from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.customer_schemas import CustomerCreate, CustomerUpdate


def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def get_customer(db: Session, customer_number: int):
    item = db.query(models.Customer).filter(models.Customer.customerNumber == customer_number).first()
    if not item:
        not_found("Customer", customer_number)
    return item


def create_customer(db: Session, data: CustomerCreate):
    item = models.Customer(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create customer")
    db.refresh(item)
    return item


def update_customer(db: Session, customer_number: int, data: CustomerUpdate):
    item = get_customer(db, customer_number)
    update_fields(item, data)
    commit_or_422(db, "Update customer")
    db.refresh(item)
    return item


def delete_customer(db: Session, customer_number: int):
    item = get_customer(db, customer_number)
    db.delete(item)
    delete_commit_or_409(db, "Delete customer")
