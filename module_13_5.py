from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Определение состояний
class Form(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Нажмите 'Рассчитать' для начала.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Рассчитать")
async def set_age(message: types.Message):
    await Form.age.set()  # Переход к состоянию age
    await message.answer("Введите ваш возраст:")


@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    # Обработка возраста
    age = message.text
    await state.update_data(age=age)  # Сохранение возраста

    await Form.growth.set()  # Переход к состоянию growth
    await message.answer("Введите ваш рост в сантиметрах:")


@dp.message_handler(state=Form.growth)
async def process_growth(message: types.Message, state: FSMContext):
    # Обработка роста
    growth = message.text
    await state.update_data(growth=growth)  # Сохранение роста

    await Form.next()  # Переход к состоянию weight
    await message.answer("Введите ваш вес в килограммах:")


@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    # Обработка веса
    weight = message.text
    await state.update_data(weight=weight)  # Сохранение веса

    # Получение данных и завершение состояния
    user_data = await state.get_data()
    age = user_data.get('age')
    growth = user_data.get('growth')
    weight = user_data.get('weight')

# Здесь можно добавить логику для расчёта калорий
    await message.answer(f"Возраст: {age}, Рост: {growth}, Вес: {weight}")

    await state.finish()  # Завершение состояния


@dp.message_handler(lambda message: message.text == "Информация")
async def send_info(message: types.Message):
    await message.answer("Здесь будет информация о том, как работает бот.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
