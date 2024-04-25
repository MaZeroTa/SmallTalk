from FCl import *


# Handle '/start'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    if message.chat.id in memory and message.chat.id > 0:
        return 0
    await bot.send_message(message.chat.id, """Как тебя зовут?""")
    print(message.chat.id)
    memory[message.chat.id] = User('User0001', message.chat.id, meta, conn)
    print(message.chat.id)
    print(memory[message.chat.id].get_data())


# Handle '/help'
@bot.message_handler(commands=['help'])
async def helpa(message):
    await bot.send_message(message.chat.id, f"""
/help - помощь
/меню - выход в основное меню
/заработок - выход в меню работ
/name - смена имён
/инвентарь - просмотр инвентаря
/профиль - просмотр профиля
""")


@bot.message_handler(commands=['профиль'])
async def profile(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    await bot.send_message(message.chat.id, f'''{memory[message.chat.id].name}, это ваш профиль:''')
    await bot.send_message(message.chat.id, memory[message.chat.id].get_data())


@bot.message_handler(commands=['gm'])
async def gm(message):
    it = load(open('data/dictionaries/admin.json', 'r', encoding='UTF-8'))
    if message.chat.id not in memory and message.chat.id in it:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''/unban''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/reputation''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/money''')
    markup.add(item1)
    memory[message.chat.id].god_mod = 1
    await bot.send_message(message.chat.id, f'''{memory[message.chat.id].name}, 
Вы получили доступ к командам админа.''', reply_markup=markup)


@bot.message_handler(commands=['unban'])
async def unban(message):
    if message.chat.id not in memory or not memory[message.chat.id].god_mod:
        return 0
    await bot.send_message(message.chat.id, f'''Введите id пользователя:''', reply_markup=None)
    memory[message.chat.id].god_mod = 'unban'


@bot.message_handler(commands=['reputation'])
async def reputation(message):
    if message.chat.id not in memory or not memory[message.chat.id].god_mod:
        return 0
    await bot.send_message(message.chat.id, '''Введите id пользователя и значение вида: {id} {score} ''',
                           reply_markup=None)
    memory[message.chat.id].god_mod = 'reputation'


@bot.message_handler(commands=['money'])
async def reputation(message):
    if message.chat.id not in memory or not memory[message.chat.id].god_mod:
        return 0
    await bot.send_message(message.chat.id, '''Введите id пользователя и значение вида: {id} {score} ''',
                           reply_markup=None)
    memory[message.chat.id].god_mod = 'money'


@bot.message_handler(commands=['инвентарь'])
async def inventory(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    await bot.send_message(message.chat.id, f'''{memory[message.chat.id].name}, это ваш инвентарь:''')
    await bot.send_message(message.chat.id, memory[message.chat.id].get_inventory())


@bot.message_handler(commands=['взаимодействовать'])
async def vzaimo(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''/подарок''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/общение''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/меню''')
    markup.add(item1)
    await bot.send_message(message.chat.id, f'''{memory[message.chat.id].name}, \
как Вы хотите взаимодействовать с {memory[message.chat.id].girl_name}''', reply_markup=markup)


@bot.message_handler(commands=['меню'])
async def menu(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    self = memory[message.chat.id]
    self.work = False
    self.sociable_mode = False
    self.blackjack_game = 0
    self.rulet = 0
    self.hangman = 0
    self.god_mod = 0
    self.mini_game_mode = False
    self.gift_mode = False
    self.store_mode = False
    self.change_name_mode = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''/взаимодействовать''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/заработок''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/магазин''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/инвентарь''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/профиль''')
    markup.add(item1)
    await bot.send_message(message.chat.id, f'''Меню''', reply_markup=markup)


@bot.message_handler(commands=['подарок'])
async def gift(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''Цветы''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Кольцо''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Шоколад''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/меню''')
    markup.add(item1)
    memory[message.chat.id].gift_mode = True
    await bot.send_message(message.chat.id, f'''Что вы хотите подарить?''', reply_markup=markup)


@bot.message_handler(commands=['name'])
async def name(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(f'''Себе ({memory[message.chat.id].name})''')
    markup.add(item1)
    item1 = types.KeyboardButton(f'''Ей ({memory[message.chat.id].girl_name})''')
    markup.add(item1)
    memory[message.chat.id].change_name_mode = 1
    await bot.send_message(message.chat.id, f'''Кому Вы хотите изменить имя??''', reply_markup=markup)


@bot.message_handler(commands=['магазин'])
async def store(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''Цветы''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Кольцо''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Шоколад''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/меню''')
    markup.add(item1)
    memory[message.chat.id].store_mode = True
    await bot.send_message(message.chat.id, f'''Что вы хотите купить?''', reply_markup=markup)
    await bot.send_message(message.chat.id, f'''Цветы - 10$ ({memory[message.chat.id].cool_down_data['Цветы']} шт.)
Кольцо - 50$ ({memory[message.chat.id].cool_down_data['Кольцо']} шт.)
Шоколад - 2$ ({memory[message.chat.id].cool_down_data['Шоколад']} шт.)''')


@bot.message_handler(commands=['заработок'])
async def work(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('''Викторина''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Виселица''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Блекджек''')
    markup.add(item1)
    item1 = types.KeyboardButton('''Рулетка''')
    markup.add(item1)
    item1 = types.KeyboardButton('''/меню''')
    markup.add(item1)
    memory[message.chat.id].mini_game_mode = True
    await bot.send_message(message.chat.id, f'''Как хотите заработать?''', reply_markup=markup)


@bot.message_handler(commands=['общение'])
async def sociable(message):
    if message.chat.id not in memory:
        return 0
    elif memory[message.chat.id].ban:
        return 0
    with open('data/dictionaries/phrases.json', encoding='utf-8') as json_file:
        data = load(json_file)
    if not memory[message.chat.id].sociable_const:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(data['acquaintance'][0]['text'])
        item3 = types.KeyboardButton('/меню')
        markup.add(item1)
        markup.add(item3)
        memory[message.chat.id].sociable_mode = True
        await bot.send_message(message.chat.id, "Выберите сообщение:", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(data['answers'][0]['text'])
        markup.add(item1)
        item3 = types.KeyboardButton('/меню')
        markup.add(item3)
        memory[message.chat.id].sociable_mode = True
        await bot.send_message(message.chat.id, "Выберите сообщение:", reply_markup=markup)


@bot.message_handler(commands=['status'])
async def status(message):
    await bot.send_message(message.chat.id, f'Запущен')


@bot.message_handler(content_types='text')
async def text(message):
    if memory[message.chat.id].name == 'User0001':
        memory[message.chat.id].name = message.text
        await bot.send_message(message.chat.id, f'Очень приятно, {memory[message.chat.id].name}.')
        await bot.send_message(message.chat.id, f'''{memory[message.chat.id].name}, это ваш профиль:''')
        await bot.send_message(message.chat.id, memory[message.chat.id].get_data())
        await menu(message)
    memory[message.chat.id].count_of_message += 1
    if memory[message.chat.id].god_mod == 1:
        memory[message.chat.id].god_mod = 0
    if memory[message.chat.id].spam_defense():
        await bot.send_message(message.chat.id, f'Вы слишком часто отправляли сообщения,\
теперь вы не сможете их отправлять до 6:24.')
    elif memory[message.chat.id].ban and not memory[message.chat.id].god_mod:
        return 0
    elif memory[message.chat.id].sociable_mode:
        data = load(open('data/dictionaries/phrases.json', 'r', encoding='UTF-8'))
        if memory[message.chat.id].sociable_const:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            if message.text == data['answers'][0]['text']:
                memory[message.chat.id].score += 1
                item1 = types.KeyboardButton(data['answers'][1]['text'])
                markup.add(item1)
                item2 = types.KeyboardButton('/меню')
                markup.add(item2)
                await bot.send_message(message.chat.id, f'{data["answers"][0]["answers"]}', reply_markup=markup)
            elif message.text == data['answers'][1]['text']:
                memory[message.chat.id].score += 1
                item1 = types.KeyboardButton(data['answers'][2]['text'])
                markup.add(item1)
                item2 = types.KeyboardButton("/меню")
                markup.add(item2)
                await bot.send_message(message.chat.id, data['answers'][1]['answers_option'][
                    randint(0, len(data['answers'][1]['answers_option']) - 1)], reply_markup=markup)
            elif message.text == data['answers'][3][0]['text']:
                memory[message.chat.id].score += 1
                item1 = types.KeyboardButton(data['answers'][3][1]['text'])
                item2 = types.KeyboardButton("/меню")
                markup.add(item1)
                markup.add(item2)
                await bot.send_message(message.chat.id, data['answers'][3][0]['answers'][
                    randint(0, len(data['answers'][3][0]['answers']) - 1)], reply_markup=markup)
            elif message.text == data['answers'][2]['text']:
                memory[message.chat.id].score += 1
                item1 = types.KeyboardButton(data['answers'][3 + randint(0, 1)][0]['text'])
                item2 = types.KeyboardButton("/меню")
                markup.add(item1)
                markup.add(item2)
                await bot.send_message(message.chat.id,
                                       data['answers'][2]['answers'][
                                           randint(0, len(data['answers'][2]['answers']) - 1)],
                                       reply_markup=markup)
            elif message.text == data['answers'][3][1]['text']:
                memory[message.chat.id].score += 1
                random_answer_index = randint(0, len(data['answers'][3][1]['answers']) - 1)
                await bot.send_message(message.chat.id, data['answers'][3][1]['answers'][random_answer_index])
                item1 = types.KeyboardButton("/меню")
                markup.add(item1)
                if random_answer_index in [0, 2]:
                    await bot.send_message(message.chat.id,
                                           "Вы погуляли с девушкой, к вашим отношениям добавлено 5 очков.",
                                           reply_markup=markup)
                    memory[message.chat.id].score += 5
                    memory[message.chat.id].sociable_mode = False
                else:
                    await bot.send_message(message.chat.id, "Вам не удалось погулять с девушкой.", reply_markup=markup)
                    memory[message.chat.id].sociable_mode = False
            elif message.text == data['answers'][4][0]['text']:
                memory[message.chat.id].score += 1
                random_answer_index_2 = randint(0, len(data['answers'][4][0]['answers']) - 1)
                await bot.send_message(message.chat.id, data['answers'][4][0]['answers'][random_answer_index_2])
                item1 = types.KeyboardButton("/меню")
                markup.add(item1)
                if random_answer_index_2 in [0]:
                    await bot.send_message(message.chat.id,
                                           "Вы погуляли с девушкой, к вашим отношениям добавлено 5 очков.",
                                           reply_markup=markup)
                    memory[message.chat.id].score += 5
                    memory[message.chat.id].sociable_mode = False
                else:
                    await bot.send_message(message.chat.id, "Вам не удалось погулять с девушкой.", reply_markup=markup)
                    memory[message.chat.id].sociable_mode = False
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            if message.text == data['acquaintance'][0]['text']:
                memory[message.chat.id].score += 1
                item1 = types.KeyboardButton(f"{data['acquaintance'][1]['text']} {memory[message.chat.id].name}")
                markup.add(item1)
                item2 = types.KeyboardButton('/меню')
                markup.add(item2)
                for elem in data['acquaintance'][0]['answers']:
                    await bot.send_message(message.chat.id, elem, reply_markup=markup)

            elif message.text == f"{data['acquaintance'][1]['text']} {memory[message.chat.id].name}":
                await bot.send_message(message.chat.id,
                                       f"{data['acquaintance'][1]['answers']} {memory[message.chat.id].girl_name}")
                memory[message.chat.id].score += 11
                item2 = types.KeyboardButton('/меню')
                markup.add(item2)
                await bot.send_message(message.chat.id,
                                       f"Вы познакомились с девушкой {memory[message.chat.id].girl_name}"
                                       f" и получили 10 очков отношений",
                                       reply_markup=markup)
                memory[message.chat.id].sociable_const = True
                memory[message.chat.id].sociable_mode = False

    elif message.text in ('Цветы', "Шоколад", "Кольцо") and memory[message.chat.id].gift_mode:
        if message.text == 'Кольцо' and memory[message.chat.id].inventory['Кольцо'] > 0:
            memory[message.chat.id].inventory['Кольцо'] -= 1
            await bot.send_message(message.chat.id, f'Вы подарили Кольцо. {memory[message.chat.id].girl_name} довольна.'
                                                    f' Осталось {memory[message.chat.id].inventory['Кольцо']}')
            await bot.send_message(message.chat.id, f'+10 к отношениям')
            memory[message.chat.id].score += 10
        elif message.text == 'Цветы' and memory[message.chat.id].inventory['Цветы'] > 0:
            memory[message.chat.id].inventory['Цветы'] -= 1
            await bot.send_message(message.chat.id, f'Вы подарили Цветы. {memory[message.chat.id].girl_name} рада. '
                                                    f'Осталось {memory[message.chat.id].inventory['Цветы']}')
            await bot.send_message(message.chat.id, f'+6 к отношениям')
            memory[message.chat.id].score += 6
        elif message.text == 'Шоколад' and memory[message.chat.id].inventory['Шоколад'] > 0:
            memory[message.chat.id].inventory['Шоколад'] -= 1
            await bot.send_message(message.chat.id,
                                   f'Вы подарили Шоколад. {memory[message.chat.id].girl_name} в восторге.'
                                   f'Осталось {memory[message.chat.id].inventory['Шоколад']}')
            await bot.send_message(message.chat.id, f'+1 к отношениям')
            memory[message.chat.id].score += 1
        else:
            await bot.send_message(message.chat.id, f'У вас нет этого подарка. Купите его в магазине')
        await gift(message)
    elif message.text in ('Цветы', "Шоколад", "Кольцо") and memory[message.chat.id].store_mode:
        if message.text == 'Кольцо' and memory[message.chat.id].cool_down_data['Кольцо'] \
                and memory[message.chat.id].money >= 50:
            memory[message.chat.id].cool_down_data['Кольцо'] -= 1
            await bot.send_message(message.chat.id, f'Вы купили Кольцо')
            memory[message.chat.id].money -= 50
            await bot.send_message(message.chat.id, f'-50$\nОсталось {memory[message.chat.id].money}')
            memory[message.chat.id].inventory['Кольцо'] += 1
        elif message.text == 'Цветы' and memory[message.chat.id].cool_down_data['Цветы'] and \
                memory[message.chat.id].money >= 10:
            memory[message.chat.id].cool_down_data['Цветы'] -= 1
            await bot.send_message(message.chat.id, f'Вы купили Цветы')
            memory[message.chat.id].money -= 10
            await bot.send_message(message.chat.id, f'-10$\nОсталось {memory[message.chat.id].money}')
            memory[message.chat.id].inventory['Цветы'] += 1
        elif message.text == 'Шоколад' and memory[message.chat.id].cool_down_data['Шоколад'] and \
                memory[message.chat.id].money >= 2:
            memory[message.chat.id].cool_down_data['Шоколад'] -= 1
            await bot.send_message(message.chat.id, f'Вы купили Шоколад')
            memory[message.chat.id].money -= 2
            await bot.send_message(message.chat.id, f'-2$\nОсталось {memory[message.chat.id].money}')
            memory[message.chat.id].inventory['Шоколад'] += 1
        else:
            await bot.send_message(message.chat.id, f'Недостаточно средств или товары на сегодня закончились')
        if (memory[message.chat.id].cool_down_data['Цветы'] == 0 and memory[message.chat.id].cool_down_data['Кольцо']
                == 0 and memory[message.chat.id].cool_down_data['Шоколад'] == 0):
            await bot.send_message(message.chat.id, f'Товары на сегодня закончились. Возвращайтесь завтра в 6:24')
        await store(message)
    elif memory[message.chat.id].change_name_mode == 1:
        if message.text == f'Себе ({memory[message.chat.id].name})':
            await bot.send_message(message.chat.id, f'Введите своё новое имя')
            memory[message.chat.id].change_name_mode = 2
        elif message.text == f'Ей ({memory[message.chat.id].girl_name})':
            await bot.send_message(message.chat.id, f'Введите её новое имя')
            memory[message.chat.id].change_name_mode = 3
    elif memory[message.chat.id].change_name_mode == 2:
        memory[message.chat.id].change_name_mode = 0
        await bot.send_message(message.chat.id, f'Теперь Ваше имя {message.text}')
        memory[message.chat.id].name = message.text
        await menu(message)
    elif memory[message.chat.id].change_name_mode == 3:
        memory[message.chat.id].change_name_mode = 0
        await bot.send_message(message.chat.id, f'Теперь её имя {message.text}')
        memory[message.chat.id].girl_name = message.text
        await menu(message)
    elif memory[message.chat.id].work:
        if message.text == memory[message.chat.id].work:
            memory[message.chat.id].money += 10
            await bot.send_message(message.chat.id, f'Вы заработали 10$')
        else:
            if memory[message.chat.id].money > 1:
                memory[message.chat.id].money -= 1
                await bot.send_message(message.chat.id, f'Вы оштрафованы на 1$')
            else:
                await bot.send_message(message.chat.id, f'Из-за штрафов вас приговорили к общественным работам.')
                await bot.send_message(message.chat.id, f'Вы будете заняты до 6:24')
                memory[message.chat.id].ban = True
        memory[message.chat.id].work = False
        await menu(message)
    elif message.text == 'Взять' and memory[message.chat.id].blackjack_game:
        if sum(memory[message.chat.id].value_card[elem[0]] for elem in
               memory[message.chat.id].variables['card_player']) <= 21:
            shuffle(memory[message.chat.id].variables['deck'])
            memory[message.chat.id].variables['card_player'] += [memory[message.chat.id].variables['deck'].pop()]
            cards_player = memory[message.chat.id].variables['card_player'][-1]
            await bot.send_message(message.chat.id,
                                   f"Вы взяли карту {cards_player[0]} {cards_player[1]}")
            await bot.send_message(message.chat.id,
                                   f"Сумма ваших карт: {sum(memory[message.chat.id].value_card[elem[0]] for elem
                                                            in memory[message.chat.id].variables['card_player'])}")
        if sum(memory[message.chat.id].value_card[elem[0]] for elem in
               memory[message.chat.id].variables['card_player']) > 21:
            await bot.send_message(message.chat.id,
                                   f"Вы проиграли! Вы потеряли: {memory[message.chat.id].blackjack_money} монет")
            memory[message.chat.id].money -= memory[message.chat.id].blackjack_money
            memory[message.chat.id].blackjack_money = 0
            memory[message.chat.id].blackjack = 0
            memory[message.chat.id].blackjack_game = 0
            memory[message.chat.id].variables = {'deck': list(
                product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз'],
                        ['Черви', 'Трефы', 'Пики', 'Буби'])),
                'store_player': 0,
                'store_dealer': 0,
                'money': 0,
                'card_player': [],
                'card_dealer': []}

            memory[message.chat.id].value_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                                  '10': 10, 'Валет': 10,
                                                  'Дама': 10,
                                                  'Король': 10, 'Туз': 11}
            await menu(message)
    elif message.text == 'Остановиться' and memory[message.chat.id].blackjack_game:
        while sum(memory[message.chat.id].value_card[elem[0]] for elem in
                  memory[message.chat.id].variables['card_dealer']) < 17:
            shuffle(memory[message.chat.id].variables['deck'])
            memory[message.chat.id].variables['card_dealer'] += [memory[message.chat.id].variables['deck'].pop()]
            cards_dealer = memory[message.chat.id].variables['card_dealer'][-1]
            await bot.send_message(message.chat.id,
                                   f'Дилер взял карту: {cards_dealer[0]} {cards_dealer[1]}')
            await bot.send_message(message.chat.id,
                                   f'Сумма карт дилера: {sum(memory[message.chat.id].value_card[elem[0]] for elem
                                                             in memory[message.chat.id].variables['card_dealer'])}')
        if (sum(memory[message.chat.id].value_card[elem[0]] for elem in
                memory[message.chat.id].variables['card_dealer']) < sum(
            memory[message.chat.id].value_card[elem[0]] for elem in
            memory[message.chat.id].variables['card_player']) < 22 or
                (sum(memory[message.chat.id].value_card[elem[0]] for elem in
                     memory[message.chat.id].variables['card_dealer']) > 21 and sum(
                    memory[message.chat.id].value_card[elem[0]]
                    for elem in memory[message.chat.id].variables['card_player']) <= 21)):  # не трогать, а то сломаешь
            await bot.send_message(message.chat.id,
                                   f"Вы выиграли! Ваш приз: {memory[message.chat.id].blackjack_money} монет")
            memory[message.chat.id].money += memory[message.chat.id].blackjack_money
            memory[message.chat.id].blackjack_money = 0
            memory[message.chat.id].blackjack = 0
            memory[message.chat.id].blackjack_game = 0
            memory[message.chat.id].variables = {'deck': list(
                product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз'],
                        ['Черви', 'Трефы', 'Пики', 'Буби'])),
                'store_player': 0,
                'store_dealer': 0,
                'money': 0,
                'card_player': [],
                'card_dealer': []}

            memory[message.chat.id].value_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                                  '10': 10, 'Валет': 10,
                                                  'Дама': 10,
                                                  'Король': 10, 'Туз': 11}
            await menu(message)

        elif (sum(memory[message.chat.id].value_card[elem[0]] for elem in
                  memory[message.chat.id].variables['card_dealer']) ==
              sum(memory[message.chat.id].value_card[elem[0]] for elem in
                  memory[message.chat.id].variables['card_player'])):
            await bot.send_message(message.chat.id,
                                   f"Ничья! Вы ничего не выйграли и ничего не проиграли")
            memory[message.chat.id].blackjack_money = 0
            memory[message.chat.id].blackjack = 0
            memory[message.chat.id].blackjack_game = 0
            memory[message.chat.id].variables = {'deck': list(
                product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз'],
                        ['Черви', 'Трефы', 'Пики', 'Буби'])),
                'store_player': 0,
                'store_dealer': 0,
                'money': 0,
                'card_player': [],
                'card_dealer': []}

            memory[message.chat.id].value_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                                  '10': 10, 'Валет': 10,
                                                  'Дама': 10,
                                                  'Король': 10, 'Туз': 11}
            await menu(message)
        else:
            await bot.send_message(message.chat.id,
                                   f"Вы проиграли! Вы потеряли: {memory[message.chat.id].blackjack_money} монет")
            memory[message.chat.id].money -= memory[message.chat.id].blackjack_money
            memory[message.chat.id].blackjack_money = 0
            memory[message.chat.id].blackjack = 0
            memory[message.chat.id].blackjack_game = 0
            memory[message.chat.id].variables = {'deck': list(
                product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз'],
                        ['Черви', 'Трефы', 'Пики', 'Буби'])),
                'store_player': 0,
                'store_dealer': 0,
                'money': 0,
                'card_player': [],
                'card_dealer': []}

            memory[message.chat.id].value_card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                                  '10': 10, 'Валет': 10,
                                                  'Дама': 10,
                                                  'Король': 10, 'Туз': 11}
            await menu(message)
    elif message.text == 'Викторина' and memory[message.chat.id].mini_game_mode:
        memory[message.chat.id].mini_game_mode = False
        it = choice(load(open('data/dictionaries/work.json', 'r', encoding='UTF-8')))
        memory[message.chat.id].work = it['true_ans']
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for elem in it['answers']:
            markup.add(types.KeyboardButton(elem))
        await bot.send_message(message.chat.id, f'''{it['question']}''', reply_markup=markup)
    elif memory[message.chat.id].god_mod:
        if memory[message.chat.id].god_mod == 'unban':
            try:
                memory[int(message.text)].ban = False
                await bot.send_message(message.chat.id, 'Бан снят')
            except Exception as e:
                await bot.send_message(message.chat.id, 'Ошибка')
        elif memory[message.chat.id].god_mod == 'money':
            try:
                memory[int(message.text.split()[0])].money += int(message.text.split()[1])
                await bot.send_message(message.chat.id, 'Начисление')
            except Exception as e:
                await bot.send_message(message.chat.id, 'Ошибка')
        elif memory[message.chat.id].god_mod == 'reputation':
            try:
                memory[int(message.text.split()[0])].score += int(message.text.split()[1])
                await bot.send_message(message.chat.id, 'Начисление')
            except Exception as e:
                await bot.send_message(message.chat.id, 'Ошибка')
        memory[message.chat.id].god_mod = 0
    elif message.text == 'Виселица' and memory[message.chat.id].mini_game_mode:
        memory[message.chat.id].mini_game_mode = False
        memory[message.chat.id].hangman = 1
        it = load(open('data/dictionaries/hangman.json', 'r', encoding='UTF-8'))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for elem in it:
            markup.add(types.KeyboardButton(elem))
        markup.add('/меню')
        await bot.send_message(message.chat.id, f'''Выберите тему''', reply_markup=markup)
    elif message.text == 'Рулетка' and memory[message.chat.id].mini_game_mode:
        memory[message.chat.id].mini_game_mode = False
        memory[message.chat.id].rulet = 1
        await bot.send_message(message.chat.id, f'''10 - 1:1
20 - 2:1
50 - 4:1''')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('10'))
        markup.add(types.KeyboardButton('20'))
        markup.add(types.KeyboardButton('50'))
        markup.add(types.KeyboardButton('/меню'))
        await bot.send_message(message.chat.id, f'''Выберите ставку''', reply_markup=markup)
    elif memory[message.chat.id].rulet:
        if message.text in ('10', '20', '50') and memory[message.chat.id].money >= int(message.text):
            memory[message.chat.id].money -= int(message.text)
            if message.text == '10':
                it = 1
            elif message.text == '20':
                it = 2
            else:
                it = 4
            data = randint(0, it)
            await bot.send_video(message.chat.id, open('data/static/rulet.mp4', 'rb'))
            await sleep(4)
            if data == 0:
                await bot.send_message(message.chat.id, f'''Поздравляю вы выиграли: {int(message.text) * it}$''')
                memory[message.chat.id].money += int(message.text) * (it + 1)
            else:
                await bot.send_message(message.chat.id, f'''Увы вы проиграли: {int(message.text)}$''')
            memory[message.chat.id].rulet = 0
            await menu(message)
        else:
            await bot.send_message(message.chat.id, f'''Ошибка ввода''')
            await bot.send_message(message.chat.id, f'''Выберите ставку''')

    elif message.text == 'Блекджек' and memory[message.chat.id].mini_game_mode:
        play = {'in_game': 0}
        memory[message.chat.id].mini_game_mode = False
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        memory[message.chat.id].blackjack = 1
        bets = [1, 5, 10, 25, 100]
        bets = list(filter(lambda x: x <= memory[message.chat.id].money, bets))
        for elem in bets:
            markup.add(types.KeyboardButton(elem))
        markup.add(types.KeyboardButton('/меню'))
        await bot.send_message(message.chat.id, 'Выберите ставку:', reply_markup=markup)
    elif memory[message.chat.id].blackjack:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = ['Взять', 'Остановиться', '/меню']
        if message.text.isdigit() and memory[message.chat.id].blackjack_game == 0:
            if memory[message.chat.id].money >= int(message.text):
                memory[message.chat.id].blackjack_money = int(message.text)
                await bot.send_message(message.chat.id, f'Ставка {message.text} монет принята. Раздача карт.')
                memory[message.chat.id].blackjack_game = 1
                shuffle(memory[message.chat.id].variables['deck'])
                memory[message.chat.id].variables['card_player'] += [memory[message.chat.id].variables['deck'].pop(),
                                                                     memory[message.chat.id].variables['deck'].pop()]
                for elem in button:
                    markup.add(types.KeyboardButton(elem))
                await bot.send_message(message.chat.id,
                                       f"Ваши карты: {'; '.join([f"{card[0]} {card[1]}" for card in
                                                                 memory[message.chat.id].variables['card_player']])}",
                                       reply_markup=markup)
                await bot.send_message(message.chat.id,
                                       f'Сумма ваших карт: {sum(memory[message.chat.id].value_card[elem[0]] for elem in
                                                                memory[message.chat.id].variables['card_player'])}')
                shuffle(memory[message.chat.id].variables['deck'])
                memory[message.chat.id].variables['card_dealer'] += [memory[message.chat.id].variables['deck'].pop()]
                await bot.send_message(message.chat.id,
                                       f'Карта дилера: {'; '.join([f"{card[0]} {card[1]}" for card in
                                                                   memory[message.chat.id].variables['card_dealer']])}')
                await bot.send_message(message.chat.id,
                                       f'Сумма карт дилера: {sum(memory[message.chat.id].value_card[elem[0]] for elem in
                                                                 memory[message.chat.id].variables['card_dealer'])}')
                await bot.send_message(message.chat.id, 'Взять карту или остановиться?')
    elif memory[message.chat.id].hangman:
        if memory[message.chat.id].hangman == 1:
            it = load(open('data/dictionaries/hangman.json', 'r', encoding='UTF-8'))
            if message.text in it:
                word = choice(it[message.text])
                memory[message.chat.id].hangman = [word.upper(), list('_' * len(word)), 6]
            await bot.send_message(message.chat.id, f'''{' '.join(memory[message.chat.id].hangman[1])}''')
        elif memory[message.chat.id].hangman[-1]:
            memory[message.chat.id].hangman[-1] -= 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            if len(message.text) != 1:
                await bot.send_message(message.chat.id, f'''Ошибка ввода. -1 попытка.''', reply_markup=markup)
            elif message.text.upper() in memory[message.chat.id].hangman[1]:
                await bot.send_message(message.chat.id, 'Вы уже вводили это. -1 попытка.', reply_markup=markup)
            elif message.text.upper() in memory[message.chat.id].hangman[0]:
                memory[message.chat.id].hangman[-1] += 1
                for i in range(len(memory[message.chat.id].hangman[0])):
                    if memory[message.chat.id].hangman[0][i] == message.text.upper():
                        memory[message.chat.id].hangman[1][i] = message.text.upper()
                await bot.send_message(message.chat.id, 'Вы угадали букву.', reply_markup=markup)
            else:
                await bot.send_message(message.chat.id, 'Мимо. -1 попытка', reply_markup=markup)
            if memory[message.chat.id].hangman[-1] == 0 or '_' not in memory[message.chat.id].hangman[1]:
                await bot.send_message(message.chat.id, f'''Игра окончена.''', reply_markup=markup)
                await bot.send_message(message.chat.id, f'''Результат:''', reply_markup=markup)
                if '_' in memory[message.chat.id].hangman[1]:
                    if memory[message.chat.id].money <= 0:
                        await bot.send_message(message.chat.id,
                                               f'Из-за штрафов вас приговорили к общественным работам.')
                        await bot.send_message(message.chat.id, f'Вы будете заняты до 6:24')
                        memory[message.chat.id].ban = True
                    else:
                        await bot.send_message(message.chat.id, f'''Вы проиграли
Правильный ответ был: {memory[message.chat.id].hangman[0].capitalize()}. -10$''', reply_markup=markup)
                        memory[message.chat.id].hangman = 0
                        memory[message.chat.id].money -= 10
                else:
                    await bot.send_message(message.chat.id, f'''Вы выиграли! +40$''', reply_markup=markup)
                    if memory[message.chat.id].hangman[0] == 'КОШКА':
                        await bot.send_photo(
                            message.chat.id,
                            request('GET', url='https://api.thecatapi.com/v1/images/search').json()[0]['url']
                        )
                        await bot.send_message(message.chat.id, 'Ну разве они не милашки?')
                    elif memory[message.chat.id].hangman[0] == 'СОБАКА':
                        await bot.send_photo(
                            message.chat.id,
                            request('GET', url='https://dog.ceo/api/breeds/image/random').json()['message']
                        )
                        await bot.send_message(message.chat.id, 'Ну разве они не милашки?')
                    memory[message.chat.id].money += 40
                await menu(message)
            else:
                await bot.send_message(message.chat.id, f'''{' '.join(memory[message.chat.id].hangman[1])}''')
    memory[message.chat.id].update_info(meta, conn)


async def main():
    load_from_db(meta)
    await gather(create_task(bot.polling(non_stop=True)), create_task(cool_down()))
    print('error')


run(main())
