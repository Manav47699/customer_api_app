from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.employee_schemas import EmployeeCreate, EmployeeUpdate


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employee(db: Session, employee_number: int):
    item = db.query(models.Employee).filter(models.Employee.employeeNumber == employee_number).first()
    if not item:
        not_found("Employee", employee_number)
    return item


def create_employee(db: Session, data: EmployeeCreate):
    item = models.Employee(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create employee")
    db.refresh(item)
    return item


def update_employee(db: Session, employee_number: int, data: EmployeeUpdate):
    item = get_employee(db, employee_number)
    update_fields(item, data)
    commit_or_422(db, "Update employee")
    db.refresh(item)
    return item


def delete_employee(db: Session, employee_number: int):
    item = get_employee(db, employee_number)
    db.delete(item)
    delete_commit_or_409(db, "Delete employee")


def get_employee_with_customers(db: Session, employee_number: int):
    employee = get_employee(db, employee_number)
    return {"employee": employee, "customers": employee.customers or []}


def get_employee_reports(db: Session, employee_number: int):
    get_employee(db, employee_number)
    return db.query(models.Employee).filter(models.Employee.reportsTo == employee_number).all()
