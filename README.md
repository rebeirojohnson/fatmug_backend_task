# FatMug Backend Task

## How to Setup the project

There are two ways to run this project for the demo purpose. The easy and straight forward way being running the code locally, while the second being running the code with docker which is better solution.

### Locally

    1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
    2. Navigate to the project directory: `cd fatmug_backend_task`
    3. Install requirements: `RUN pip install -r requirements.txt --no-cache`
    4. Start the application: `python manage.py runserver 0.0.0.0:8000`
    5. Open your web browser and navigate to `http://localhost:8000`.

    
> [!NOTE]  
> Use --no-cache to install as sometimes cached install of Django rest framework causes issue with static files.

### Using Docker (Recommended)
    1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
    2. Navigate to the project directory: `cd fatmug_backend_task`
    3. Build the Image: `docker build --tag "docker.fatmug.backend" .`
    4. Start the application: `docker compose up -d`
    5. Open your web browser and navigate to `http://localhost:8000`.

## How to Interact with the project
Now that the application is set up we can start using the application 

> [!NOTE]  
> Since All endpoints are secured using authentication. We need to first authenticate to use the other endpoints 

    URL = "http://127.0.0.1:8000/api/login/"

    PAYLOAD = {
        "username":"admin",
        "password":"admin"
    }

    REQUEST_METHOD = POST
   
> [!NOTE] 

> For the demo purpose the username and password are set to admin bypassing the password validation such as minimun length, similarity and common password list check

> [!TIP]
> Optional information to help a user be more successful.

> [!CAUTION]
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!IMPORTANT]  
> For the Demo purpose the .env file is pushed to GIT but during real production the env files will be encrypted and not pushed to GitHUB.