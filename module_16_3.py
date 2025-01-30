from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI()

# Инициализация словаря users
users = {'1': 'Имя: Example, возраст: 18'}


# Модель для валидации данных
class UserData(BaseModel):
    username: str
    age: int


@field_validator('age')
def age_must_be_positive(v):
    if v <= 0:
        raise ValueError('Возраст должен быть положительным числом')
    return v



@app.get("/users")
def get_users():
    return users



@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    # Валидация данных
    user_data = UserData(username=username, age=age)

    # Генерация нового ключа
    new_id = str(max(int(k) for k in users.keys()) + 1) if users else '1'

    # Добавление пользователя
    users[new_id] = f"Имя: {user_data.username}, возраст: {user_data.age}"

    return f"User {new_id} is registered"



@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    # Валидация данных
    user_data = UserData(username=username, age=age)

    # Проверка существования пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Обновление данных
    users[user_id] = f"Имя: {user_data.username}, возраст: {user_data.age}"

    return f"User {user_id} has been updated"



@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    # Проверка существования пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Удаление пользователя
    del users[user_id]

    return f"User {user_id} has been deleted"
