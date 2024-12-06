from fastapi import FastAPI, HTTPException

app = FastAPI()

# Начальный словарь пользователей
users = {"1": "Имя: Example, возраст: 18"}


# GET запрос на получение всех пользователей
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

    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


# PUT запрос для обновления данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    if not username or not isinstance(username, str):
        raise HTTPException(status_code=400, detail="Имя пользователя должно быть строкой")
    if age < 0 or age > 120:
        raise HTTPException(status_code=400, detail="Возраст должен быть от 0 до 120")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return f"User {user_id} has been deleted"
