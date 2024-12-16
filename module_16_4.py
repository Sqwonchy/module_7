from fastapi import FastAPI, Path, HTTPException
from typing import List, Annotated
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

def find_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    return None

@app.get("/users")
async def get_all_users() -> List[User]:
    return users



@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=5,max_length=20, description= 'Enter username', example='UrbanUser' )],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age',example=24)]) -> User:
    user_id = users[-1].id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(ge=0,le=999, description='Enter your id',example=1) ],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    user = find_user(user_id)
    if user:
        user.username = username
        user.age = age
        return user
    else:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=0,le=999, description='Enter your id',example=1) ]):
    user = find_user(user_id)
    if user:
        users.remove(user)
        return {"detail": f"User {user_id} has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

