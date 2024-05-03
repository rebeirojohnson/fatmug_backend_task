# FatMug Backend Task

## How to run the project

### Locally

    1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
    2. Navigate to the project directory: `cd fatmug_backend_task`
    3. Install requirements: `RUN pip install -r requirements.txt --no-cache`
    4. Start the application: `python manage.py runserver 0.0.0.0:8000`
    5. Open your web browser and navigate to `http://localhost:8000`.

    
### Using Docker (Recommended)
    1. Clone the repository: `git clone https://github.com/rebeirojohnson/fatmug_backend_task.git`
    2. Navigate to the project directory: `cd fatmug_backend_task`
    3. Build the Image: `docker build --tag "docker.fatmug.backend" .`
    4. Start the application: `docker compose up -d`
    5. Open your web browser and navigate to `http://localhost:8000`.

> [!NOTE]  
> Use --no-cache to install as sometimes cached install of Django rest framework causes issue with static files.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]  
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!CAUTION]
> Negative potential consequences of an action.