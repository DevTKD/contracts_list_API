from datetime import date
from typing import Literal, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app  = FastAPI()

class Contract:
    contract_id: int
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


class ContractRequest(BaseModel):
    contract_id: Optional[int] = Field(description = "ID is not needed on create", default = None)
    contract_name: str = Field(min_length=3)
    contract_type: str = Field(min_length=3)
    contract_status: Literal["Active", "Inactive"]
    contract_start_date: date = Field(default_factory=date.today)
    contract_end_date: date

    model_config = {
        "json_schema_extra":{
            "example": {
                "contract_name" : "New contract name",
                "contract_type" : "MSA",
                "contract_status" : "Active",
                "contract_start_date" : "2026-05-27",
                "contract_end_date" : "2027-05-27"
            }
        }
    }

CONTRACTS = [
    Contract(1, "Bilateral NDA", "NDA", "Active", date(2025, 1, 20), date(2027, 1, 19)),
    Contract(2, "Master Services Agreement", "MSA", "Active", date(2022, 6, 18), date(2027, 6, 17)),
    Contract(3, "Vendor Agreement", "Vendor Service Agreement", "Inactive", date(2025, 1, 20), date(2026, 3, 19)),
    Contract(4, "Unilateral NDA", "NDA", "Active", date(2025, 3, 20), date(2027, 3, 19)),
    Contract(5, "Statement of Work", "SOW", "Active", date(2025, 1, 20), date(2027, 1, 19)),
    Contract(6, "Order Form", "OF", "Inactive", date(2000, 8, 18), date(2015, 8, 17))
]

@app.get("/contracts")
async def get_all_contracts():
    return CONTRACTS

@app.get("/contracts/{contract_id}")
async def retrieve_contract(contract_id: int):
    for contract in CONTRACTS:
        if contract.contract_id == contract_id:
            return contract
    return None

@app.get("/contracts/")
async def retrieve_contract_by_status(contract_status: str):
    contracts_to_return = []
    for contract in CONTRACTS:
        if contract.contract_status.casefold() == contract_status.casefold():
            contracts_to_return.append(contract)
    return contracts_to_return

@app.post("/create-contract")
async def create_contract(contract_request: ContractRequest):
    new_contract = Contract(**contract_request.model_dump())
    CONTRACTS.append(find_contract_id(new_contract))
    
def find_contract_id(contract: Contract):
    if len(CONTRACTS) > 0:
        contract.contract_id = CONTRACTS[-1].contract_id + 1
    else:
        contract.id = 1
    return contract
