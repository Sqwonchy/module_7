from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
import logging
from module_14_4 import *
import set_api
import module_14_5_2
import re

logging.basicConfig(level=logging.INFO)

api = set_api.api
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать норму калорий"),
         KeyboardButton(text="Формула расчета")],
        [KeyboardButton(text="Купить"),
         KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True
)
inline_list_by = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product_1', callback_data="product_buying"),
            InlineKeyboardButton(text='Product_2', callback_data="product_buying"),
            InlineKeyboardButton(text='Product_3', callback_data="product_buying"),
            InlineKeyboardButton(text='Product_4', callback_data="product_buying")
        ]
    ]
)

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

def is_latin(word):
    return bool(re.fullmatch(r'[a-zA-Z]+', word))

def chek_email(email):
    data = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(data,email))



@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Хотите узнать формулу или просто подсчитать калории?\nВыберите опцию из меню ниже:",
        reply_markup=start_keyboard,
    )


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        await message.answer(f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]} \n ")
        with open(f"files/img_{product[0]}.png", "rb") as img:
            await message.answer_photo(img)
    await message.answer(text='Выберите продукт для покупки:', reply_markup=inline_list_by)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт ")


@dp.message_handler(text='Формула расчета')
async def get_formulas(message):
    await message.answer("Формула расчета: 10 х вес (кг) + 6.25 х рост (см) – 5 х возраст (г) + 5")


@dp.message_handler(text="Рассчитать норму калорий")
async def set_age(message):
    await message.answer("Введите свой возраст (в годах):")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age <= 0 or age > 120:
            raise ValueError("Некорректный возраст")
        await state.update_data(age=age)
        await message.answer("Введите свой рост (в сантиметрах):")
        await UserState.growth.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (число от 1 до 120).")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = float(message.text)
        if growth <= 0 or growth > 300:
            raise ValueError("Некорректный рост")
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес (в килограммах):")
        await UserState.weight.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост (число от 1 до 300).")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text)
        if weight <= 0 or weight > 500:
            raise ValueError("Некорректный вес")
        await state.update_data(weight=weight)
        data = await state.get_data()

        normal_calories = (
                (data['weight'] * 10) +
                (data['growth'] * 6.25) -
                (data['age'] * 5) +
                5
        )
        await message.answer(f"Ваша норма калорий: {normal_calories:.2f} ккал.")
        await state.finish()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный вес (число от 1 до 500).")

@dp.message_handler(text= 'Регистрация')
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    try:
        if is_latin(username):
            if not  module_14_5_2.is_included(username):
                await state.update_data(username=username)
                await message.answer('Введите свою почту ')
                await RegistrationState.email.set()
            else:
                raise ValueError()
        else:
            raise TypeError()
    except TypeError:
        await message.answer('Введите подходящий username (только латинские буквы)')
    except ValueError:
        await message.answer("Пользователь с данным username уже существует введите другой username")

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    mail = message.text
    try:
        if chek_email(mail):
            await state.update_data(email=mail)
            await message.answer("Введите свой возраст:")
            await RegistrationState.age.set()
        else:
            raise ValueError
    except ValueError:
        await message.answer('Введен неправильный формат почты')

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if 1 <= age <= 150:
            await state.update_data(age=age)
            data = await state.get_data()
            module_14_5_2.add_user(data['username'],data['email'],data['age'])
            await state.finish()
        else:
            raise ValueError
    except ValueError:
        await message.answer('Введите коррекный возраст')


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение или выберите опцию из меню.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

