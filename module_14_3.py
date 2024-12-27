from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


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
inline_keyboard = InlineKeyboardMarkup(row_width=2)
inline_keyboard.add(
    InlineKeyboardButton("Product1", callback_data="product_buying"),
    InlineKeyboardButton("Product2", callback_data="product_buying"),
    InlineKeyboardButton("Product3", callback_data="product_buying"),
    InlineKeyboardButton("Product4", callback_data="product_buying"),
)


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


@dp.message_handler(lambda message: message.text == "Купить")
async def get_buying_list(message: types.Message):
    # Отправка информации о продуктах
    products = [
        {"name": "Баночка с орехами", "description": "Полезные орехи", "price": 100, "image": "1.jpg"},
        {"name": "Баночка с семенами", "description": "Семена для здоровья", "price": 200, "image": "2.jpg"},
        {"name": "Баночка с сухофруктами", "description": "Сладкие и полезные", "price": 300, "image": "3.jpg"},
        {"name": "Баночка с суперфудами", "description": "Суперфуды для энергии", "price": 400, "image": "4.jpg"},
    ]

    for product in products:
        await message.answer(f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}')
        with open(product["image"], "rb") as img:
            await message.answer_photo(img, "Выберите продукт для покупки:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data.startswith("product_"))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = call.data.split("_")[1]
    await call.answer()  # Подтверждение нажатия на кнопку
    await call.message.answer(f"Вы успешно приобрели Продукт {product_id}!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    