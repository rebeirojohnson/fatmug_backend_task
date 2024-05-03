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

## Using the Test Files

> [!TIP]
> To check the results without using another application, I have created files in a folder called local_testing to demonstrate the use of the application.

1. **login.py**
    - *Used to perform the Authentication of the User.*

2. **view_all_vendors.py**
    - *Fetch the list of all the Vendors.*

3. **add_new_vendor.py**
    - *Create a new Vendor and add to the database.*

4. **view_all_purchase_orders.py**
    - *Fetch all the purchase orders, optionally filtered by vendor code.*

5. **view_purchase_order_detail.py**
    - *Fetch details of a specific purchase order.*

6. **delete_purchase_order_detail.py**
    - *Delete a specific purchase order.*

7. **order_acknowledge.py**
    - *Acknowledge an order.*

8. **delete_vendor.py**
    - *Delete a vendor.*

9. **view_vendor_details.py**
    - *View details of a specific vendor.*

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

> [!CAUTION]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.

> [!IMPORTANT]
> For the demo purpose, the .env file is pushed to Git but during real production, the env files will be encrypted and not pushed to GitHub.