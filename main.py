from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["user_management"]
users_collection = db["users"]

# User model
class User(BaseModel):
    name: str
    email: str
    age: int
    address: Optional[str] = None

class UserInDB(User):
    id: str

@app.post("/users/", response_model=UserInDB)  # Corrected here
async def create_user(user: User):
    user_dict = user.dict()
    result = users_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

@app.get("/users/{user_id}", response_model=UserInDB)
async def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User  not found")
    user["id"] = str(user["_id"])
    return user

@app.get("/users/", response_model=List[UserInDB])
async def list_users():
    users = []
    for user in users_collection.find():
        user["id"] = str(user["_id"])
        users.append(user)
    return users

@app.put("/users/{user_id}", response_model=UserInDB)
async def update_user(user_id: str, user: User):
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User  not found")
    user_dict = user.dict()
    user_dict["id"] = user_id
    return user_dict

@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User  not found")
    return {"detail": "User  deleted successfully"}