from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter()

@router.get("/customers", response_model=list[schemas.CustomerSchema])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@router.get("/customers/{customerNumber}", response_model=schemas.CustomerSchema)
def read_one(customerNumber: int, db: Session = Depends(database.get_db)):
    customer = crud.get_customer(db, id=customerNumber)
    if not customer: raise HTTPException(status_code=404, detail="Not found")
    return customer

@router.post("/customers", response_model=schemas.CustomerSchema)
def create(customer: schemas.CustomerSchema, db: Session = Depends(database.get_db)):
    return crud.create_customer(db, customer_data=customer)

@router.put("/customers/{customerNumber}", response_model=schemas.CustomerSchema)
def update(customerNumber: int, customer: schemas.CustomerSchema, db: Session = Depends(database.get_db)):
    return crud.update_customer(db, id=customerNumber, data=customer)

@router.delete("/customers/{customerNumber}")
def delete(customerNumber: int, db: Session = Depends(database.get_db)):
    if not crud.delete_customer(db, id=customerNumber): raise HTTPException(status_code=404)
    return {"message": "Deleted"}