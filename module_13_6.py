from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from setting import api


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()

button = InlineKeyboardButton(text= "Рассчитать норму каллорий", callback_data='calories')
button_2 = InlineKeyboardButton(text='Формула расчета', callback_data = 'formulas')
kb.row(button, button_2)




class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
@dp.message_handler(text= ['Рассчитать'])
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.answer()
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.answer()
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    normal_calories = ((float(data['weight']) * 10) + (float(data['growth']) * 6.25) - (float(data['age']) * 5) + 5)
    await message.answer(f'Ваша норма каллорий: {normal_calories}.')
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"Привет! Я бот помогающий твоему здоровью", reply_markup = kb)


@dp.message_handler()
async def all_message(message):
    await message.answer(f"Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
