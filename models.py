from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)


class Vendor(Base):

    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_email = Column(String)

    available_stock = Column(Integer)


class ProductVendor(Base):

    __tablename__ = "product_vendor_mapping"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))


class PurchaseOrder(Base):

    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    quantity = Column(Integer)

    status = Column(String, default="Pending")