# 🥤 Beverage Hub

A RESTful beverage management API built with **Python, Flask, Flask-SQLAlchemy, SQLAlchemy, and SQLite**.

Beverage Hub is a backend API that allows users to create, retrieve, and delete beverage records through HTTP requests. The project demonstrates the fundamentals of building a database-backed REST API using Flask and SQLAlchemy ORM.

---

## 🚀 Features

- Get all beverages
- Get a beverage by ID
- Add a single beverage
- Add multiple beverages in one request
- Delete a beverage
- JSON request and response handling
- SQLite database persistence
- SQLAlchemy ORM
- Pretty-formatted JSON responses
- HTTP status codes
- Automatic 404 handling
- API testing with Postman

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLAlchemy**
- **SQLite**
- **Postman**
- **Git**
- **GitHub**

---

## 📁 Project Structure

```text
beverage-hub/
│
├── application.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
└── instance/
    └── data.db
```

### File Description

| File / Directory | Description |
|---|---|
| `application.py` | Main Flask application containing the database model and API endpoints |
| `requirements.txt` | Python dependencies required by the project |
| `instance/data.db` | SQLite database containing beverage records |
| `README.md` | Project documentation |
| `LICENSE` | MIT License |
| `.gitignore` | Files and directories excluded from Git |

---

# 🗄️ Database

Beverage Hub uses **SQLite** as its database.

The database is configured using:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
```

**SQLAlchemy** is used as the ORM layer to interact with the SQLite database.

The application contains a `Drink` model that represents beverage records in the database.

---

## 🥤 Drink Model

```python
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
```

### Database Schema

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | Integer | Primary Key | Unique identifier for each beverage |
| `name` | String(100) | Not Null | Name of the beverage |
| `description` | String(255) | Optional | Description of the beverage |

### Example Records

| ID | Name | Description |
|---:|---|---|
| 1 | Grape Soda | Sweet grape-flavored soda |
| 2 | Cherry Cola | Cola with a cherry flavor |
| 3 | Pepsi | Classic cola soft drink |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sarvan-0/beverage-hub.git
```

## 2. Navigate to the Project

```bash
cd beverage-hub
```

## 3. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask development server:

```bash
python -m flask --app application:app run
```

The API will be available at:

```text
http://127.0.0.1:5000
```

You can also specify a custom port:

```bash
python -m flask --app application:app run --port 5000
```

---

# 📡 API Documentation

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Check whether the API is running |
| `GET` | `/drinks` | Retrieve all beverages |
| `GET` | `/drinks/<id>` | Retrieve a specific beverage |
| `POST` | `/drinks` | Create one or multiple beverages |
| `DELETE` | `/drinks/<id>` | Delete a beverage |

---

# 🏠 GET /

Checks whether the API is running.

### Request

```http
GET /
```

### Example

```text
http://127.0.0.1:5000/
```

### Response

```text
Hello, world!
```

---

# 📋 GET /drinks

Returns all beverages stored in the database.

### Request

```http
GET /drinks
```

### Example

```text
http://127.0.0.1:5000/drinks
```

### Response

```json
{
    "drinks": [
        {
            "id": 1,
            "name": "Grape Soda",
            "description": "Sweet grape-flavored soda"
        },
        {
            "id": 2,
            "name": "Cherry Cola",
            "description": "Cola with a cherry flavor"
        }
    ]
}
```

---

# 🔎 GET /drinks/<id>

Returns a single beverage using its ID.

### Request

```http
GET /drinks/1
```

### Example

```text
http://127.0.0.1:5000/drinks/1
```

### Response

```json
{
    "id": 1,
    "name": "Grape Soda",
    "description": "Sweet grape-flavored soda"
}
```

### Beverage Not Found

If the requested beverage does not exist:

```text
GET /drinks/999
```

The API returns:

```text
404 Not Found
```

This is handled using:

```python
Drink.query.get_or_404(id)
```

---

# ➕ POST /drinks

Creates a new beverage.

### Request

```http
POST /drinks
```

### Headers

```text
Content-Type: application/json
```

### Request Body

```json
{
    "name": "Pepsi",
    "description": "Classic cola soft drink"
}
```

### Response

```json
{
    "id": 3,
    "name": "Pepsi",
    "description": "Classic cola soft drink"
}
```

### Status Code

```text
201 Created
```

---

# ➕ POST /drinks - Multiple Beverages

The API also supports adding multiple beverages in a single request.

### Request

```http
POST /drinks
```

### Headers

```text
Content-Type: application/json
```

### Request Body

```json
[
    {
        "name": "Fanta",
        "description": "Orange-flavored soft drink"
    },
    {
        "name": "Sprite",
        "description": "Lemon-lime flavored soda"
    },
    {
        "name": "Mountain Dew",
        "description": "Citrus-flavored carbonated drink"
    }
]
```

### Response

```json
{
    "message": "Drinks added successfully",
    "drinks": [
        {
            "id": 4,
            "name": "Fanta",
            "description": "Orange-flavored soft drink"
        },
        {
            "id": 5,
            "name": "Sprite",
            "description": "Lemon-lime flavored soda"
        },
        {
            "id": 6,
            "name": "Mountain Dew",
            "description": "Citrus-flavored carbonated drink"
        }
    ]
}
```

### Status Code

```text
201 Created
```

---

# 🗑️ DELETE /drinks/<id>

Deletes a beverage from the database.

### Request

```http
DELETE /drinks/3
```

### Example

```text
http://127.0.0.1:5000/drinks/3
```

### Response

```json
{
    "message": "Drink deleted successfully"
}
```

### Status Code

```text
200 OK
```

If the beverage does not exist:

```text
404 Not Found
```

---

# 🔄 CRUD Operations

CRUD stands for:

- **C**reate
- **R**ead
- **U**pdate
- **D**elete

Beverage Hub currently implements:

### Create

```http
POST /drinks
```

Creates one or multiple beverages.

### Read

```http
GET /drinks
GET /drinks/<id>
```

Retrieves all beverages or a specific beverage.

### Update

Update functionality is **not implemented yet**.

Planned endpoints:

```http
PUT /drinks/<id>
PATCH /drinks/<id>
```

### Delete

```http
DELETE /drinks/<id>
```

Deletes a beverage from the database.

---

# 🧠 How It Works

The application follows a simple backend architecture:

```text
Client
   ↓
HTTP Request
   ↓
Flask Route
   ↓
SQLAlchemy ORM
   ↓
SQLite Database
   ↓
Database Result
   ↓
JSON Response
   ↓
Client
```

For example, when creating a beverage:

```text
POST /drinks
      ↓
JSON Request
      ↓
Flask
      ↓
Drink Object
      ↓
SQLAlchemy
      ↓
SQLite Database
      ↓
Database Commit
      ↓
JSON Response
```

---

# 🔍 Example: Creating a Beverage

A client sends:

```json
{
    "name": "Coca-Cola",
    "description": "Classic carbonated cola"
}
```

Flask receives the JSON data:

```python
data = request.get_json()
```

A new `Drink` object is created:

```python
drink = Drink(
    name=data['name'],
    description=data.get('description', '')
)
```

The object is added to the database session:

```python
db.session.add(drink)
```

The transaction is committed:

```python
db.session.commit()
```

The newly created beverage is then returned to the client as JSON.

---

# 🧪 Testing

The API was tested using **Postman**.

## Get All Beverages

```http
GET http://127.0.0.1:5000/drinks
```

## Get One Beverage

```http
GET http://127.0.0.1:5000/drinks/1
```

## Create One Beverage

```http
POST http://127.0.0.1:5000/drinks
```

Request body:

```json
{
    "name": "Coca-Cola",
    "description": "Classic carbonated cola"
}
```

## Create Multiple Beverages

```http
POST http://127.0.0.1:5000/drinks
```

Request body:

```json
[
    {
        "name": "Fanta",
        "description": "Orange-flavored soft drink"
    },
    {
        "name": "Sprite",
        "description": "Lemon-lime flavored soda"
    }
]
```

## Delete a Beverage

```http
DELETE http://127.0.0.1:5000/drinks/1
```

---

# 📊 HTTP Status Codes

| Status Code | Meaning | Usage |
|---:|---|---|
| `200` | OK | Successful GET or DELETE request |
| `201` | Created | Beverage successfully created |
| `404` | Not Found | Beverage does not exist |
| `405` | Method Not Allowed | HTTP method is not supported for the endpoint |

---

# 🔐 Error Handling

The API uses Flask-SQLAlchemy's `get_or_404()` method when retrieving individual beverages.

Example:

```python
drink = Drink.query.get_or_404(id)
```

If the beverage exists, the object is returned.

If the beverage does not exist, Flask automatically returns:

```text
404 Not Found
```

This prevents the application from attempting to operate on a nonexistent database record.

---

# 📦 Dependencies

The project uses:

```text
Flask
Flask-SQLAlchemy
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🚧 Current Limitations

Beverage Hub is currently a foundational REST API intended for learning and development.

The following features are not implemented yet:

- Authentication
- Authorization
- Input validation
- PUT/PATCH update endpoints
- Pagination
- Search and filtering
- Advanced error handling
- Database migrations
- PostgreSQL support
- Swagger/OpenAPI documentation
- Automated tests
- Production deployment

---

# 🔮 Future Improvements

Planned improvements include:

- [ ] Add PUT endpoint
- [ ] Add PATCH endpoint
- [ ] Add input validation
- [ ] Add improved error handling
- [ ] Add pagination
- [ ] Add search functionality
- [ ] Add filtering
- [ ] Add authentication
- [ ] Add authorization
- [ ] Add user accounts
- [ ] Add PostgreSQL support
- [ ] Add database migrations
- [ ] Add automated unit tests
- [ ] Add integration tests
- [ ] Add Swagger/OpenAPI documentation
- [ ] Deploy the API
- [ ] Build a frontend application

---

# 📚 What I Learned

This project helped me understand the fundamentals of backend API development, including:

- Flask application structure
- REST API fundamentals
- HTTP methods
- API routing
- Dynamic URL parameters
- JSON requests and responses
- SQLAlchemy ORM
- Flask-SQLAlchemy
- SQLite databases
- Database models
- CRUD operations
- Database sessions
- Application context
- HTTP status codes
- Error handling
- API testing with Postman
- Git and GitHub

---

# 🎯 Project Goal

The goal of Beverage Hub was to understand how a backend REST API works from end to end.

Instead of storing beverage data directly inside Python variables, the application persists the data in a database and exposes it through HTTP endpoints.

This project serves as a foundation for building more advanced backend applications.

---

# 📌 Future Architecture

The current architecture is:

```text
Client
   ↓
Flask
   ↓
SQLAlchemy
   ↓
SQLite
```

A future production-oriented version could use:

```text
Frontend
   ↓
REST API
   ↓
Flask
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

Additional components such as authentication, validation, testing, API documentation, and deployment can then be added.

---

# 👨‍💻 Author

**Sarvan**

GitHub:  
https://github.com/Sarvan-0

Repository:  
https://github.com/Sarvan-0/beverage-hub

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## ⭐ Project Status

**Current Status:** 🟢 Active Development

Beverage Hub currently provides the core functionality required for a basic database-backed REST API.

Future versions will focus on improving API design, validation, database architecture, testing, authentication, and deployment.
