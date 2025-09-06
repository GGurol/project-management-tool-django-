# Django Project Management Application

This is a Django-based Project Management Application project.


## Project Base:

Framework : Django 5.2

Database : SQLite


### Installation

Follow these steps to set up and run the Django Pet Clinic Application:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GGurol/project-management-tool-django.git
   ```

2. Navigate to the project directory:

   ```bash
   cd project-management-tool-django
   ```

3. Build the docker and build:

   ```bash
   docker compose up --build -d
   ```

4. Apply database migrations:

   ```bash
   docker compose exec web python manage.py makemigrations
   docker compose exec web python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. Access the application in your web browser at `http://localhost:8000`.


