from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Пустой список пользователей
users = []


# Модель User
class User(BaseModel):
    id: int
    username: str
    age: int


# GET запрос для получения всех пользователей
@app.get("/users")
async def get_users():
    return users


# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    if not username or not isinstance(username, str):
        raise HTTPException(status_code=400, detail="Имя пользователя должно быть строкой")
    if age < 0 or age > 120:
        raise HTTPException(status_code=400, detail="Возраст должен быть от 0 до 120")

    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# PUT запрос для обновления данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="User was not found")


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail="User was not found")
