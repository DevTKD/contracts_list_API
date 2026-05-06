# Contracts List API

A simple REST API built with **FastAPI** that manages and returns a list of contracts.

---

## 🚀 Features

- Retrieve a full list of contracts
- Retrieve a single contract by ID
- Filter contracts by ID and contract type
- Create a new contract
- Update an existing contract
- Each contract includes ID, name, type, status, and start/end dates
- Built with FastAPI for fast, modern Python API development

---

## 🛠️ Tech Stack

- **Python 3.12**
- **FastAPI**
- **Uvicorn** (ASGI server)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DevTKD/contracts_list_API.git
   cd contracts_list_API
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## 📋 API Endpoints

| Method | Endpoint                                        | Description                                  |
|--------|-------------------------------------------------|----------------------------------------------|
| GET    | `/contracts`                                    | Returns all contracts                        |
| GET    | `/contracts/{contract_id}`                      | Returns a single contract by ID              |
| GET    | `/contracts/{contract_id}/?contract_type=<type>` | Returns contracts matching ID and type     |
| POST   | `/contracts/create_contract`                    | Creates a new contract                       |
| PUT    | `/contracts/update_contract`                    | Updates an existing contract by ID in body   |
| GET    | `/docs`                                         | Interactive Swagger UI                       |
| GET    | `/redoc`                                        | ReDoc API documentation                      |

---

## 📄 Sample Responses

**GET** `/contracts`

```json
[
  {
    "id": "CT001",
    "contract_name": "Contract 001",
    "contract_type": "Master Services Agreement",
    "contract_status": "Active",
    "contract_start_date": "January 1, 2023",
    "contract_end_date": "December 31, 2026"
  }
]
```

**GET** `/contracts/{contract_id}`

Request: `/contracts/CT001`

```json
{
  "id": "CT001",
  "contract_name": "Contract 001",
  "contract_type": "Master Services Agreement",
  "contract_status": "Active",
  "contract_start_date": "January 1, 2023",
  "contract_end_date": "December 31, 2026"
}
```

**GET** `/contracts/{contract_id}/?contract_type=<type>`

Request: `/contracts/CT003/?contract_type=Partnership Agreement`

```json
[
  {
    "id": "CT003",
    "contract_name": "Contract 003",
    "contract_type": "Partnership Agreement",
    "contract_status": "Active",
    "contract_start_date": "January 1, 2025",
    "contract_end_date": "December 31, 2027"
  }
]
```

**POST** `/contracts/create_contract`

Request body:

```json
{
  "id": "CT007",
  "contract_name": "Contract 007",
  "contract_type": "Vendor Agreement",
  "contract_status": "Pending",
  "contract_start_date": "January 1, 2029",
  "contract_end_date": "December 31, 2031"
}
```

**PUT** `/contracts/update_contract`

Request body:

```json
{
  "id": "CT002",
  "contract_name": "Contract 002",
  "contract_type": "Consulting Agreement",
  "contract_status": "Active",
  "contract_start_date": "January 1, 2024",
  "contract_end_date": "December 31, 2025"
}
```

> **Note:** ID matching is case-insensitive in lookup/update comparisons (for example, `ct001` and `CT001` both match).

---

## 📁 Project Structure

```
contracts_list_API/
├── main.py           # Main FastAPI application
├── test_main.http    # HTTP request test file
├── DEVNOTES.md       # Development log and learning notes
├── .gitignore        # Git ignore rules
└── README.md         # Project documentation
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
