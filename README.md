# Setting up Django Project with Virtual Environment on macOS

This guide provides step-by-step instructions to set up a Django project with a virtual environment on macOS. By following these steps, you can isolate your project dependencies and manage multiple Django projects effortlessly.

## Step 1: Installing Virtual Environment

Create a virtual environment using Python's built-in `venv` module.

```bash
python3 -m venv <envname>
```

Replace `<envname>` with your desired environment name, for example:

```bash
python3 -m venv myenv
```

## Step 2: Activating Virtual Environment

Activate the virtual environment using the following command:

```bash
source <envname>/bin/activate
```

For example:

```bash
source myenv/bin/activate
```

## Step 3: Installing Django

Install Django inside the activated virtual environment using pip.

```bash
pip install django==4.0
```

## Step 4: Creating Django Project

Create a new Django project using the `django-admin` command.

```bash
django-admin startproject <projname>
```

Replace `<projname>` with your desired project name.

## Step 5: Creating Django App

Navigate into your project directory and create a new Django app.

```bash
cd <projname>
django-admin startapp <appname>
```

Replace `<appname>` with your desired app name.

## Step 6: Registering App in settings.py

Add your newly created app to the `INSTALLED_APPS` list in your project's `settings.py` file.

## Step 7: Making Migrations

Generate database migrations for your models and apply them to the database.

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 8: Running the Project

Start the Django development server to run your project.

```bash
python manage.py runserver
```

## Step 9: Creating Admin User

Create a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

Follow the prompts to enter your desired username, email, and password.

```

```
