from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    dept: str
    age: int
    city: str
    

employee = Employee(name="Poorani", dept="IT", age=35, city="Wilmington")
print(employee)