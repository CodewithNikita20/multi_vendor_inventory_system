API Testing Example:

1. Create Product
POST /products
Example:
{
  "name": "Industrial Oven",
  "description": "Large capacity oven used for bakery production"
}

2. Register Vendor
POST /vendors
Example:
{
  "name": "KitchenEquip Suppliers",
  "contact_email": "sales@kitchenequip.com",
  "available_stock": 120
}

3. Link Product with Vendor
POST /product-vendor
Example:
{
  "product_id": 1,
  "vendor_id": 1
}

4. Create Purchase Order
POST /purchase-orders
Example:
{
  "product_id": 1,
  "vendor_id": 1,
  "quantity": 10
}

Vendor Stock
120 → 110

5. Update Order Status
PUT /purchase-orders/1/status
Example:
{
  "status": "Ordered"
}

Possible statuses:

Ordered
Approved
Delivered