from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequestemp(BaseModel):
    empid:str
    password:str

class AdminLoginRequest(BaseModel):
    adminid: str
    password: str

class EmployeeRegisterRequest(BaseModel):
    empid: str
    password: str
    role: str
