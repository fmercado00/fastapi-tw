
# Fast API
from fastapi import FastAPI, Body, Query, Path, status, Header, Form, File, UploadFile, Depends, HTTPException, Cookie

app = FastAPI()

@app.get(path="/", tags=["Service"])
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