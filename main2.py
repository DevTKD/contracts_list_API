from datetime import date
from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

app  = FastAPI()

class Contract:
    contract_id: str
    contract_name: str
    contract_type: str
    contract_status: Literal["active", "inactive"]
    contract_start_date: date
    contract_end_date: date

    def __init__(self, contract_id, contract_name, contract_type, contract_status, contract_start_date,
                 contract_end_date):
        self.contract_id = contract_id
        self.contract_name = contract_name
        self.contract_type = contract_type
        self.contract_status = contract_status
        self.contract_start_date = contract_start_date
        self.contract_end_date = contract_end_date

# ToDo: Update contract_id to an optional
class ContractRequest(BaseModel):
    contract_id: str
    contract_name: str = Field(min_length=3)
    contract_type: str = Field(min_length=3)
    contract_status: Literal["active", "inactive"]
    contract_start_date: date
    contract_end_date: date

# ToDo: fix dates in CONTRACTS
CONTRACTS = [
    Contract("CT001", "Bilateral NDA", "NDA", "Active", "01/20/2025", "01/19/2027"),
    Contract("CT002", "Master Services Agreement", "MSA", "Active", "06/18/2022", "06/17/2027"),
    Contract("CT003", "Vendor Agreement", "Vendor Service Agreement", "Inactive", "01/20/2025", "03/19/2026"),
    Contract("CT004", "Unilateral NDA", "NDA", "Active", "03/20/2025", "03/19/2027"),
    Contract("CT005", "Statement of Work", "SOW", "Active", "01/20/2025", "01/19/2027"),
    Contract("CT006", "Order Form", "OF", "Inactive", "08/18/2000", "08/17/2015")
]

@app.get("/contracts")
async def get_all_contracts():
    return CONTRACTS

# ToDo: add post endpoint and function around automatic numbering of the contract IDs