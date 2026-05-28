# Contracts List API

FastAPI learning project for managing contracts, with active development tracked in `main2.py`.

---

## Current Progress (`main2.py`)

- Added a `Contract` class to represent contract records.
- Added a `ContractRequest` Pydantic model for request validation.
- Updated `contract_start_date` and `contract_end_date` to real `date` types.
- Added optional `contract_id` on create requests; ID is auto-assigned when missing.
- Added Pydantic `model_config` example payload with ISO date format.

---

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- Uvicorn

---

## Run `main2.py`

```bash
uvicorn main2:app --reload
```

API base URL: `http://127.0.0.1:8000`

Docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Active Endpoints in `main2.py`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contracts` | Return all contracts |
| GET | `/contracts/{contract_id}` | Return one contract by numeric ID |
| POST | `/create-contract` | Create a contract (auto-assign ID if not provided) |

---

## Request Model (`ContractRequest`)

```python
class ContractRequest(BaseModel):
    contract_id: Optional[int] = None
    contract_name: str
    contract_type: str
    contract_status: Literal["Active", "Inactive"]
    contract_start_date: date = Field(default_factory=date.today)
    contract_end_date: date
```

### Example create payload

```json
{
  "contract_name": "New contract name",
  "contract_type": "MSA",
  "contract_status": "Active",
  "contract_start_date": "2026-05-27",
  "contract_end_date": "2027-05-27"
}
```

Notes:
- Use ISO format for dates: `YYYY-MM-DD`.
- `contract_id` is optional for create requests.

---

## Known Gaps in `main2.py`

- `GET /contracts/{contract_id}` currently compares `contract.contract_id` to itself instead of the input parameter, so ID filtering needs a small fix.
- `create_contract` currently appends and does not return a response body yet.
- `find_contract_id` sets `contract.id` in the empty-list branch; it should set `contract.contract_id`.
- PUT/DELETE routes are not implemented in `main2.py` yet.
- No explicit 404 handling yet when a contract is not found.

---

## Project Structure

```text
contracts_list_API/
├── main.py
├── main2.py
├── DEVNOTES.md
├── test_main.http
├── .gitignore
└── README.md
```

