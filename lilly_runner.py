import vk_api
from lilly import Lilly
from vk_api.longpoll import VkLongPoll, VkEventType
import config
import random
from Connection import Connect
from vk_methods import VkMethods
from Monopoly import Monopoly
from User import User



# Авторизуемся как сообщество
vk = vk_api.VkApi(token=config.token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Словарь, где будут хранится разные объекты бота для разных пользователей

def run():
    print("Server started")
    i = 0

    monopoly = {}
    user = {}

    lobby = [[[], 0]]
    connect = Connect(lobby)
    button = "keyboard.json"


    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:


                print('New message:')
                print('For me by: ', end='')
                print(event.user_id)

                user_id = event.user_id
                mes_user = event.text.upper()

                vk_methods = VkMethods(vk)
                name = vk_methods.getNameById(user_id)
                is_active, i_user = connect.getLobbyByIdUser(user_id)

                print(name)
                print()

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
                            monopoly[i] = Monopoly(i, lobby[0], first_id, vk)
                            print('ДА')
                        else:
                            print('НЕТ')

                    else:
                        users_bot_class_dict = Lilly()
                        text = users_bot_class_dict.update_screen(mes_user)
                        vk_methods.write_msg(event.user_id, text, button="keyboard.json")

                else:
                    if is_active[1] == 1: # КОД ОСНОВНОЙ ИГРЫ
                        text = "Да начнется Монополия\n"
                        button = "game.json"
                        text = monopoly[i_user].update_screen(mes_user, user_id)
                        button = monopoly[i_user].button
                        print(button)
                        if not text == False:
                            vk_methods.write_msg(event.user_id, text, button)

                    elif mes_user == 'ОТМЕНИТЬ ПОИСК':
                        connect.cancelSearchUsers(user_id, is_active, name, vk)

                    else:
                        text = "Ожидайте подключения других игроков!"
                        vk_methods.write_msg(event.user_id, text, button)

                print('Text:', mes_user)
                print()




print("Lilly_Test is ready")
