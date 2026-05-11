from typing import Optional

from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    employeeNumber: int
    lastName: str = Field(max_length=50)
    firstName: str = Field(max_length=50)
    extension: str = Field(max_length=10)
    email: str = Field(max_length=100)
    officeCode: str = Field(max_length=10)
    reportsTo: Optional[int] = None
    jobTitle: str = Field(max_length=50)


class EmployeeOut(EmployeeCreate):
    class Config:
        from_attributes = True


class EmployeeUpdate(BaseModel):
    lastName: Optional[str] = Field(default=None, max_length=50)
    firstName: Optional[str] = Field(default=None, max_length=50)
    extension: Optional[str] = Field(default=None, max_length=10)
    email: Optional[str] = Field(default=None, max_length=100)
    officeCode: Optional[str] = Field(default=None, max_length=10)
    reportsTo: Optional[int] = None
    jobTitle: Optional[str] = Field(default=None, max_length=50)
