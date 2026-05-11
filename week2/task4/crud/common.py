from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from logger import get_logger

logger = get_logger(__name__)


def commit_or_422(db: Session, action: str):
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        logger.error("%s failed due to integrity error: %s", action, exc)
        raise HTTPException(status_code=422, detail="Constraint validation failed")


def delete_commit_or_409(db: Session, action: str):
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        logger.error("%s failed due to reference error: %s", action, exc)
        raise HTTPException(status_code=409, detail="Cannot delete: record is referenced by other rows")


def not_found(entity: str, identifier):
    logger.warning("%s not found: %s", entity, identifier)
    raise HTTPException(status_code=404, detail=f"{entity} not found")


def update_fields(db_obj, data):
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_obj, key, value)
