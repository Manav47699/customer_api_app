from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from crud import employee_crud
from schemas.employee_schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate

router = APIRouter()


@router.get("/", response_model=list[EmployeeOut])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return employee_crud.get_employees(db, skip, limit)


@router.get("/{employeeNumber}", response_model=EmployeeOut)
def get_employee(employeeNumber: int, db: Session = Depends(database.get_db)):
    return employee_crud.get_employee(db, employeeNumber)


@router.get("/{employeeNumber}/customers")
def get_employee_customers(employeeNumber: int, db: Session = Depends(database.get_db)):
    return employee_crud.get_employee_with_customers(db, employeeNumber)


@router.get("/{employeeNumber}/reports", response_model=list[EmployeeOut])
def get_employee_reports(employeeNumber: int, db: Session = Depends(database.get_db)):
    return employee_crud.get_employee_reports(db, employeeNumber)


@router.post("/", response_model=EmployeeOut)
def create_employee(data: EmployeeCreate, db: Session = Depends(database.get_db)):
    return employee_crud.create_employee(db, data)


@router.put("/{employeeNumber}", response_model=EmployeeOut)
def update_employee(employeeNumber: int, data: EmployeeUpdate, db: Session = Depends(database.get_db)):
    return employee_crud.update_employee(db, employeeNumber, data)


@router.delete("/{employeeNumber}")
def delete_employee(employeeNumber: int, db: Session = Depends(database.get_db)):
    employee_crud.delete_employee(db, employeeNumber)
    return {"message": "Deleted"}
