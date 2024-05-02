Vendor Management System with Performance Metrics

Features:

Vendor Profiles: Create and manage vendor profiles with essential details.
Purchase Order Tracking: Track purchase orders with status updates and history.
Vendor Performance Metrics: Calculate and display vendor performance metrics like delivery time, quality, and reliability.

Key Components:

Django for backend development.
Django REST Framework for building RESTful APIs.

Installation:

Clone the repository.
Set up a virtual environment.
Install dependencies using pip (pip install -r requirements.txt).
Run migrations to create the database schema.
Start the development server. (python manage.py runserver)

Usage:

Access the admin interface to manage vendor profiles and purchase orders.
Utilize RESTful APIs for integrating with other systems or building custom interfaces.



superuser
username : admin
password : admin@123

or Create new superuser
python manage.py createsuperuser

To provide an authentication token in Postman, you can follow these steps:

Obtain Authentication Token:
/api/token/
{
    "username" : "admin",
    "password" : "admin@123"
}
Set Authorization Header:
Open Postman and create a new request or open an existing one.
In the request headers section, add a new header with the key Authorization.
Set the value of the header to Token <your_authentication_token_here>, replacing <your_authentication_token_here> with the actual token you obtained.
Send Request:
Once you have set the Authorization header, you can send the request as usual.
Postman will include the token in the request headers, and your Django application will authenticate the request accordingly.


VENDORS
/api/vendors/

● POST /api/vendors/: Create a new vendor.
● GET /api/vendors/: List all vendors.
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
● DELETE /api/vendors/{vendor_id}/: Delete a vendor.

Example input for creating new Vendor:  
{  
    "name":"V1 Corporation",
    "contact_details":"John Doe - john@example.com, 9876543210",
    "address":"123 Main Street, Kerala, India",
    "vendor_code":"VEND001",
    "on_time_delivery_rate":0.85,
    "quality_rating_avg":4.2,
    "average_response_time":2.5,
    "fulfillment_rate":0.92
 }

PURCHASE ORDERS
/api/purchase_orders/

● POST /api/purchase_orders/: Create a purchase order.
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order


Example input for creating new Purchase Order:  

{
    "po_number":"PO00001",
    "vendor":3, #Vendor Id
    "order_date":"2024-05-03 11:00:00",
    "delivery_date":"2024-05-13 14:00:00",
    "items":[
        {"item_name": "Product A", "description": "Good Quality", "unit_price": 20.75},
        {"item_name": "Product B", "description": "Nice Product", "unit_price": 15.72}
        ],
    "quantity":200,
    "status":"completed",
    "quality_rating":4.2,
    "issue_date":"2024-05-03 11:00:00",
    "acknowledgment_date":"2024-05-08 09:00:00"
}




GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics.



CONTACT
Arun Krishna V B
Email : arunkvb98@gmail.com