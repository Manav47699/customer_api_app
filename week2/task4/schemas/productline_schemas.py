from typing import Optional

from pydantic import BaseModel, Field


class ProductLineCreate(BaseModel):
    productLine: str = Field(max_length=50)
    textDescription: Optional[str] = Field(default=None, max_length=4000)
    htmlDescription: Optional[str] = None


class ProductLineOut(ProductLineCreate):
    class Config:
        from_attributes = True


class ProductLineUpdate(BaseModel):
    textDescription: Optional[str] = Field(default=None, max_length=4000)
    htmlDescription: Optional[str] = None
