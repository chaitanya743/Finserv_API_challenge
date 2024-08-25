# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Union
# import re
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins for testing
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods
#     allow_headers=["*"],  # Allow all headers
# )

# # Mount the static directory to serve HTML, CSS, and JS files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Define the request body model
# class DataModel(BaseModel):
#     data: List[Union[str, int]]

# @app.post("/bfhl")
# async def process_data(request_body: DataModel):
#     # User details (hardcoded for simplicity)
#     user_id = "naga_chaitanya_07042003"
#     email = "anandanaga.21bce9321@vitapstudent.ac.in"
#     roll_number = "21BCE9321"

#     # Extract data from the request
#     data = request_body.data
#     numbers = [str(item) for item in data if isinstance(item, int) or re.match(r'^\d+$', str(item))]
#     alphabets = [str(item) for item in data if isinstance(item, str) and item.isalpha()]
#     highest_lowercase_alphabet = [max([c for c in alphabets if c.islower()], default='')]

#     return {
#         "is_success": True,
#         "user_id": user_id,
#         "email": email,
#         "roll_number": roll_number,
#         "numbers": numbers,
#         "alphabets": alphabets,
#         "highest_lowercase_alphabet": highest_lowercase_alphabet if highest_lowercase_alphabet[0] else []
#     }

# @app.get("/bfhl")
# async def get_operation_code():
#     return {"operation_code": 1}


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Mount the static directory to serve HTML, CSS, and JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the request body model
class DataModel(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def process_data(request_body: DataModel):
    # User details (hardcoded for simplicity)
    user_id = "naga_chaitanya_07042003"
    email = "anandanaga.21bce9321@vitapstudent.ac.in"
    roll_number = "21BCE9321"

    # Extract data from the request
    data = request_body.data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase_alphabet = [max((c for c in alphabets if c.islower()), default='')]

    return {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
