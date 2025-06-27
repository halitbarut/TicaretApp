# TicaretApp: A Full-Stack E-commerce Application

A full-stack e-commerce application built with a **FastAPI** backend and a server-rendered **Jinja2** frontend. This project demonstrates how to build a complete, interactive web application with a modern Python backend, handling everything from user authentication to shopping cart management.

## Features

- **FastAPI Backend**: A high-performance, asynchronous API serving all business logic.
- **Jinja2 Frontend**: A server-rendered user interface for browsing products, managing a cart, and user authentication.
- **Full User Authentication**: Secure user registration and login using OAuth2 Password Flow and JWT tokens.
- **Complete Product Management**: API endpoints for creating, reading, filtering, updating, and deleting products.
- **Interactive Shopping Cart**: A persistent shopping cart for authenticated users.
- **Clean Architecture**: A modular structure separating API routers, database logic (CRUD), and frontend templates.
- **SQLAlchemy ORM**: Robust database interaction with a SQLite backend.
- **Pydantic**: Data validation for both API requests and application settings.

## Project Structure

The project follows a hybrid structure where FastAPI serves both the API and the HTML templates.

```
TicaretApp/
├── .env.example # Environment variable template
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── ticaretapp/
├── init.py
├── routers/
│ ├── init.py
│ ├── cart.py
│ ├── products.py
│ └── users.py
├── static/
│ ├── pages/
│ │ ├── cart.js
│ │ ├── login.js
│ │ ├── products.js
│ │ └── register.js
│ ├── auth.js
│ ├── main.js
│ └── style.css
└── templates/
├── cart.html
├── index.html
├── layout.html
├── login.html
└── register.html
├── config.py
├── crud.py
├── database.py
├── dependencies.py
├── main.py
├── models.py
├── schemas.py
└── security.py
```


## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/halitbarut/TicaretApp.git
    cd TicaretApp
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Configure environment variables:**
    Create a `.env` file by copying the template.
    ```sh
    cp .env.example .env
    ```
    *You can generate a new `SECRET_KEY` by running `openssl rand -hex 32` in your terminal and pasting it into the `.env` file.*

4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  Start the FastAPI server from the project's root directory:
    ```sh
    uvicorn ticaretapp.main:app --reload
    ```

2.  The application will now be running. Open your web browser and navigate to:
    **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## Application & API Usage

### Web Interface
The main user interface is available at the root URL (`/`). From here, you can browse products, register a new account, log in, and manage your shopping cart.

### API Documentation
The backend API is available under the `/api` prefix. You can access the interactive API documentation (Swagger UI) to test the endpoints directly:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Project Status & Roadmap

### Completed Features
- [x] Full user authentication flow (Register, Login, JWT).
- [x] RESTful API for Product management (CRUD).
- [x] Ownership verification for modifying products.
- [x] Server-rendered frontend using Jinja2 templates.
- [x] Dynamic shopping cart system for users.

### Next Steps
- [ ] Implement Order placement system from the cart.
- [ ] Add advanced user management (update profile, change password).
- [ ] Implement database migrations with **Alembic**.
- [ ] Write unit and integration tests with **Pytest**.
- [ ] Add advanced product filtering and pagination to the API and UI.