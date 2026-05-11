from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ProductCreate(BaseModel):
    productCode: str = Field(max_length=15)
    productName: str = Field(max_length=70)
    productLine: str = Field(max_length=50)
    productScale: str = Field(max_length=10)
    productVendor: str = Field(max_length=50)
    productDescription: str
    quantityInStock: int = Field(ge=0)
    buyPrice: Decimal
    MSRP: Decimal

    @model_validator(mode="after")
    def validate_price(self):
        if self.MSRP < self.buyPrice:
            raise ValueError("MSRP must be greater than or equal to buyPrice")
        return self


class ProductOut(ProductCreate):
    class Config:
        from_attributes = True


class ProductUpdate(BaseModel):
    productName: Optional[str] = Field(default=None, max_length=70)
    productLine: Optional[str] = Field(default=None, max_length=50)
    productScale: Optional[str] = Field(default=None, max_length=10)
    productVendor: Optional[str] = Field(default=None, max_length=50)
    productDescription: Optional[str] = None
    quantityInStock: Optional[int] = Field(default=None, ge=0)
    buyPrice: Optional[Decimal] = None
    MSRP: Optional[Decimal] = None

    @model_validator(mode="after")
    def validate_price(self):
        if self.buyPrice is not None and self.MSRP is not None and self.MSRP < self.buyPrice:
            raise ValueError("MSRP must be greater than or equal to buyPrice")
        return self
