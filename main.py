from fastapi import FastAPI
app = FastAPI()
# Establish contracts list 
CONTRACTS= [
                {"id": "CT001",
                 "contract_name": "Contract 001",
                 "contract_type": "Master Services Agreement",
                 "contract_status": "Active",
                 "contract_start_date": "January 1, 2023",
                 "contract_end_date": "December 31, 2026"
                 },
    {
        "id": "CT002",
        "contract_name": "Contract 002",
        "contract_type": "Consulting Agreement",
        "contract_status": "Pending",
        "contract_start_date": "January 1, 2024",
        "contract_end_date": "December 31, 2024"
    },
    {
        "id": "CT003",
        "contract_name": "Contract 003",
        "contract_type": "Partnership Agreement",
        "contract_status": "Active",
        "contract_start_date": "January 1, 2025",
        "contract_end_date": "December 31, 2027"
    },
    {
        "id": "CT004",
        "contract_name": "Contract 004",
        "contract_type": "Subcontract Agreement",
        "contract_status": "Active",
        "contract_start_date": "January 1, 2026",
        "contract_end_date": "December 31, 2028"
    },
    {
        "id": "CT005",
        "contract_name": "Contract 005",
        "contract_type": "Bilateral NDA",
        "contract_status": "Active",
        "contract_start_date": "January 1, 2027",
        "contract_end_date": "December 31, 2030"
    },
    {
        "id": "CT006",
        "contract_name": "Contract 006",
        "contract_type": "Unilateral NDA",
        "contract_status": "Active",
        "contract_start_date": "January 1, 2028",
        "contract_end_date": "December 31, 2032"
    }
]

@app.get("/contracts")
async def contracts_list():
    return CONTRACTS

#adding a dynamic parameter
@app.get("/contracts/{contract_id}")
async def contracts_detail(contract_id: str):
    for contract in CONTRACTS:
        if contract.get("id").casefold() == contract_id.casefold():
            return contract
