import asyncio
import time

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import database
from logger import get_logger

logger = get_logger(__name__)
router = APIRouter()


@router.get("/customers/count")
def count_customers(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /customers/count")
    count = crud.get_customers_count(db)
    logger.info("Response success: GET /customers/count")
    return {"customers": count}


@router.get("/orders/count")
def count_orders(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /orders/count")
    count = crud.get_orders_count(db)
    logger.info("Response success: GET /orders/count")
    return {"orders": count}


@router.get("/products/count")
def count_products(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /products/count")
    count = crud.get_products_count(db)
    logger.info("Response success: GET /products/count")
    return {"products": count}


@router.get("/employees/count")
def count_employees(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /employees/count")
    count = crud.get_employees_count(db)
    logger.info("Response success: GET /employees/count")
    return {"employees": count}


@router.get("/offices/count")
def count_offices(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /offices/count")
    count = crud.get_offices_count(db)
    logger.info("Response success: GET /offices/count")
    return {"offices": count}


@router.get("/payments/count")
def count_payments(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /payments/count")
    count = crud.get_payments_count(db)
    logger.info("Response success: GET /payments/count")
    return {"payments": count}


@router.get("/orderdetails/count")
def count_orderdetails(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /orderdetails/count")
    count = crud.get_orderdetails_count(db)
    logger.info("Response success: GET /orderdetails/count")
    return {"orderdetails": count}


@router.get("/productlines/count")
def count_productlines(db: Session = Depends(database.get_db)):
    logger.info("Incoming request: GET /productlines/count")
    count = crud.get_productlines_count(db)
    logger.info("Response success: GET /productlines/count")
    return {"productlines": count}


@router.get("/overall_counts")
async def get_overall_counts():
    start_time = time.perf_counter()
    logger.info("Incoming request: GET /overall_counts")
    logger.info("Starting all concurrent count tasks")

    results = await asyncio.gather(
        asyncio.to_thread(crud.get_customers_count_threadsafe),
        asyncio.to_thread(crud.get_orders_count_threadsafe),
        asyncio.to_thread(crud.get_products_count_threadsafe),
        asyncio.to_thread(crud.get_employees_count_threadsafe),
        asyncio.to_thread(crud.get_offices_count_threadsafe),
        asyncio.to_thread(crud.get_payments_count_threadsafe),
        asyncio.to_thread(crud.get_orderdetails_count_threadsafe),
        asyncio.to_thread(crud.get_productlines_count_threadsafe),
    )

    elapsed = time.perf_counter() - start_time
    logger.info("asyncio.gather completed for /overall_counts in %.4f seconds", elapsed)
    logger.info("Response success: GET /overall_counts")

    return {
        "customers": results[0],
        "orders": results[1],
        "products": results[2],
        "employees": results[3],
        "offices": results[4],
        "payments": results[5],
        "orderdetails": results[6],
        "productlines": results[7],
    }
