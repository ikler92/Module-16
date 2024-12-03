from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# 1. Главная страница
@app.get("/")
def read_main():
    return "Главная страница"


# 2. Страница администратора
@app.get("/user/admin")
def read_admin():
    return "Вы вошли как администратор"


# 3. Страница пользователя с валидацией user_id
@app.get("/user/{user_id}")
def read_user_by_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]):
    return f"Вы вошли как пользователь № {user_id}"


# 4. Страница пользователя с параметрами username и age с валидацией
@app.get("/user/{username}/{age}")
def read_user_info(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    return f"Информация о пользователе. Имя: '{username}', Возраст: {age}."
