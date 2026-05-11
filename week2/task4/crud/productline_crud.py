from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.productline_schemas import ProductLineCreate, ProductLineUpdate


def get_productlines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductLine).offset(skip).limit(limit).all()


def get_productline(db: Session, product_line: str):
    item = db.query(models.ProductLine).filter(models.ProductLine.productLine == product_line).first()
    if not item:
        not_found("ProductLine", product_line)
    return item


def create_productline(db: Session, data: ProductLineCreate):
    item = models.ProductLine(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create productline")
    db.refresh(item)
    return item


def update_productline(db: Session, product_line: str, data: ProductLineUpdate):
    item = get_productline(db, product_line)
    update_fields(item, data)
    commit_or_422(db, "Update productline")
    db.refresh(item)
    return item


def delete_productline(db: Session, product_line: str):
    item = get_productline(db, product_line)
    db.delete(item)
    delete_commit_or_409(db, "Delete productline")


def get_productline_with_products(db: Session, product_line: str):
    item = get_productline(db, product_line)
    return {"productline": item, "products": item.products or []}
