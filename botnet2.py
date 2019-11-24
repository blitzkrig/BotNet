import vk
import os
import time
import random
import vk_api
import requests
#from func import funcs
from data import botnetdata3
from threading import Thread
from colorama import Fore, init, Style, Back
from vk_api.longpoll import VkLongPoll, VkEventType
init(autoreset=False)
print('\nstart botnet\n')
time.sleep(1)
botx = 1
class admbot: #admin bot
    def captcha_handler(captcha):
        key = ImageToTextTask.ImageToTextTask(anticaptcha_key='ключ антикапчи', save_format='const') \
            .captcha_handler(captcha_link=captcha.get_url())
        return captcha.try_again(key['solution']['text'])
    def __init__(self):
        self.num = botx
        time.sleep(botx)
        self.name = botnetdata3.bots_info[self.num]['name'] #берем данные из файла
        self.bot_id = botnetdata3.bots_info[self.num]['bot_id']
        self.token = botnetdata3.bots_info[self.num]['token']
        session = vk_api.VkApi(token=self.token, captcha_handler=captcha_handler) #авторизация
        longpoll = VkLongPoll(session)
        vk = session.get_api()
        print(Fore.CYAN + 'admbot connected!')
        bot_id = vk.users.get()[0]["id"]
        for event in longpoll.listen():
            if event.type == VkEventType.CHAT_UPDATE:
                if event.type_id == 8:
                    x = event.info["user_id"]
                    y = event.chat_id
                    try:                                                                               
                        vk.messages.addChatUser(
                        chat_id=event.chat_id,
                        user_id=x
                        )    
                    except Exception as errmsg:
                        with open('log.txt', 'a', encoding = 'utf-8') as f:
                            f.write(str(errmsg) + '\n')
                elif event.type_id == 6:
                    botnetdata3.bots_sms = botnetdata3.bots_sms + 4
                    if event.info["user_id"] == name and botnetdata3.blitzkrieg == True:
                        try:
                            vk.execute(
                            code = "var ch_id = " + str(event.chat_id) + "; var x = 5; while (x > 0) { API.messages.send({message:'" + str(botnetdata3.raid_msg) + "',chat_id:ch_id,attachment:'wall-183828650_92',random_id:0}); x = x -1 ;}"
                            )
                        except vk_api.exceptions.ApiError:
                            q = 0
            elif event.from_chat:
                botnetdata3.bots_requests = botnetdata3.bots_requests + 1
                try:
                    st = event.text.lower()
                except AttributeError:
                    st = 'нет текста'
                else:
                    if st.startswith('/start') and (event.user_id == botnetdata3.useradmin):
                        код
                        else:
                            try:
                                код
                            except vk_api.exceptions.ApiError:
                                q = 0
                    elif код
class bot:
    def __init__(self):
        self.num = botx + 1
        time.sleep(botx)
        self.name = botnetdata3.bots_info[self.num]['name']
        self.bot_id = botnetdata3.bots_info[self.num]['bot_id']
        self.token = botnetdata3.bots_info[self.num]['token']
        session = vk_api.VkApi(token=self.token)
        longpoll = VkLongPoll(session)
        vk = session.get_api()
        print(Fore.CYAN + str(self.num) + ' bot connected!')
        bot_id = vk.users.get()[0]["id"]
        for event in longpoll.listen():
            if event.type == VkEventType.CHAT_UPDATE:
                if event.type_id == 8:
                    x = event.info["user_id"]
                    y = event.chat_id
                    try:                                                                               
                        vk.messages.addChatUser(
                        chat_id=event.chat_id,
                        user_id=x
                        )    
                    except Exception as errmsg:
                        with open('log.txt', 'a', encoding = 'utf-8') as f:
                            f.write(str(errmsg) + '\n')
                elif event.type_id == 6:
                    botnetdata3.bots_sms = botnetdata3.bots_sms + 4
                    if event.info["user_id"] == name and botnetdata3.blitzkrieg == True:
                        try:
                            vk.execute(
                            code = "var ch_id = " + str(event.chat_id) + "; var x = 5; while (x > 0) { API.messages.send({message:'" + str(botnetdata3.raid_msg) + "',chat_id:ch_id,attachment:'wall-183828650_92',random_id:0}); x = x -1 ;}"
                            )
                        except vk_api.exceptions.ApiError:
                            q = 0
            elif event.from_chat:
                botnetdata3.bots_requests = botnetdata3.bots_requests + 1
                try:
                    st = event.text.lower()
                except AttributeError:
                    st = 'нет текста'
                else:
                    if st.startswith('/start') and (event.user_id == botnetdata3.useradmin):
                        код
                    elif st.startswith('start') and (event.user_id == botnetdata3.useradmin):
                        код

bots = []
class MyThread(Thread): # объекты класса суем в список и запускаем поочередно
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    def run(self):
        bots.append(bot())

thread = []
for botx in range(len(botnetdata3.bots_info) - 1):
    name = 'bot ' + str(botx + 1)
    thread.append(MyThread(name))
    thread[botx].start()

if __name__ == '__main__':
    time.sleep(3)
    admbot() # запуск admin bota