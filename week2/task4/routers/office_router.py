from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import office_crud
from schemas.office_schemas import OfficeCreate, OfficeOut, OfficeUpdate

router = APIRouter()


@router.get("/", response_model=list[OfficeOut])
def list_offices(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return office_crud.get_offices(db, skip, limit)


@router.get("/{officeCode}", response_model=OfficeOut)
def get_office(officeCode: str, db: Session = Depends(database.get_db)):
    return office_crud.get_office(db, officeCode)


@router.get("/{officeCode}/employees")
def get_office_employees(officeCode: str, db: Session = Depends(database.get_db)):
    return office_crud.get_office_with_employees(db, officeCode)


@router.post("/", response_model=OfficeOut)
def create_office(data: OfficeCreate, db: Session = Depends(database.get_db)):
    return office_crud.create_office(db, data)


@router.put("/{officeCode}", response_model=OfficeOut)
def update_office(officeCode: str, data: OfficeUpdate, db: Session = Depends(database.get_db)):
    return office_crud.update_office(db, officeCode, data)


@router.delete("/{officeCode}")
def delete_office(officeCode: str, db: Session = Depends(database.get_db)):
    office_crud.delete_office(db, officeCode)
    return {"message": "Deleted"}
