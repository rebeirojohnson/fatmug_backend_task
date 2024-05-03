# FatMug Backend Task

## How to Setup the Project

There are two ways to run this project for the demo purpose. The easy and straightforward way is to run the code locally, while the second is to run the code with Docker, which is a better solution.

### Locally

1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
2. Navigate to the project directory: `cd fatmug_backend_task`
3. Install requirements: `RUN pip install -r requirements.txt --no-cache`
4. Start the application: `python manage.py runserver 0.0.0.0:8000`
5. Open your web browser and navigate to `http://localhost:8000`.

> [!NOTE]
> Use `--no-cache` to install as sometimes cached install of Django rest framework causes issues with static files.

### Using Docker (Recommended)

1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
2. Navigate to the project directory: `cd fatmug_backend_task`
3. Build the Image: `docker build --tag "docker.fatmug.backend" .`
4. Start the application: `docker compose up -d`
5. Open your web browser and navigate to `http://localhost:8000`.

> [!TIP]
> This project is also hosted using Docker on an AWS instance and can be interacted with directly at http://65.2.40.22:8000/.

## How to Interact with the Project

Now that the application is set up, we can start using the application.

> [!IMPORTANT]
> Since all endpoints are secured using authentication, we need to first authenticate to use the other endpoints.


    URL = "http://127.0.0.1:8000/api/login/"

    PAYLOAD = {
        "username":"admin",
        "password":"admin"
    }

    REQUEST_METHOD = POST
   

> [!WARNING]
> For the demo purpose, the username and password are set to admin bypassing the password validation such as minimum length, similarity, and common password list check.

## Interacting with the API Endpoints

> [!TIP]
> To check the results without using another application, I have created files in a folder called local_testing to demonstrate the use of the application.

1. **POST /api/login/**
    - *Used to perform the Authentication of the User.*
    - File - login.py
    - Payload 
        ```json
            {
                "username":"admin",
                "password":"admin"
            }
        ```
    - Response 

        Valid Credentails

            {
                "message": "Login Success"
            }

        Invalid Credentails

            {
                "error": "Invalid credentials"
            }


2. **GET /api/vendors/**
    - *Fetch the list of all the Vendors.*
    - File - view_all_vendors.py
    - Response

    ```json
        [
            {
                "vendor_code": "NVFCH",
                "name": "Test Vendor",
                "contact_details": "12345678",
                "address": "Dubai"
            },
            {
                "vendor_code": "JSPMIL",
                "name": "Johnson Solution Pvt",
                "contact_details": "7899404714",
                "address": "India"
            }
        ]
    ```

3. **POST /api/vendors/**
    - *Create a new Vendor and add to the database.*
    - File - add_new_vendor.py
    - Payload
        ```json
        {
            "name": "Python Vendor",
            "contact_details": "987654321",
            "address": "New Zeland"
        }
        ```
    - Reponse
        ```json
            {
                "vendor_code": "PVIJI",
                "name": "Python Vendor",
                "contact_details": "987654321",
                "address": "New Zeland"
            }
        ```

4. **GET /api/vendors/{vendor_id}/**
    - File - view_vendor_details.py
    - *View details of a specific vendor.*
    - Response
        ```json
            {
                "vendor_code": "NVFCH",
                "name": "New Vendor",
                "contact_details": null,
                "address": "Dubai"
            }
        ```
5. **POST /api/vendors/{vendor_id}/**
    - File - update_vendor_details.py
    - *View details of a specific vendor.*
    - Payload
        ```json
            {
                "name": "New Tech Name",
                "contact_details": "New Address",
                "address": "777777"
            }
        ```
    - Response
        ```json
            {
                "vendor_code": "NVFCH",
                "name": "New Tech Name",
                "contact_details": "New Address",
                "address": "777777"
            }
        ```
6. **DELETE /api/vendors/{vendor_id}/**
    - File - delete_vendor.py
    - *Delete a vendor.*
    - Response
        ```
            API - No Response 204 
            Python - Vendor Deleted Successfully
        ```

7. **GET /api/purchase_orders/?vendor_code=vendor_code**
    - *Fetch all the purchase orders, optionally filtered by vendor code.*
    - File - view_all_purchase_orders.py
    - Params (Optinal) - vendor_code
    - Reponse All Vendor
        ```json
            [
                {
                    "po_number": "258a9267-b337-458f-99d6-dbc3fcd77fdd",
                    "delivery_date": "2024-01-01T05:30:00+05:30",
                    "status": "completed",
                    "vendor_id": "NSLZO"
                },
                {
                    "po_number": "80ffc765-b5ee-4e04-9fc0-eedac30ef88b",
                    "delivery_date": "2024-01-01T05:30:00+05:30",
                    "status": "completed",
                    "vendor_id": "NVOOV"
                },
                {
                    "po_number": "f1e0f118-1714-45e5-876b-11b549060922",
                    "delivery_date": "2024-01-01T05:30:00+05:30",
                    "status": "completed",
                    "vendor_id": "NSLZO"
                }
            ]
        ```
    - Reponse Specific Vendor - NSLZO
        ```json
            [
                {
                    "po_number": "258a9267-b337-458f-99d6-dbc3fcd77fdd",
                    "delivery_date": "2024-01-01T05:30:00+05:30",
                    "status": "completed",
                    "vendor_id": "NSLZO"
                },
                {
                    "po_number": "f1e0f118-1714-45e5-876b-11b549060922",
                    "delivery_date": "2024-01-01T05:30:00+05:30",
                    "status": "completed",
                    "vendor_id": "NSLZO"
                }
            ]
        ```
8. **POST /api/purchase_orders/**
    - *Creates a new Purchase Order with auto generated order id*
    - File - create_purchase_order.py
    - Payload
        ```json
            {
                "order_date": "2025-01-01T00:00:00Z",
                "delivery_date": "2025-02-01T00:00:00Z",
                "items": [
                    {
                        "item": "item 1"
                    },
                    {
                        "item": "item 2"
                    }
                ],
                "quantity": 2,
                "status": "completed",
                "quality_rating": 2.5,
                "vendor": "NVFCH"
            }
        ```
    - Reponse 
        ```json
            {
                "po_number": "7e0305e6-0276-4349-99a7-829e79759b0d",
                "order_date": "2025-01-01T05:30:00+05:30",
                "delivery_date": "2025-02-01T05:30:00+05:30",
                "items": [
                    {
                        "item": "item 1"
                    },
                    {
                        "item": "item 2"
                    }
                ],
                "quantity": 2,
                "status": "completed",
                "quality_rating": 2.5,
                "issue_date": "2024-05-03T19:18:50.863815+05:30",
                "acknowledgment_date": null,
                "is_product_delivered_on_time": true,
                "vendor": "NVFCH"
            }
        ```


8. **GET /api/purchase_orders/{po_id}/:**
    - *Fetch details of a specific purchase order.*
    - Params - po_id - purchase_order_number
    - File - view_purchase_order_detail.py
    - Response
        ```json
            {
                "po_number": "f1e0f118-1714-45e5-876b-11b549060922",
                "order_date": "2024-01-01T05:30:00+05:30",
                "delivery_date": "2024-01-01T05:30:00+05:30",
                "items": [],
                "quantity": 0,
                "status": "completed",
                "quality_rating": 5.0,
                "issue_date": "2024-05-03T10:16:19.030802+05:30",
                "acknowledgment_date": "2024-05-03T10:16:19.030519+05:30",
                "is_product_delivered_on_time": false,
                "vendor": "NSLZO"
            }
        ```

8. **PATCH /api/purchase_orders/{po_id}/:**
    - *Update Details of purchase order.*
    - Params - po_id - purchase_order_number
    - File - edit_purchase_order.py
    - Payload
        ```json
            {
                "order_date": "2025-01-01T00:00:00Z",
                "delivery_date": "2025-02-01T00:00:00Z",
                "items": [],
                "quantity": 0,
                "status": "completed",
                "quality_rating": 8.5,
                "vendor": "NVFCH"
            }
        ```
    - Response
        ```json
            {
                "po_number": "258a9267-b337-458f-99d6-dbc3fcd77fdd",
                "order_date": "2025-01-01T05:30:00+05:30",
                "delivery_date": "2025-02-01T05:30:00+05:30",
                "items": [],
                "quantity": 0,
                "status": "completed",
                "quality_rating": 8.5,
                "issue_date": "2024-05-03T19:12:40.099724+05:30",
                "acknowledgment_date": null,
                "is_product_delivered_on_time": true,
                "vendor": "NVFCH"
            }
        ```

9. **DELETE /api/purchase_orders/{po_id}/**
    - *Delete a specific purchase order.*
    - File - delete_purchase_order_detail.py
    - Response
        ```
        API - No Response - 204 Status
        Python - Product Order Deleted Successfully 
        ```
    
10. **POST /api/purchase_orders/{po_id}/acknowledge/**
    - File - order_acknowledge.py
    - *Acknowledge an order.*
    - Reponse
        ```json
            {
                "message": "Acknowledgment date updated successfully"
            }
        ```



The testing files are by default set to interact with the hosted version of the application. If you want to interact with the locally installed application, it can be done by modifying the .env file.


    SERVER_IP = 65.2.40.22:8000

    # Set to 127.0.0.1:8000 for Local testing


## Updating the Vendor Performance

The update of the performance is done using a function called update vendor performance.

```sql
declare

average_quality_rating_for_vendor float = 0;
average_on_time_delivery_rate_temp float = 0;
average_response_time_temp float = 0;
average_fulfillment_rate_temp float = 0;

begin

average_quality_rating_for_vendor = (SELECT avg(quality_rating) as average_quality_rating FROM django_data.api_purchaseorder
where vendor_id = vendor_id_inp);

average_fulfillment_rate_temp = ((SELECT (COUNT(CASE WHEN status ilike 'completed' THEN 1 END) * 100.0) / COUNT(*) AS completion_percentage FROM django_data.api_purchaseorder
where vendor_id = vendor_id_inp));

average_response_time_temp = (SELECT avg(EXTRACT(EPOCH FROM (acknowledgment_date - issue_date))) AS time_difference_seconds
FROM django_data.api_purchaseorder
where vendor_id = vendor_id_inp
);

update django_data.api_vendor 
set quality_rating_avg = average_quality_rating_for_vendor,
on_time_delivery_rate = average_on_time_delivery_rate_temp,
average_response_time = average_response_time_temp,
fulfillment_rate = average_fulfillment_rate_temp
where vendor_code = vendor_id_inp;

INSERT INTO django_data.api_historicalperformance(
    on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate, vendor_id)
    VALUES (average_on_time_delivery_rate_temp, average_quality_rating_for_vendor,average_response_time_temp, average_fulfillment_rate_temp,vendor_id_inp);


return 'success';

end

```

> [!NOTE]
> As this function runs within the database, the execution of the code is much faster than calculating with Python and then updating the database.


> [!IMPORTANT]
> For the demo purpose, the .env file is pushed to Git but during real production, the env files will be encrypted and not pushed to GitHub.