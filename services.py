from sqlalchemy.orm import Session
import models


def create_product(db: Session, payload):

    product = models.Product(
        name=payload.name,
        description=payload.description
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def register_vendor(db: Session, payload):

    vendor = models.Vendor(
        name=payload.name,
        contact_email=payload.contact_email,
        available_stock=payload.available_stock
    )

    db.add(vendor)
    db.commit()
    db.refresh(vendor)

    return vendor


def map_product_vendor(db: Session, payload):

    mapping = models.ProductVendor(
        product_id=payload.product_id,
        vendor_id=payload.vendor_id
    )

    db.add(mapping)

    db.commit()

    db.refresh(mapping)

    return mapping


def create_purchase_order(db: Session, payload):

    vendor = db.query(models.Vendor).filter(
        models.Vendor.id == payload.vendor_id
    ).first()

    if vendor.available_stock < payload.quantity:
        raise Exception("Not enough stock")

    vendor.available_stock -= payload.quantity

    order = models.PurchaseOrder(
        product_id=payload.product_id,
        vendor_id=payload.vendor_id,
        quantity=payload.quantity,
        status="Pending"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def update_order_status(db: Session, order_id: int, status: str):

    order = db.query(models.PurchaseOrder).filter(
        models.PurchaseOrder.id == order_id
    ).first()

    order.status = status

    db.commit()
    db.refresh(order)

    return order