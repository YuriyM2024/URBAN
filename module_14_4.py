
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

API_TOKEN = '7219539757:AAGxwcPpkhhoCUyVsnfR3RhspZ62FwQsq_k'

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
keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"), KeyboardButton("Купить"))

# Inline клавиатура
inline_keyboard = InlineKeyboardMarkup(row_width=4)
inline_keyboard.add(
    InlineKeyboardButton("Продукт 1", callback_data="product_1"),
    InlineKeyboardButton("Продукт 2", callback_data="product_2"),
    InlineKeyboardButton("Продукт 3", callback_data="product_3"),
    InlineKeyboardButton("Продукт 4", callback_data="product_4"),
)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Нажмите 'Рассчитать' для начала.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Рассчитать")
async def set_age(message: types.Message):
    await Form.age.set()
    await message.answer("Введите ваш возраст:")


@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await Form.growth.set()
    await message.answer("Введите ваш рост в сантиметрах:")


@dp.message_handler(state=Form.growth)
async def process_growth(message: types.Message, state: FSMContext):
    growth = message.text
    await state.update_data(growth=growth)
    await Form.next()
    await message.answer("Введите ваш вес в килограммах:")


@dp.message_handler(state=Form.weight)
async def process_weight(message: types.Message, state: FSMContext):
    weight = message.text
    await state.update_data(weight=weight)

    user_data = await state.get_data()
    age = user_data.get('age')
    growth = user_data.get('growth')
    weight = user_data.get('weight')

    await message.answer(f"Возраст: {age}, Рост: {growth}, Вес: {weight}")
    await state.finish()


@dp.message_handler(lambda message: message.text == "Информация")
async def send_info(message: types.Message):
    await message.answer("Здесь будет информация о том, как работает бот.")


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(product[4], "rb") as img:
            await message.answer_photo(img, "Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("product_"))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split("_")[1]
    await call.answer()  # Подтверждение нажатия на кнопку
    await call.message.answer(f"Вы успешно приобрели Продукт {product_id}!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
