# multi_vendor_inventory_system
A backend service built using Python, FastAPI and PostgreSQL to manage products, vendors, and purchase orders.
This service simulates a simple procurement workflow used in product companies where vendors supply products and purchase orders are created to procure items.

Features:

Product management
Vendor registration with available stock
Product–Vendor mapping
Purchase order creation
Automatic vendor stock deduction when orders are placed
Order status updates (Pending / Approved / Delivered)

Tech Stack:

Python
FastAPI
PostgreSQL


Project Structure:
project/
│
├── main.py            # API routes
├── models.py          # Database models
├── schemas.py         # Request/response schemas
├── services.py        # Business logic
├── database.py        # Database connection
├── requirements.txt   # Python dependencies
└── README.md

Setup Instructions
1 Install dependencies
pip install -r requirements.txt
2 Create PostgreSQL database
CREATE DATABASE kitchen_inventory;
3 Configure database connection
Update the database URL in database.py.

Example:

DATABASE_URL = "postgresql://postgres:password@localhost:5432/kitchen_inventory"
4 Run the server
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
5 Open API Docs
http://127.0.0.1:8000/docs
API Workflow

Typical workflow:

1 Create Product
2 Register Vendor
3 Link Product with Vendor
4 Create Purchase Order
5 Vendor stock gets reduced automatically
6 Update order status

Example Use Case:
Vendor A supplies 100 units of Oven.
A purchase order is created for 5 units.
System automatically updates vendor stock:
100 → 95

Future Improvements:

-Pagination and filtering APIs
-Docker containerization
-Authentication and authorization

Author
Nikita
