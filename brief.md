# Project Brief: Asset Request Management System

## Objective

Build a backend-only Asset Request Management System using:

- Python
- Poetry
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL

The application should be developed as a **monolithic application** following a **layered architecture**:

```text
Routes/API Layer
    ↓
Service Layer
    ↓
Repository/Data Access Layer
    ↓
Database
```

Recommended project structure:

```text
app/
├── api/
│   └── routes/
├── services/
├── repositories/
├── models/
├── schemas/
├── db/
├── core/
└── main.py

alembic/
tests/
```

---

# Roles

## Employee

Can:

- Login
- View available asset types
- Create asset requests
- View own requests
- Cancel pending requests

## Admin

Can:

- Login
- Create asset types
- Update asset types
- Deactivate asset types
- View all asset requests
- Approve requests
- Reject requests

---

# Database Tables

## users

| Column | Type |
|----------|----------|
| id | Integer |
| name | String |
| email | String (Unique) |
| password_hash | String |
| role | Enum (employee/admin) |
| is_active | Boolean |
| created_at | DateTime |

---

## asset_types

| Column | Type |
|----------|----------|
| id | Integer |
| name | String |
| description | Text |
| is_active | Boolean |
| created_at | DateTime |

Examples:

```text
Laptop
Monitor
Keyboard
Software License
ID Card
```

---

## asset_requests

| Column | Type |
|----------|----------|
| id | Integer |
| user_id | Foreign Key → users.id |
| asset_type_id | Foreign Key → asset_types.id |
| reason | Text |
| status | Enum |
| admin_comment | Text (Nullable) |
| created_at | DateTime |
| updated_at | DateTime |

Possible statuses:

```text
pending
approved
rejected
cancelled
```

---

# API Endpoints

## Authentication

### Login

```http
POST /auth/login
```

Request:

```json
{
  "email": "employee@company.com",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

---

# Asset Type APIs

(Admin Only)

### Create Asset Type

```http
POST /asset-types
```

### List Asset Types

```http
GET /asset-types
```

### Update Asset Type

```http
PATCH /asset-types/{asset_type_id}
```

### Deactivate Asset Type

```http
DELETE /asset-types/{asset_type_id}
```

---

# Employee Request APIs

### Create Request

```http
POST /requests
```

Request:

```json
{
  "asset_type_id": 1,
  "reason": "Required for project development"
}
```

---

### View My Requests

```http
GET /requests/me
```

---

### View Request Details

```http
GET /requests/{request_id}
```

---

### Cancel Request

```http
PATCH /requests/{request_id}/cancel
```

Only pending requests can be cancelled.

---

# Admin Request APIs

### View All Requests

```http
GET /admin/requests
```

Optional filters:

```text
status=pending
status=approved
status=rejected
```

---

### Approve Request

```http
PATCH /admin/requests/{request_id}/approve
```

Request:

```json
{
  "admin_comment": "Approved"
}
```

---

### Reject Request

```http
PATCH /admin/requests/{request_id}/reject
```

Request:

```json
{
  "admin_comment": "Insufficient justification"
}
```

---

# JWT Authentication

## JWT Payload

For this project, JWT tokens will not expire.

Example payload:

```json
{
  "sub": "1",
  "role": "employee"
}
```

---

## Login Flow

```text
1. User sends email and password
2. Backend validates credentials
3. Backend generates JWT
4. JWT is returned to client
5. Client stores token
6. Client sends token with every protected request
```

---

## Using JWT as a Bearer Token

Request:

```http
GET /requests/me

Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

## FastAPI Example

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    user_id = payload