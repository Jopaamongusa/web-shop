import aiogram
import aiogram.filters
import sqlite3
import pandas
import os
from aiogram import asyncio

ID_USERS = 2
ID_PRODUCT = 4
ID_CART = 6
ID_CHAT =  -1002198970276

t_f_send_massege = False

# path = os.path.abspath(__file__+f"/../../project/data.db")

# db = sqlite3.connect(path)

# product =  pandas.read_sql_table(table_name= 'product', con= db)
# try:
#     Delivery = pandas.read_sql_table(teble_name = 'delivery',  con = db)
# except:
#     Delivery = None
# users = pandas.read_sql_table(table_name='users', con= db)

path = os.path.abspath(__file__ + "/../../project/data.db")

db = sqlite3.connect(path)

product_query = "SELECT * FROM product"
product = pandas.read_sql_query(product_query, db)

try:
    delivery_query = "SELECT * FROM delivery"
    Delivery = pandas.read_sql_query(delivery_query, db)
except:
    Delivery = None

users_query = "SELECT * FROM users"
users = pandas.read_sql_query(users_query, db)


bot = aiogram.Bot(token='7457520671:AAHm8b8bC932IDmJq_7gLNZCNitU8FSKLKM')

dispatcer = aiogram.Dispatcher()

button_get_users = aiogram.types.KeyboardButton(text="/users")
button_get_product = aiogram.types.KeyboardButton(text="/product")
button_add_cart = aiogram.types.KeyboardButton(text="/cart")
keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard=[[button_get_users, button_get_product, button_add_cart]])

@dispatcer.message(aiogram.filters.CommandStart())

async def start(message: aiogram.types.Message):
    await message.answer(text= 'hello', reply_markup= keyboard)

@dispatcer.message(aiogram.filters.Command(commands = ['users']))

async def get_users(message: aiogram.types.Message):
    await bot.send_message(
        chat_id="-1002198970276",
        text= f'users:\n {users}',
        message_thread_id= ID_USERS
    )

@dispatcer.message(aiogram.filters.Command(commands = ['product']))

async def get_users(message: aiogram.types.Message):
    await bot.send_message(
        chat_id="-1002198970276",
        text=f'product: \n {product}',
        message_thread_id= ID_PRODUCT
    )

# @dispatcer.message(aiogram.filters.Command(commands = ['cart']))

# async def get_users(message: aiogram.types.Message):
#     await bot.send_message(
#         chat_id="-1002198970276",
#         text= 'cart: ...',
#         message_thread_id= ID_CART
#     )

@dispatcer.message(aiogram.filters.Command(commands = ['cart'])) 

async def send_info(message: aiogram.types.Message):
    if Delivery != None:
        await bot.send_message(
        chat_id = "-1002198970276",
        message_thread_id = ID_PRODUCT,
        text =  f"""
                    Замовлення {Delivery.name} буде відправлений 
                    до міста: {Delivery.city}
                    та на віділ почти: {Delivery.post} 
                    на і'мя та фамілію: {Delivery.name} {Delivery.vorname}
                    також було наділано повідомлення на почту: {Delivery.email} 
                """
        )
    else:
        await bot.send_message(
            chat_id = "-1002198970276",
            message_thread_id = ID_PRODUCT,
            text = "Замовлень немає",
        )
async def main():
    await dispatcer.start_polling(bot)

asyncio.run(main())

