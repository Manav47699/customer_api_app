from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, model_validator


class OrderCreate(BaseModel):
    orderNumber: int
    orderDate: date
    requiredDate: date
    shippedDate: Optional[date] = None
    status: Literal["Shipped", "Resolved", "Cancelled", "On Hold", "Disputed", "In Process"]
    comments: Optional[str] = None
    customerNumber: int

    @model_validator(mode="after")
    def validate_required_date(self):
        if self.requiredDate < self.orderDate:
            raise ValueError("requiredDate must be after or equal to orderDate")
        return self


class OrderOut(OrderCreate):
    class Config:
        from_attributes = True


class OrderUpdate(BaseModel):
    orderDate: Optional[date] = None
    requiredDate: Optional[date] = None
    shippedDate: Optional[date] = None
    status: Optional[
        Literal["Shipped", "Resolved", "Cancelled", "On Hold", "Disputed", "In Process"]
    ] = None
    comments: Optional[str] = None
    customerNumber: Optional[int] = None

    @model_validator(mode="after")
    def validate_required_date(self):
        if self.orderDate is not None and self.requiredDate is not None:
            if self.requiredDate < self.orderDate:
                raise ValueError("requiredDate must be after or equal to orderDate")
        return self
