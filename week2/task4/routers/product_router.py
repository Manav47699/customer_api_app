from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import product_crud
from schemas.product_schemas import ProductCreate, ProductOut, ProductUpdate

router = APIRouter()


@router.get("/", response_model=list[ProductOut])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return product_crud.get_products(db, skip, limit)


@router.get("/{productCode}", response_model=ProductOut)
def get_product(productCode: str, db: Session = Depends(database.get_db)):
    return product_crud.get_product(db, productCode)


@router.get("/{productCode}/orderdetails")
def get_product_orderdetails(productCode: str, db: Session = Depends(database.get_db)):
    return product_crud.get_product_with_orderdetails(db, productCode)


@router.post("/", response_model=ProductOut)
def create_product(data: ProductCreate, db: Session = Depends(database.get_db)):
    return product_crud.create_product(db, data)


@router.put("/{productCode}", response_model=ProductOut)
def update_product(productCode: str, data: ProductUpdate, db: Session = Depends(database.get_db)):
    return product_crud.update_product(db, productCode, data)


@router.delete("/{productCode}")
def delete_product(productCode: str, db: Session = Depends(database.get_db)):
    product_crud.delete_product(db, productCode)
    return {"message": "Deleted"}
