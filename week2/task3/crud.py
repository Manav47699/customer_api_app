from sqlalchemy.orm import Session

import models
from database import SessionLocal
from logger import get_logger

logger = get_logger(__name__)


def _count_rows(db: Session, model, label: str) -> int:
    logger.info("Count query started for %s", label)
    count = db.query(model).count()
    logger.info("Count query completed for %s: %s", label, count)
    return count


def get_customers_count(db: Session) -> int:
    return _count_rows(db, models.Customer, "customers")


def get_orders_count(db: Session) -> int:
    return _count_rows(db, models.Order, "orders")


def get_products_count(db: Session) -> int:
    return _count_rows(db, models.Product, "products")


def get_employees_count(db: Session) -> int:
    return _count_rows(db, models.Employee, "employees")


def get_offices_count(db: Session) -> int:
    return _count_rows(db, models.Office, "offices")


def get_payments_count(db: Session) -> int:
    return _count_rows(db, models.Payment, "payments")


def get_orderdetails_count(db: Session) -> int:
    return _count_rows(db, models.OrderDetail, "orderdetails")


def get_productlines_count(db: Session) -> int:
    return _count_rows(db, models.ProductLine, "productlines")


def _run_with_new_session(counter_func):
    db = SessionLocal()
    try:
        return counter_func(db)
    except Exception as exc:
        logger.error("Database count operation failed: %s", exc)
        raise
    finally:
        db.close()


def get_customers_count_threadsafe() -> int:
    return _run_with_new_session(get_customers_count)


def get_orders_count_threadsafe() -> int:
    return _run_with_new_session(get_orders_count)


def get_products_count_threadsafe() -> int:
    return _run_with_new_session(get_products_count)


def get_employees_count_threadsafe() -> int:
    return _run_with_new_session(get_employees_count)


def get_offices_count_threadsafe() -> int:
    return _run_with_new_session(get_offices_count)


def get_payments_count_threadsafe() -> int:
    return _run_with_new_session(get_payments_count)


def get_orderdetails_count_threadsafe() -> int:
    return _run_with_new_session(get_orderdetails_count)


def get_productlines_count_threadsafe() -> int:
    return _run_with_new_session(get_productlines_count)
