from fastapi import FastAPI
from fastapi import HTTPException

# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Маршрут к главной странице
@app.get("/")
async def read_root():
    return {"message": "Главная страница"}


# Маршрут к странице администратора
@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршрут к страницам пользователей с передачей данных в адресной строке
@app.get("/user")
async def read_user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
