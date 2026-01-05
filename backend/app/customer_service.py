import pandas as pd
import uuid
import os
from .excel_init import init_excel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUSTOMER_FILE = os.path.join(BASE_DIR, "data", "customers.xlsx")

init_excel(
    CUSTOMER_FILE,
    ["customer_id", "name", "email", "password"]
)

def get_customer_by_email(email: str):
    df = pd.read_excel(CUSTOMER_FILE)

    # 🔥 Normalize Excel values
    df["email"] = df["email"].astype(str).str.strip().str.lower()
    df["password"] = df["password"].astype(str).str.strip()

    email = email.strip().lower()

    row = df[df["email"] == email]
    if row.empty:
        return None

    return row.iloc[0].to_dict()


def add_customer(name: str, email: str, password: str):
    df = pd.read_excel(CUSTOMER_FILE)

    if email in df["email"].values:
        return None

    customer_id = f"CUST-{uuid.uuid4().hex[:8]}"

    df.loc[len(df)] = {
        "customer_id": customer_id,
        "name": name,
        "email": email,
        "password": password
    }

    df.to_excel(CUSTOMER_FILE, index=False)
    return customer_id
