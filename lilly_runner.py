import vk_api
from lilly import Lilly
from vk_api.longpoll import VkLongPoll, VkEventType
import config
import random
from Connection import Connect
from vk_methods import VkMethods
from Monopoly import Monopoly
from User import User
import time
import math



# Авторизуемся как сообщество
vk = vk_api.VkApi(token=config.token)

# Работа с сообщениями
timer = 0
# Словарь, где будут хранится разные объекты бота для разных пользователей

def everyTime(connect, monopoly):
    lobby_from_class_connect = connect.lobby
    for i in range(len(lobby_from_class_connect)):
        if lobby_from_class_connect[i][1] == 1:
            time_lobby = monopoly[i].timer

            time_lobby = math.floor(time_lobby+30)
            print(time_lobby)
            print(math.floor(time.time()))
            print()
            if time_lobby < math.floor(time.time()):
                monopoly[i].exitTime()
                print('игрок вылетел')
        if lobby_from_class_connect[i][1] == 1 and not lobby_from_class_connect[i][0]:
            connect.lobby.remove([[], 1])
            connect.i = connect.i - 1
            break

def run():
    print(vk_api.__file__)
    print("Server started")
    i = 0

    monopoly = {}
    user = {}

    lobby = [[[], 0]]
    connect = Connect(lobby)
    button = "keyboard.json"

    while True:

        everyTime(connect, monopoly) # проверяем, истекло ли время

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
        if messages["count"] >= 1:

            print('New message:')
            print('For me by: ', end='')

            user_id = messages["items"][0]["last_message"]["from_id"]
            mes_user = messages["items"][0]["last_message"]["text"].upper()

            vk_methods = VkMethods(vk)
            name = vk_methods.getNameById(user_id)
            is_active, i_user = connect.getLobbyByIdUser(user_id)

            if not is_active == False:
                mes = ''
                for i in range(len(is_active[0])):
                    mes = mes + str(is_active[0][i]) + ', '
                print("Участник состоит в лобби: " + str(i_user))
                print("Лобби: " + mes)

            if is_active == False: # ЕСЛИ ЛОББИ НЕ АКТИВНО - ПРОДОЛЖАЕМ ДОБАВЛЯТЬ ПОЛЬЗОВАТЕЛЕЙ

                if mes_user == 'НАЙТИ': # ИЩЕМ ЛОББИ
                    lobby, i, first_id = connect.AddUserInLobbyFind(user_id, vk)
                    print(lobby[1])
                    if lobby[1] == 1:
                        timer = time.time()
                        monopoly[i] = Monopoly(i, lobby[0], first_id, vk, timer)
                        print('ДА')
                    else:
                        print('НЕТ')

                else:
                    users_bot_class_dict = Lilly()
                    text = users_bot_class_dict.update_screen(mes_user)
                    vk_methods.write_msg(user_id, text, button="keyboard.json")

            else:
                if is_active[1] == 1: # КОД ОСНОВНОЙ ИГРЫ
                    text = "Да начнется Монополия\n"
                    button = "game.json"
                    text = monopoly[i_user].update_screen(mes_user, user_id)
                    button = monopoly[i_user].button
                    print(button)
                    if not text == False:
                        vk_methods.write_msg(user_id, text, button)

                elif mes_user == 'ОТМЕНИТЬ ПОИСК':
                    connect.cancelSearchUsers(user_id, is_active, name, vk)

                else:
                    text = "Ожидайте подключения других игроков!"
                    vk_methods.write_msg(user_id, text, button)

            print('Text:', mes_user)
            print()




print("Lilly_Test is ready")
