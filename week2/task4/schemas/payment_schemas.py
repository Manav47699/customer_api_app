from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class PaymentCreate(BaseModel):
    customerNumber: int
    checkNumber: str = Field(max_length=50)
    paymentDate: date
    amount: Decimal = Field(gt=0)

    @model_validator(mode="after")
    def validate_date(self):
        if self.paymentDate > date.today():
            raise ValueError("paymentDate cannot be in the future")
        return self


class PaymentOut(PaymentCreate):
    class Config:
        from_attributes = True


class PaymentUpdate(BaseModel):
    paymentDate: Optional[date] = None
    amount: Optional[Decimal] = Field(default=None, gt=0)

    @model_validator(mode="after")
    def validate_date(self):
        if self.paymentDate is not None and self.paymentDate > date.today():
            raise ValueError("paymentDate cannot be in the future")
        return self
