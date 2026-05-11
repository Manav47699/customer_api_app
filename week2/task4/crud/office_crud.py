from sqlalchemy.orm import Session

import models
from crud.common import commit_or_422, delete_commit_or_409, not_found, update_fields
from schemas.office_schemas import OfficeCreate, OfficeUpdate


def get_offices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Office).offset(skip).limit(limit).all()


def get_office(db: Session, office_code: str):
    item = db.query(models.Office).filter(models.Office.officeCode == office_code).first()
    if not item:
        not_found("Office", office_code)
    return item


def create_office(db: Session, data: OfficeCreate):
    item = models.Office(**data.model_dump())
    db.add(item)
    commit_or_422(db, "Create office")
    db.refresh(item)
    return item


def update_office(db: Session, office_code: str, data: OfficeUpdate):
    item = get_office(db, office_code)
    update_fields(item, data)
    commit_or_422(db, "Update office")
    db.refresh(item)
    return item


def delete_office(db: Session, office_code: str):
    item = get_office(db, office_code)
    db.delete(item)
    delete_commit_or_409(db, "Delete office")


def get_office_with_employees(db: Session, office_code: str):
    office = get_office(db, office_code)
    return {"office": office, "employees": office.employees or []}
