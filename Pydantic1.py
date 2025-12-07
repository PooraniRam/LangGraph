from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    dept: str
    age: int
    city: str
    

employee = Employee(name="Poorani", dept="IT", age=35, city="Wilmington123")
print("Base Model :",employee)

type(employee)


from dataclasses import dataclass
@dataclass
class Employee():
    name: str
    dept: str
    age: int
    city: str

employee = Employee(name="Poorani", dept="IT", age=35, city="Wilmington")
print("Data Class :",employee)


# Model with optional field
from typing import Optional
class Employee(BaseModel):
    name: str
    dept: str
    age: int
    city: str
    salary: Optional[float] = None # Optional with default value
    isActive: Optional[bool] = True # Optional wiht default value
    

employee = Employee(name="Poorani", dept="IT", age=35, city="Wilmington")
employee = Employee(name="Poorani", dept="IT", age=35, city="Wilmington", salary=135000.00, isActive=0)
print("Base Model :",employee) 


#Definition
# Optional[type] : Indicates the field can be None
# Default value( = None or = true ): Makes the field optional
# Required fields must still be provided
# Pydantic validate types even for optional fields when values are provided

from typing import List

class ClassRoom(BaseModel):
    roomNo: int
    students: List[str] # List of string
    capacity:int

classroom = ClassRoom(
    roomNo=101,
    students=("Maha", "Adhi", "Bob"),
    capacity=30
)

print("Class Room :", classroom)