
# Fast API
from fastapi import FastAPI, Body, Query, Path, status, Header, Form, File, UploadFile, Depends, HTTPException, Cookie

app = FastAPI()

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