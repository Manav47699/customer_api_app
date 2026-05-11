from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class CustomerCreate(BaseModel):
    customerNumber: int
    customerName: str = Field(max_length=50)
    contactLastName: str = Field(max_length=50)
    contactFirstName: str = Field(max_length=50)
    phone: str = Field(max_length=50)
    addressLine1: str = Field(max_length=50)
    addressLine2: Optional[str] = Field(default=None, max_length=50)
    city: str = Field(max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)
    postalCode: Optional[str] = Field(default=None, max_length=15)
    country: str = Field(max_length=50)
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: Optional[Decimal] = None


class CustomerOut(CustomerCreate):
    class Config:
        from_attributes = True


class CustomerUpdate(BaseModel):
    customerName: Optional[str] = Field(default=None, max_length=50)
    contactLastName: Optional[str] = Field(default=None, max_length=50)
    contactFirstName: Optional[str] = Field(default=None, max_length=50)
    phone: Optional[str] = Field(default=None, max_length=50)
    addressLine1: Optional[str] = Field(default=None, max_length=50)
    addressLine2: Optional[str] = Field(default=None, max_length=50)
    city: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)
    postalCode: Optional[str] = Field(default=None, max_length=15)
    country: Optional[str] = Field(default=None, max_length=50)
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: Optional[Decimal] = None
