from typing import Optional, List
from models.base.tweet import Tweet
from models.base.users_base_model import UserBase
from models.request.users_request_model import UserRequestModel
from models.response.user_response_model import UserResponseModel
import json


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
    status_code=status.HTTP_201_CREATED,
    summary = "Login a registered user",
    tags=["Users"]
)
async def login():
    pass

@app.post(
    path="/v1/users/signup",
    response_model=UserResponseModel,
    status_code=status.HTTP_201_CREATED,
    summary = "Register a new user",
    tags=["Users"]
)
async def signup(user: UserRequestModel = Body(...)):
    """
    # Signup

    ## This path operation register a user in the app.

    ### Parameters:

    - user: UserRequestModel

    ### Returns:
    User: UserResponseModel. Return response model without password.
    """
    user_dict = user.dict()
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results, indent=4))
    userResponse = UserResponseModel(**user_dict)
    return userResponse


@app.get(
    path="/v1/users",
    response_model=List[UserResponseModel],
    status_code=status.HTTP_200_OK,
    summary = "List all users",
    tags=["Users"]
)
async def show_all_users():
    """
    # Show all users

    ## This path operation gets all user in the app.

    ### Parameters:

    - None

    ### Returns:
    List: UserResponseModel. Shows all users with the response model.
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return [UserResponseModel(**user) for user in results]

@app.get(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_OK,
    summary = "Get a specific user",
    tags=["Users"]
)
async def show_user():
    pass

@app.delete(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_OK,
    summary = "Delete a user",
    tags=["Users"]
)
async def delete_user():
    pass

@app.put(
    path="/v1/users/{user_id}",
    response_model=UserResponseModel,
    status_code=status.HTTP_200_OK,
    summary = "Update a user",
    tags=["Users"]
)
async def delete_user():
    pass

## Tweets

@app.get(
    path="/v1/tweets",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary = "List all tweets",
    tags=["Tweets"]
)
async def show_all_tweets():
    """
    # Show all tweets

    ## This path operation gets all tweets in the app.

    ### Parameters:

    - None

    ### Returns:
    List: Tweet. Shows all tweets using base model.
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        return json.loads(f.read())


@app.get(
    path="/v1/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary = "List all tweets",
    tags=["Tweets"]
)
async def show_a_tweet():
    """
    # Show a tweet 

    ## This path operation gets a tweet by id.

    ### Parameters:

    - tweet_id: str. The id of the tweet.

    ### Returns:
    Twwet: Tweet. Shows a tweet using base model.
    """
    pass

@app.post(
    path="/v1/tweets",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary = "Post a tweet",
    tags=["Tweets"]
)
async def post_tweet(tweet: Tweet = Body(...)):
    """
    # Post a tweet

    ## This path operation post a tweet in the app.

    ### Parameters:

    - tweet: Tweet. The tweet to be posted.

    ### Returns:
    status: Status. Json thtat shows if the post was successful or not.
    """

    tweet_dict = tweet.dict()
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results, indent=4))
    return tweet

   

@app.delete(
    path="/v1/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary = "Delete a tweet",
    tags=["Tweets"]
)
async def delete_tweet():
    """
    # Delete a tweet

    ## This path operation delete a tweet in the app.

    ### Parameters:

    - tweet_id: str. The id of the tweet.

    ### Returns:
    Status: Status. Shows if the tweet was successfully deleted or not.
    """
    pass

@app.put(
    path="/v1/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary = "Update a tweet",
    tags=["Tweets"]
)
async def update_tweet():
    """
    # Update a tweet

    ## This path operation update a tweet in the app.

    ### Parameters:

    - tweet_id: str. The id of the tweet.

    ### Returns:
    Status: Status. Shows if the tweet was successfully updated or not.
    """
    pass