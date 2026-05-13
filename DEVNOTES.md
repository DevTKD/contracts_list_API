# 📘 Dev Log — Contracts API (FastAPI)

## Overview
This project is my first real API build using FastAPI.

Instead of following tutorial exercises, I apply each concept directly to this project.  
The goal is to **build something original while learning**.

The domain is **contracts**, based on 20+ years of experience as a contract manager.  
This allows me to work with meaningful, real-world data instead of placeholders.

---

## 🗓 Development Log

| Date | Focus | Details |
|------|------|--------|
| **Apr 27, 2026** | Project Setup | Defined project scope and learning approach. Chose contracts as the domain based on real-world experience (MSAs, NDAs, statuses like Active/Pending). |
| **Apr 28, 2026** | FastAPI Basics | Initialized app using `FastAPI()`. Ran server with Uvicorn (`--reload`). Confirmed auto-generated docs at `/docs` and `/redoc`. |
| **Apr 29, 2026** | Data Modeling | Implemented in-memory data using a Python list (`CONTRACTS`). Focused on routing and request handling instead of database setup. |
| **Apr 30, 2026** | Path Parameters | Built endpoint `/contracts/{contract_id}`. Implemented case-insensitive matching using `.casefold()`. Identified need for proper 404 handling. |
| **May 1, 2026** | Query Parameters | Combined path and query parameters (`contract_id` + `contract_type`). Maintained consistent list-based response structure. |
| **May 2, 2026** | POST Endpoint | Implemented `POST /contracts/create_contract` to add new contracts. Used `Body()` to accept request data and append it to the in-memory `CONTRACTS` list. Returned a confirmation response with `201 Created` status. |
| **May 6, 2026** | PUT Endpoint | Implemented `PUT /contracts/{contract_id}` to update an existing contract by ID. Added update logic to modify matching contract fields in the in-memory `CONTRACTS` list and return the updated contract. |
| **May 6, 2026** | DELETE Endpoint | Implemented `DELETE /contracts/delete_contract/{contract_id}` to remove a contract by ID. Added case-insensitive ID matching and delete logic with `pop()` once a match is found. |
| **May 12, 2026** | Contract Class | Built `Contract` class in `main2.py` with all required attributes (`contract_id`, `contract_name`, `contract_type`, `contract_status`, `contract_start_date`, `contract_end_date`). Initialized `CONTRACTS` list with actual class instances instead of raw dictionaries. |
| **May 12, 2026** | Pydantic Models | Starting implementation of Pydantic models for data validation. Planning to replace raw dictionaries and add type validation for request/response bodies. |

---

## ⚙️ Current Implementation

- FastAPI application running with Uvicorn
- In-memory contract dataset (`CONTRACTS`)
- Endpoints:
  - `GET /contracts`
  - `GET /contracts/{contract_id}`
  - `GET /contracts/{contract_id}?contract_type=...`
  - `POST /contracts/create_contract` — Create a new contract
  - `PUT /contracts/update_contract` — Update an existing contract by ID (ID provided in request body)
  - `DELETE /contracts/delete_contract/{contract_id}` — Delete a contract by ID
- Case-insensitive ID matching
- Auto-generated API documentation:
  - Swagger UI (`/docs`)
  - ReDoc (`/redoc`)

---

## ⚠️ Known Limitations

- No database (data resets on server restart)
- Missing error handling (e.g., 404 responses)
- Data validation in progress (Pydantic models being implemented)
- No authentication

---

## 🚧 Next Steps

- Introduce Pydantic models for validation (in progress)
- Add proper HTTP error handling (404, etc.)
- Integrate a database for persistence
- Add basic authentication