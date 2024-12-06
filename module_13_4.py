from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

api = 'Token'  # Ваш токен

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()        # Состояние для ввода возраста
    growth = State()     # Состояние для ввода роста
    weight = State()     # Состояние для ввода веса


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Введите 'Calories', чтобы начать ввод данных.")


@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await UserState.age.set()  # Устанавливаем состояние для ввода возраста
    await message.answer("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))  # Сохраняем возраст как целое число
    await UserState.growth.set()  # Устанавливаем состояние для ввода роста
    await message.answer("Введите свой рост:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))  # Сохраняем рост как целое число
    await UserState.weight.set()  # Устанавливаем состояние для ввода веса
    await message.answer("Введите свой вес:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))  # Сохраняем вес как целое число
    data = await state.get_data()  # Получаем все ранее введенные данные
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    calories = calculate_calories(weight, growth, age)  # Вычисляем калории
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()  # Завершаем состояние


def calculate_calories(weight, height, age):
    # Формула расчета калорий для мужчин
    calories = 10 * weight + 6.25 * height - 5 * age + 5
    return calories


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
