from pydantic import BaseModel

class Employee(BaseModel):
    fname:str
    lname:str
    age:int

class Employee_Login(BaseModel):
    username:str
    password:str
    

class ShowEmployee(Employee):
    class Config():
        orm_mode=True

class ShowEmployee_Login(BaseModel):
    username:str
    class Config():
        orm_mode=True

class Login( BaseModel):
    username:str
    password:str

