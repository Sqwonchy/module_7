from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_users(username, age) -> str:
    user_id = str(int(max(users,key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"user {user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id, username, age) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def deleted_users(user_id):
    users.pop(user_id)
    return f"user {user_id} has been deleted"