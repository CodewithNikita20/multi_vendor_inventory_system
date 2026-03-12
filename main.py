from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base

import schemas
import services
import models


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Multi Vendor Inventory Service")


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/products")
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    return services.create_product(db, payload)

@app.get("/products")
def list_products(db: Session = Depends(get_db)):

    products = db.query(models.Product).all()

    return products

@app.post("/vendors")
def create_vendor(payload: schemas.VendorCreate, db: Session = Depends(get_db)):
    return services.register_vendor(db, payload)

@app.get("/vendors")
def list_vendors(db: Session = Depends(get_db)):
    vendors = db.query(models.Vendor).all()
    return vendors

@app.post("/product-vendor")
def link_product_vendor(payload: schemas.ProductVendorCreate, db: Session = Depends(get_db)):
    return services.map_product_vendor(db, payload)

@app.get("/product-vendor")
def list_product_vendor(db: Session = Depends(get_db)):

    mapping = db.query(models.ProductVendor).all()

    return mapping

@app.post("/purchase-orders")
def create_order(payload: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    return services.create_purchase_order(db, payload)

@app.get("/purchase-orders")
def list_purchase_orders(db: Session = Depends(get_db)):
    orders = db.query(models.PurchaseOrder).all()
    return orders

@app.put("/purchase-orders/{order_id}/status")
def update_order_status(order_id: int, payload: schemas.OrderStatusUpdate, db: Session = Depends(get_db)):
    return services.update_order_status(db, order_id, payload.status)

