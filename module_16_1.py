from fastapi import FastAPI, Query

# Создание приложения FastAPI
app = FastAPI()


# Маршрут для главной страницы
@app.get("/")
async def read_main():
    return "Главная страница"


# Маршрут для страницы администратора
@app.get("/user/admin")
async def read_admin():
    return "Вы вошли как администратор"


# Маршрут для страницы пользователей с параметром user_id
@app.get("/user/{user_id}")
async def read_user_by_id(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


# Маршрут для страницы пользователей с данными из адресной строки
@app.get("/user")
async def read_user_info(username: str = Query(...), age: int = Query(...)):
    return f"Информация о пользователе. Имя: '{username}', Возраст: {age}."
