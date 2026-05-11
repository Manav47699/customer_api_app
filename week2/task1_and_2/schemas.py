from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class CustomerSchema(BaseModel):
    customerNumber: int
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: str
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: Optional[Decimal] = None

#pydantic excepts an dictionary but db sends a object. the below block tells pydantic to just look for the attribute/column inside the object
    class Config:
        from_attributes = True