from typing import Optional

from pydantic import BaseModel, Field


class OfficeCreate(BaseModel):
    officeCode: str = Field(max_length=10)
    city: str = Field(max_length=50)
    phone: str = Field(max_length=50)
    addressLine1: str = Field(max_length=50)
    addressLine2: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)
    country: str = Field(max_length=50)
    postalCode: str = Field(max_length=15)
    territory: str = Field(max_length=10)


class OfficeOut(OfficeCreate):
    class Config:
        from_attributes = True


class OfficeUpdate(BaseModel):
    city: Optional[str] = Field(default=None, max_length=50)
    phone: Optional[str] = Field(default=None, max_length=50)
    addressLine1: Optional[str] = Field(default=None, max_length=50)
    addressLine2: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=50)
    country: Optional[str] = Field(default=None, max_length=50)
    postalCode: Optional[str] = Field(default=None, max_length=15)
    territory: Optional[str] = Field(default=None, max_length=10)
