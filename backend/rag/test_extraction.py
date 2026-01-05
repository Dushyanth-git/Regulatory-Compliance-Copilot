from pdf_loader import extract_pdf_pages

# -----------------------
# Customer PDF
# -----------------------
customer_pdf = "backend/data/customer/customer_rights.pdf"

print("=== CUSTOMER PDF ===")
customer_pages = extract_pdf_pages(customer_pdf)
print(f"Total pages extracted: {len(customer_pages)}")

if customer_pages:
    print("Sample text (page 1):\n")
    print(customer_pages[0]["text"][:600])


# -----------------------
# Employee PDF
# -----------------------
employee_pdf = "backend/data/employee/banking acts- for employees.pdf"

print("\n=== EMPLOYEE PDF ===")
employee_pages = extract_pdf_pages(employee_pdf)
print(f"Total pages extracted: {len(employee_pages)}")

if employee_pages:
    print("Sample text (page 1):\n")
    print(employee_pages[0]["text"][:600])
