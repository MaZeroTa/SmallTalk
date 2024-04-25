from FCl import *


class User:
    def __init__(self, name, iid, meta, conn):
        query = meta.tables['user'].select().where(meta.tables['user'].columns.chat_id == iid)
        result = conn.execute(query)
        user_info = list(i for i in result)
        if len(user_info) != 0:
            user_info = user_info[0]
        else:
            query = meta.tables['user'].insert().values(chat_id=iid, username=name,
                                                        time=time.strftime("%Y-%m-%d %H:%M",
                                                                           time.localtime(time.time())))
            conn.execute(query)
            conn.commit()
            query = meta.tables['user'].select().where(meta.tables['user'].columns.chat_id == iid)
            result = conn.execute(query)
            user_info = list(i for i in result)[0]
        # УРААААААААААА :D

        print(user_info)  # проверочка инфо
        self.id = iid
        self.name = user_info[1]
        self.girl_name = user_info[2]
        self.score = user_info[4]
        self.money = user_info[3]
        self.inventory = {'Цветы': user_info[6], 'Кольцо': user_info[7], 'Шоколад': user_info[8]}
        self.cool_down_data = {'Цветы': 5, 'Кольцо': 2, 'Шоколад': 10}
        self.gift_mode = False
        self.store_mode = False
        self.change_name_mode = 0
        self.time_start = user_info[5]
        self.work = False
        self.count_of_message = 0
        self.ban = False
        self.sociable = False
        self.sociable_mode = False
        self.sociable_const = False
        self.rulet = 0
        self.blackjack = 0
        self.blackjack_money = 0
        self.blackjack_game = 0
        self.blackjack_card_player = []
        self.blackjack_card_dealer = []
        self.hangman = 0
        self.god_mod = 0
        self.mini_game_mode = False
        self.variables = {'deck': list(
            product(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз'],
                    ['Черви', 'Трефы', 'Пики', 'Буби'])),
            'store_player': 0,
            'store_dealer': 0,
            'money': 0,
            'card_player': [],
            'card_dealer': []}

        self.value_card = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Валет': 10,
            'Дама': 10,
            'Король': 10,
            'Туз': 11}

    def get_data(self):
        text = f'''
Имя: {self.name}
Деньги: {self.money}$
Отношения: {self.score}
Вы с нами с {self.time_start}
'''
        return text

    def get_inventory(self):
        text = ''
        for elem in self.inventory:
            text += elem + ' - ' + str(self.inventory[elem]) + '\n'
        return text

    def cool_down(self):
        self.cool_down_data = {'Цветы': 5, 'Кольцо': 2, 'Шоколад': 10}
        self.ban = False

    def spam_defense(self):
        if self.count_of_message > 3 and not self.ban:
            self.ban = True
            return True

    def update_info(self, meta, conn):
        query = meta.tables['user'].update().where(meta.tables['user'].columns.chat_id == self.id).values(
            ring=self.inventory['Кольцо'],
            flower=self.inventory['Цветы'],
            choco=self.inventory['Шоколад'],
            username=self.name,
            score=self.score,
            money=self.money,
            girlname=self.girl_name,
            time=self.time_start
        )
        conn.execute(query)
        conn.commit()
