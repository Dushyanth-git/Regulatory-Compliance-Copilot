import pandas as pd
import os
from .excel_init import init_excel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMPLOYEE_FILE = os.path.join(BASE_DIR, "data", "employees.xlsx")

init_excel(
    EMPLOYEE_FILE,
    ["empid", "password", "role"]
)

def get_employee(empid: str):
    try:
        df = pd.read_excel(EMPLOYEE_FILE)
    except Exception:
        return None

    # 🔥 Normalize Excel values
    df["empid"] = df["empid"].astype(str).str.strip()
    df["password"] = df["password"].astype(str).str.strip()

    empid = empid.strip()

    row = df[df["empid"] == empid]
    if row.empty:
        return None

    return row.iloc[0].to_dict()


def add_employee(empid: str, password: str, role: str):
    try:
        df = pd.read_excel(EMPLOYEE_FILE)
    except Exception:
        return False

    if empid in df["empid"].values:
        return False

    df.loc[len(df)] = {
        "empid": empid,
        "password": password,
        "role": role
    }

    df.to_excel(EMPLOYEE_FILE, index=False)
    return True
