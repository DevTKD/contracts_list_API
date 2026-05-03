April 27th, 2026: Project start
Decision: what this project is and why
This is my first real API project, built alongside a FastAPI Udemy course. The approach: learn a concept in the course, then apply it here immediately instead of just doing the tutorial exercises. That way the project is mine, not the instructor's.

Chose contracts as the domain because I have 20+ years of real-world experience with them as a contract manager. I 
know what a Master Services Agreement is, what an NDA looks like, what "Active" vs "Pending" means in practice That 
domain knowledge means I'm not just moving data around, I actually understand what the data represents.


April 28th,2026
Learned: how FastAPI apps are initialized
The entry point is simple â€” app = FastAPI() creates the application instance. Uvicorn is the server that actually runs it. The --reload flag during development means the server restarts automatically when I save changes, which is really useful.

The API is available at http://127.0.0.1:8000 by default. FastAPI also auto-generates interactive docs at /docs 
(Swagger UI) and /redoc.  I didn't have to build those, they just appear. That felt like magic the first time.

#fastapi #basicsuvicorn

April 29th,2026
Decision: in-memory list as data source
The contracts data is stored as a plain Python list of dictionaries at the top of main.py, called CONTRACTS. No database yet. This is intentional â€” the focus right now is learning routing and request handling, not database setup.

The all-caps naming (CONTRACTS) signals that it's a module-level constant, which is a Python convention. Worth 
noting this won't persist changes, if I eventually add POST/PUT/DELETE endpoints, any changes disappear when the 
server restarts. That's a known limitation I'll address when I get to databases.

The contract types I used are real: MSA, Consulting Agreement, Partnership Agreement, Subcontract, Bilateral NDA, Unilateral NDA. That's from domain knowledge, not made up.

#data modeling # decisionfuture: database

April 30th,2026
Learned: path parameters
Added a /contracts/{contract_id} endpoint. The curly braces in the route tell FastAPI this is a dynamic segment â€” whatever the user puts there gets passed into the function as contract_id.

To find the matching contract I loop through the list and compare IDs. Made the comparison case-insensitive using .casefold() on both sides â€” so ct001 and CT001 both work. I chose .casefold() over .lower() because I learned it handles edge cases in non-English characters better, even though it probably won't matter for contract IDs.

Open question: right now if the contract_id doesn't exist, the function returns None and FastAPI sends back a 200 with no body. That's wrong â€” it should return a 404. Need to learn how to handle that properly.
path parametersroutingopen question

May 1st,2026
Learned: combining path and query parameters
Added a third endpoint that takes both a path parameter (contract_id) and a query parameter (contract_type). The path parameter is part of the URL itself. The query parameter comes after a ? â€” like /contracts/CT001/?contract_type=Bilateral NDA.

FastAPI figures out which is which automatically based on whether the parameter name appears in the route path or 
not. I didn't have to do anything special to declare it as a query param,  just adding it to the function signature 
was enough.

This endpoint returns a list even though it'll usually only match one contract. That's intentional â€” keeps it consistent with the main list endpoint.

Next steps I'm aware of:
Things I know I'm missing and plan to add as I learn them: proper 404 error handling when a contract isn't found, Pydantic models for data validation instead of raw dicts, a real database instead of the in-memory list, POST/PUT/DELETE endpoints to actually manage contracts, and eventually authentication.

