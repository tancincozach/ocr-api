# Django REST API

## Overview

This project is a basic REST API built with Django and Django REST Framework. It provides endpoints for user authentication and access control using JWT tokens.

## Features

- **User Authentication**: Login, logout, and token management using JWT.
- **Dynamic Route Guarding**: Middleware that protects API routes based on authentication status.
- **Admin Interface**: Built-in Django admin for managing users and other entities.

## Installation

### Prerequisites

- Python 3.11 or higher
- Docker and Docker Compose

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install dependencies:**

    Using Docker:
    
    ```bash
    docker-compose build
    ```

    Without Docker:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**

    Create a `.env` file based on the `.env.example` and set your environment variables.

4. **Run migrations:**

    Using Docker:

    ```bash
    docker-compose run web python manage.py migrate
    ```

    Without Docker:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for admin access):**

    Using Docker:

    ```bash
    docker-compose run web python manage.py createsuperuser
    ```

    Without Docker:

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**

    Using Docker:

    ```bash
    docker-compose up
    ```

    Without Docker:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Login**: `POST /api/login/`
  - Request body: `{ "username": "user", "password": "pass" }`
  - Response: `{ "access": "JWT_ACCESS_TOKEN", "refresh": "JWT_REFRESH_TOKEN" }`

- **Refresh Token**: `POST /api/token/refresh/`
  - Request body: `{ "refresh": "JWT_REFRESH_TOKEN" }`
  - Response: `{ "access": "NEW_JWT_ACCESS_TOKEN" }`

- **Logout**: `POST /api/logout/`
  - Request body: `{ "refresh": "JWT_REFRESH_TOKEN" }`
  - Response: `{ "message": "Logged out successfully" }`

## Middleware

The `DynamicRouteGuardMiddleware` is used to protect API routes. It requires authentication for all routes starting with `/api/`, except for the excluded routes such as `/api/login/`, `/api/token/refresh/`, and `/api/logout/`.

## Debugging

Logging is configured to output debug information to the console. The `debug.log` file creation is disabled.

## Contributing

Feel free to submit issues or pull requests. Please ensure that your contributions adhere to the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
