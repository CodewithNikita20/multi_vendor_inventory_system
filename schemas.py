from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    description: str


class VendorCreate(BaseModel):
    name: str
    contact_email: str
    available_stock: int


class ProductVendorCreate(BaseModel):
    product_id: int
    vendor_id: int


class PurchaseOrderCreate(BaseModel):
    product_id: int
    vendor_id: int
    quantity: int


class OrderStatusUpdate(BaseModel):
    status: str