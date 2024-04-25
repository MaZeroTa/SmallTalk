from json import load
import time
from requests import request
from telebot.async_telebot import AsyncTeleBot
from asyncio import sleep, create_task, gather, run
from itertools import product
from telebot import types
from random import randint, choice, shuffle
from sqlalchemy import create_engine, MetaData, select, Table
from user import User
memory = {}
bot = AsyncTeleBot('6974364023:AAFEvTq68TgJRfB4NcaIgDNK8kNruxNKHZY')
engine = create_engine('sqlite:///info.db')
meta = MetaData()
conn = engine.connect()
meta.reflect(bind=engine)  # эти четыре строки не трошьте, остальные в пример


async def cool_down():
    while True:
        await sleep(1)
        if time.strftime("%H:%M:%S", time.localtime(time.time())) in ("06:24:00", "06:24:01"):
            for elem in memory:
                memory[elem].cool_down()
        if int(time.strftime("%S", time.localtime(time.time()))[1]) % 2 == 0:
            for elem in memory:
                memory[elem].count_of_message = 0


def load_from_db(meta):
    query = meta.tables['user'].select()
    result = conn.execute(query)
    for row in result:
        memory[row[0]] = User('User', row[0], meta, conn)
