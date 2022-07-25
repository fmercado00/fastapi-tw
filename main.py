from typing import Optional, List
from models.base.users_base_model import UserBase
from models.response.user_response_model import UserResponseModel

# Fast API
from fastapi import FastAPI, Body, Query, Path, status, Header, Form, File, UploadFile, Depends, HTTPException, Cookie


app = FastAPI()

# Path Operations

@app.get(path="/"
, tags=["Ping"]
, summary="Ping Service to discover if the service is on-line"
,  status_code=status.HTTP_200_OK
)
def home():
    """
    # Default endpoint for the service

    ## This path operation responses when the service is up and healthy.

    ### Parameters:

    - None

    ### Returns:
    Messarge: "TW Application is alive!"
    """
    return {"message": "TW Application is alive!"}

## Users

@app.post(
    path="/v1/users/login",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_CREATED,
    summary = "Login a registered user",
    tags=["Users"]
)
def login():
    pass

@app.post(
    path="/v1/users/signup",
    response_model=UserResponseModel,
    status_code=status.HTTP_201_CREATED,
    summary = "Register a new user",
    tags=["Users"]
)
def signup():
    pass

@app.get(
    path="/v1/users",
    response_model=List[UserResponseModel],
    status_code=status.HTTP_200_OK,
    summary = "List all users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_OK,
    summary = "Get a specific user",
    tags=["Users"]
)
def show_user():
    pass

@app.delete(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_OK,
    summary = "Register a new user",
    tags=["Users"]
)
def delete_user():
    pass

@app.put(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_201_CREATED,
    summary = "Register a new user",
    tags=["Users"]
)
def delete_user():
    pass

## Tweets