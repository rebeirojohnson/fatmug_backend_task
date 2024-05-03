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

* [tree-md](./tree-md)
 * [dir2](./dir2)
   * [file21.ext](./dir2/file21.ext)
   * [file22.ext](./dir2/file22.ext)
   * [file23.ext](./dir2/file23.ext)
 * [dir1](./dir1)
   * [file11.ext](./dir1/file11.ext)
   * [file12.ext](./dir1/file12.ext)
 * [file_in_root.ext](./file_in_root.ext)
 * [README.md](./README.md)
 * [dir3](./dir3)

> [!TIP]
> Optional information to help a user be more successful.

> [!CAUTION]
> Crucial information necessary for users to succeed.

> [!WARNING]  
> Critical content demanding immediate user attention due to potential risks.

> [!IMPORTANT]  
> For the Demo purpose the .env file is pushed to GIT but during real production the env files will be encrypted and not pushed to GitHUB.