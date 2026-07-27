# Electronics Store CRUD API

A simple **CRUD (Create, Read, Update, Delete)** REST API built using **FastAPI**, **SQLAlchemy**, **MySQL**, and **Pydantic**. This project manages electronic products such as mobiles, laptops, TVs, air conditioners, and washing machines.

---

# Project Structure

```text
electronics-store/
│
├── main.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── README.md
└── venv/
```

---

# File Description

## 1. `database.py`

### Purpose

This file is responsible for establishing the connection between FastAPI and the MySQL database.

### Responsibilities

- Creates the MySQL database engine.
- Creates database sessions.
- Defines the SQLAlchemy Base class.


---

## 2. `models.py`

### Purpose

Defines the database table structure using SQLAlchemy ORM.

### Responsibilities

- Maps the Python `Electronics` class to the `electronics` table.
- Defines all database columns.

### Table Columns

- `id`
- `name`
- `category`
- `brand`
- `price`
- `stock`

---

## 3. `schemas.py`

### Purpose

Defines Pydantic schemas for request validation and response formatting.

### Responsibilities

- Validates incoming request data.
- Structures outgoing response data.
- Converts SQLAlchemy objects into JSON responses.

### Schemas

### `ElectronicsCreate`

Used when creating or updating an electronic product.


### `ElectronicsResponse`

Used while returning data to the client.

Includes:

- Product ID
- ORM support using


---

## 4. `crud.py`

### Purpose

Contains all database operations.

Implements complete CRUD functionality.

### Functions

- `create_electronics()`
- `get_all_electronics()`
- `get_electronics()`
- `get_by_category()`
- `update_electronics()`
- `delete_electronics()`

### SQLAlchemy Methods Used

- `add()`
- `commit()`
- `refresh()`
- `query()`
- `filter()`
- `first()`
- `all()`
- `delete()`

---

## 5. `main.py`

### Purpose

Creates the FastAPI application and exposes REST API endpoints.

### Responsibilities

- Creates the FastAPI app.
- Handles HTTP requests.
- Performs request validation.
- Calls CRUD functions.
- Returns API responses.
- Handles exceptions.

### API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| POST | `/electronics` | Create a product |
| GET | `/electronics` | Get all products |
| GET | `/electronics/{electronics_id}` | Get product by ID |
| GET | `/electronics/category/{category}` | Get products by category |
| PUT | `/electronics/{electronics_id}` | Update a product |
| DELETE | `/electronics/{electronics_id}` | Delete a product |

---

# Project Workflow

```text
Postman / Browser
        │
        ▼
     main.py
        │
        ▼
   schemas.py
(Request Validation)
        │
        ▼
      crud.py
(Database Operations)
        │
        ▼
     models.py
(SQLAlchemy ORM)
        │
        ▼
   database.py
(Database Connection)
        │
        ▼
      MySQL
        │
        ▼
     JSON Response
```

---

# Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn

---



# Features

- Create electronic products
- Retrieve all products
- Retrieve a product by ID
- Retrieve products by category
- Update product information
- Delete products
- Automatic request validation
- Automatic interactive API documentation
- MySQL database integration using SQLAlchemy ORM

---

# Author

**Hemanth Tavva**

---

# Learning Outcomes

This project demonstrates:

- FastAPI fundamentals
- REST API development
- CRUD operations
- SQLAlchemy ORM
- Pydantic validation
- Dependency Injection
- Database session management
- MySQL integration
- API testing with Postman and Swagger