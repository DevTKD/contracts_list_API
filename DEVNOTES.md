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

---

## ⚙️ Current Implementation

- FastAPI application running with Uvicorn
- In-memory contract dataset (`CONTRACTS`)
- Endpoints:
  - `GET /contracts`
  - `GET /contracts/{contract_id}`
  - `GET /contracts/{contract_id}?contract_type=...`
  - `POST /contracts/create_contract` — Create a new contract
  - `PUT /contracts/{contract_id}` — Update an existing contract by ID
- Case-insensitive ID matching
- Auto-generated API documentation:
  - Swagger UI (`/docs`)
  - ReDoc (`/redoc`)

---

## ⚠️ Known Limitations

- No database (data resets on server restart)
- Missing error handling (e.g., 404 responses)
- No data validation (raw dictionaries instead of models)
- No DELETE endpoint yet
- No authentication

---

## 🚧 Next Steps

- Add proper HTTP error handling (404, etc.)
- Introduce Pydantic models for validation
- Integrate a database for persistence
- Implement POST (completed), PUT (completed), DELETE (pending)
- Add basic authentication