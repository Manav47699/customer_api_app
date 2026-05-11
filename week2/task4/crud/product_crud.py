from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.product_schemas import ProductCreate, ProductUpdate


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_code: str):
    item = db.query(models.Product).filter(models.Product.productCode == product_code).first()
    if not item:
        not_found("Product", product_code)
    return item


def create_product(db: Session, data: ProductCreate):
    item = models.Product(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create product")
    db.refresh(item)
    return item


def update_product(db: Session, product_code: str, data: ProductUpdate):
    item = get_product(db, product_code)
    update_fields(item, data)
    commit_or_422(db, "Update product")
    db.refresh(item)
    return item


def delete_product(db: Session, product_code: str):
    item = get_product(db, product_code)
    db.delete(item)
    delete_commit_or_409(db, "Delete product")


def get_product_with_orderdetails(db: Session, product_code: str):
    product = get_product(db, product_code)
    return {"product": product, "orderdetails": product.orderdetails or []}
