from fastapi import FastAPI
from . import schemas

from .customer_service import add_customer, get_customer_by_email
from .employee_service import get_employee, add_employee

app = FastAPI(title="Customer Auth Service (Excel-backed)")

# -------------------------
# Admin database (pre-seeded)
# -------------------------
admindb = {
    "ADMIN001": {
        "adminid": "ADMIN001",
        "password": "compliance"
    }
}

# -------------------------
# Customer Register
# -------------------------
@app.post("/customer/register")
def register_customer(request: schemas.RegisterRequest):

    customer_id = add_customer(
        request.name,
        request.email,
        request.password
    )

    if not customer_id:
        return {
            "success": False,
            "message": "User already exists. Please login."
        }

    return {
        "success": True,
        "message": "Registration successful.",
        "customer_id": customer_id
    }

# -------------------------
# Customer Login
# -------------------------
@app.post("/customer/login")
def login_customer(request: schemas.LoginRequest):

    customer = get_customer_by_email(request.email)

    if not customer or customer["password"] != request.password:
        return {
            "success": False,
            "message": "Invalid email or password."
        }

    return {
        "success": True,
        "message": "Login successful.",
        "customer_id": customer["customer_id"],
        "name": customer["name"]
    }

# -------------------------
# Employee Login
# -------------------------
@app.post("/employee/login")
def login_employee(request: schemas.LoginRequestemp):

    emp = get_employee(request.empid)

    if not emp or emp["password"].strip() != request.password.strip():

        return {
            "success": False,
            "message": "Invalid employee id or password."
        }

    return {
        "success": True,
        "message": "Login successful.",
        "role": emp["role"]
    }

# -------------------------
# Admin Login
# -------------------------
@app.post("/admin/login")
def admin_login(request: schemas.AdminLoginRequest):
    adminid = request.adminid.strip().upper()
    password = request.password.strip()

    admin = admindb.get(adminid)

    if not admin or admin["password"] != password:
        return {
            "success": False,
            "message": "Invalid admin credentials"
        }

    return {
        "success": True,
        "message": "Admin login successful"
    }

# -------------------------
# Admin creates employee
# -------------------------
@app.post("/admin/create-employee")
def create_employee(request: schemas.EmployeeRegisterRequest):

    success = add_employee(
        request.empid,
        request.password,
        request.role
    )

    if not success:
        return {
            "success": False,
            "message": "Employee already exists"
        }

    return {
        "success": True,
        "message": "Employee created successfully"
    }

# -------------------------
# Health Check
# -------------------------
@app.get("/health")
def health():
    return {"status": "ok"}
