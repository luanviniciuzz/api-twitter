# MINI Twitter API

The Mini-Twitter API is a scalable RESTful service for a lightweight social media platform, allowing users to connect and interact through posts. It features user registration, authentication, and various interaction capabilities, creating a dynamic space for sharing thoughts and updates.

<img src="EDR.png" alt="Exemplo imagem">

> EDR Diagram

### TECHNICAL REQUIREMENTS

Tasks completed for the trainee position:

- [x] [TC.1] API Development
- [x] [TC.2] Authentication
- [x] [TC.3] Database
- [x] [TC.4.] Pagination
- [x] [TC.6] Documentation

## 💻 Requirements

Before you begin, make sure you have met the following requirements:

- Python 3.8 +
- PostgreSQL

## 🚀 Instalation - MINI Twitter API

1. **Clone the repository**

    ```bash
    git clone https://github.com/luanviniciuzz/api-twitter.git
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    On Windows:
    ```bash
    .\venv\Scripts\Activate.ps1
    ```

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

    Make sure that `requirements.txt` includes the necessary libraries, such as `Django`, `djangorestframework`, and `psycopg2`.

5. **Configure the Database**

    In the `settings.py` file, locate the database configuration and replace it with your database details:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'database_name',
            'USER': 'username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

6. **Run migrations**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser (optional)**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the instructions to create an admin user.

8. **Start the server**

    ```bash
    python manage.py runserver
    ```

    Your API will be available with the SWAGGER documentation at `http://127.0.0.1:8000/api/docs/#/`.
    Or Admin User `http://127.0.0.1:8000/admin`


## ☕ USE CASES MINI TWITTER API
 - To register, access the API and provide your email, username, and password. Use JSON Web Tokens (JWT) to manage your authentication when logging in and for session management. After authenticating, you can create a post that includes text and one image. You can also like posts from other users. You have the ability to follow or unfollow other users as you wish, and your feed will display only the posts from the users you are following. You can view a paginated list of posts from the users you follow, and the posts will be displayed in chronological order, from the most recent to the oldest. Follow these instructions to navigate the platform effectively!
```


