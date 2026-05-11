from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import productline_crud
from schemas.productline_schemas import ProductLineCreate, ProductLineOut, ProductLineUpdate

router = APIRouter()


@router.get("/", response_model=list[ProductLineOut])
def list_productlines(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return productline_crud.get_productlines(db, skip, limit)


@router.get("/{productLine}", response_model=ProductLineOut)
def get_productline(productLine: str, db: Session = Depends(database.get_db)):
    return productline_crud.get_productline(db, productLine)


@router.get("/{productLine}/products")
def get_productline_products(productLine: str, db: Session = Depends(database.get_db)):
    return productline_crud.get_productline_with_products(db, productLine)


@router.post("/", response_model=ProductLineOut)
def create_productline(data: ProductLineCreate, db: Session = Depends(database.get_db)):
    return productline_crud.create_productline(db, data)


@router.put("/{productLine}", response_model=ProductLineOut)
def update_productline(productLine: str, data: ProductLineUpdate, db: Session = Depends(database.get_db)):
    return productline_crud.update_productline(db, productLine, data)


@router.delete("/{productLine}")
def delete_productline(productLine: str, db: Session = Depends(database.get_db)):
    productline_crud.delete_productline(db, productLine)
    return {"message": "Deleted"}
