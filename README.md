# FastAPI E-commerce Backend - TicaretApp

A simple e-commerce backend application built with FastAPI and SQLite. This project serves as a practice and a template for creating a modern, asynchronous web API in Python.

## Features

- **User Management**: Create and manage users.
- **Product Management**: CRUD (Create, Read, Update, Delete) operations for products.
- **FastAPI**: Modern, fast (high-performance) web framework.
- **SQLAlchemy**: Python SQL toolkit and Object Relational Mapper (ORM).
- **Pydantic**: Data validation and settings management.
- **SQLite**: Server-less, self-contained database.
- **Interactive API Docs**: Automatic documentation via Swagger UI and ReDoc.

```
TicaretApp/
├── ticaretapp/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```


## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

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

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  Start the FastAPI server from the project's root directory:
    ```sh
    uvicorn ticaretapp.main:app --reload
    ```

2.  The application will be running on `http://127.0.0.1:8000`.

## API Usage

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

You can use this interface to test all the available endpoints, such as creating users and adding products.

### Completed
- [x] Implement user authentication (OAuth2 with JWT tokens).
- [x] Add endpoints for updating and deleting products.
- [x] Implement ownership verification for product modification.

### Next Steps
- [ ] Add CRUD operations for Users (update, delete).
- [ ] Add more models (e.g., Orders, Cart).
- [ ] Write unit and integration tests.
- [ ] Implement pagination for all list endpoints.
