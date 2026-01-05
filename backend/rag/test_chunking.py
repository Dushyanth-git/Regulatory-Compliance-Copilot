from pdf_loader import extract_pdf_pages
from chunker import chunk_pages

# -------- CUSTOMER --------
customer_pdf = "backend/data/customer/customer_rights.pdf"
customer_pages = extract_pdf_pages(customer_pdf)
customer_chunks = chunk_pages(customer_pages, audience="customer")

print("=== CUSTOMER CHUNKS ===")
print("Total chunks:", len(customer_chunks))
print(customer_chunks[0]["text"][:700])
print("Page:", customer_chunks[0]["page"])

# -------- EMPLOYEE --------
employee_pdf = "backend/data/employee/banking acts- for employees.pdf"
employee_pages = extract_pdf_pages(employee_pdf)
employee_chunks = chunk_pages(employee_pages, audience="employee")

print("\n=== EMPLOYEE CHUNKS ===")
print("Total chunks:", len(employee_chunks))
print(employee_chunks[0]["text"][:700])
print("Page:", employee_chunks[0]["page"])
