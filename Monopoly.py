from User import User
from vk_methods import VkMethods
from Connection import Connect
import random

class Monopoly:
	"""docstring for Monopoly"""
	def __init__(self, id_lobby, id_users, move_players, vk):

		self.now_player = ''

		self.move_players = move_players # определяет, какого игрока ход
		self.id_users = id_users
		self.hai = "Привет, Лобби "
		self.id_lobby = id_lobby # ID лобби в котором находится игрок
		self.NEXT_INPUT = "get_command" # Следующая команда для пользователя
		self.COMMANDS = [
						["БРОСИТЬ КУБИКИ"], # 0
						["КУПИТЬ ПРЕДПРИЯТИЕ"],
						["НЕ ПОКУПАТЬ"]
					]
		self.i = 0
		self.count_players = len(self.id_users)
		self.button_sleep = "game_without.json"
		self.button = ''
		self.LAST_NEXT_INPUT = ''
		self.NEXT_INPUT_AND_BUTTON = {
				"get_command" : "game.json",
				"isBuy_command" : "isBuy.json"
		}

		# типы корпораций: 1 - ы
		# ключ : [Название, Владелец, Тип корпорации, уровень филиала, цена["price_to_buy" : цена, "price_to_build_branch" : цена, "price_branch" : [цена, цена, цена, цена, цена]]]
		self.map = { 
			0 : ["start", 0, 0, 0, 0],

			1 : ["МАГНИТ", 0, 1, 0, {"price_to_buy" : 50, "price_to_build_branch" : 50, "price_branch" : [1, 10, 30, 90, 200]}],
			2 : ["ПЯТЕРОЧКА", 0, 1, 0, {"price_to_buy" : 60, "price_to_build_branch" : 50, "price_branch" : [4, 15, 60, 180, 450]}],
			3 : ["moving", 0, 11, 0, 0],
			4 : ["АШАН", 0, 1, 0, {"price_to_buy" : 70, "price_to_build_branch" : 50, "price_branch" : [6, 20, 80, 200, 600]}],
			5 : ["charity", 0, 22, 0, 0],
			6 : ["ПЕРВЫЙ КАНАЛ", 0, 2, 0, {"price_to_buy" : 90, "price_to_build_branch" : 50, "price_branch" : [7, 30, 90, 250, 550]}],
			7 : ["РЕН ТВ", 0, 2, 0, {"price_to_buy" : 100, "price_to_build_branch" : 50, "price_branch" : [8, 40, 100, 300, 600]}],
			8 : ["event" , 0, 33, 0, 0],
			9 : ["BBC" , 0, 2, 0, {"price_to_buy" : 110, "price_to_build_branch" : 50, "price_branch" : [12, 50, 150, 350, 650]}],
			10 : ["jail" , 0, 0, 0, 0],

			11 : ["ADIDAS" , 0, 3, 0, {"price_to_buy" : 130, "price_to_build_branch" : 100, "price_branch" : [15, 60, 200, 400, 700]}],
			12 : ["PUMA" , 0, 3, 0, {"price_to_buy" : 140, "price_to_build_branch" : 100, "price_branch" : [20, 65, 210, 420, 750]}],
			13 : ["moving" , 0, 11, 0, 0],
			14 : ["NIKE" , 0, 3, 0, {"price_to_buy" : 150, "price_to_build_branch" : 100, "price_branch" : [21, 70, 220, 450, 800]}],
			15 : ["black_business" , 0, 44, 0, 0],
			16 : ["ALIEXSPRESS" , 0, 4, 0, {"price_to_buy" : 170, "price_to_build_branch" : 100, "price_branch" : [22, 75, 250, 500, 810]}],
			17 : ["BANGGOOD" , 0, 4, 0, {"price_to_buy" : 180, "price_to_build_branch" : 100, "price_branch" : [23, 80, 260, 550, 850]}],
			18 : ["event"  , 0, 33, 0, 0],
			19 : ["AVITO" , 0, 4, 0, {"price_to_buy" : 190, "price_to_build_branch" : 100, "price_branch" : [24, 85, 270, 600, 860]}],
			20 : ["casino" , 0, 0, 0, 0],

			21 : ["VK" , 0, 5, 0, {"price_to_buy" : 210, "price_to_build_branch" : 150, "price_branch" : [25, 90, 280, 610, 900]}],
			22 : ["moving", 0, 11, 0, 0],
			23 : ["TWITTER", 0, 5, 0, {"price_to_buy" : 220, "price_to_build_branch" : 150, "price_branch" : [30, 95, 290, 650, 950]}],
			24 : ["FACEBOOK", 0, 5, 0, {"price_to_buy" : 230, "price_to_build_branch" : 150, "price_branch" : [32, 100, 300, 700, 1000]}],
			25 : ["white_business", 0, 55, 0, 0],
			26 : ["SAMGUNG", 0, 6, 0, {"price_to_buy" : 250, "price_to_build_branch" : 150, "price_branch" : [35, 110, 310, 750, 1100]}],
			27 : ["event", 0, 33, 0, 0],
			28 : ["LG", 0, 6, 0, {"price_to_buy" : 260, "price_to_build_branch" : 150, "price_branch" : [36, 120, 350, 800, 1200]}],
			29 : ["APPLE", 0, 6, 0, {"price_to_buy" : 270, "price_to_build_branch" : 150, "price_branch" : [38, 130, 360, 850, 1250]}],			
			30 : ["jail", 0, 0, 0, 0],

			31 : ["STEAM", 0, 7, 0, {"price_to_buy" : 290, "price_to_build_branch" : 200, "price_branch" : [30, 140, 340, 900, 1300]}],
			32 : ["event", 0, 33, 0, 0],
			33 : ["UPLAY", 0, 7, 0, {"price_to_buy" : 300, "price_to_build_branch" : 200, "price_branch" : [40, 150, 400, 950, 1350]}],
			34 : ["ORIGIN", 0, 7, 0, {"price_to_buy" : 310, "price_to_build_branch" : 200, "price_branch" : [41, 160, 450, 1000, 1500]}],
			35 : ["black_business", 0, 44, 0, 0],
			36 : ["TOYOTA", 0, 8, 0, {"price_to_buy" : 330, "price_to_build_branch" : 200, "price_branch" : [44, 165, 500, 1200, 1700]}],
			37 : ["event", 0, 33, 0, 0],
			38 : ["BMW", 0, 8, 0, {"price_to_buy" : 340, "price_to_build_branch" : 200, "price_branch" : [45, 170, 600, 1400, 1901]}],
			39 : ["BENTLEY", 0, 8, 0, {"price_to_buy" : 350, "price_to_build_branch" : 200, "price_branch" : [50, 175, 700, 1500, 2000]}],
		}
		self.user = {}

		self.vk_methods = VkMethods(vk) 
		
		for i in range(len(self.id_users)):
			self.user[self.id_users[i]] = User(self.id_users[i], self.id_lobby ) 

	def counterMove(self):
		if self.i >= self.count_players-1:
			self.i = 0
		else:
			self.i = self.i + 1
		self.move_players = self.id_users[self.i] # даем ход следующему игроку

	def get_command(self, command, user_id):
		if self.COMMANDS[0][0] == command: # БРОСИТЬ КУБИКИ
			text = 'Ход: ' + self.vk_methods.getNameById(self.move_players) # Сообщение
			text1 = "Ваш ход"
			text2, summa_dice = self.rollDice() # ПОЛУЧАЕМ СЛУЧАЙНОЕ ЧИСЛО ОТ 2 до 12
			position = self.user[user_id].getPosition(summa_dice)
			print("клетка под номером: " + str(position))
			text2 = text2 + '\n' + " попадает на клетку с " + self.map[position][0]
			self.vk_methods.write_msg(self.move_players, text1, "game_without.json") # {ВАШ ХОД} - Сообщение для всех пользователей
			if (self.map[position][0] == "event"):
				self.vk_methods.sendMessageAll(self.id_users, text2, "game_without.json")
				self.vk_methods.sendMessageAllNoUser(self.id_users, "событие", user_id, "game_without.json") # - Сообщение для всех, кроме ходящего
				self.nextMove()
				return "Событие"
			else:
				self.vk_methods.sendMessageAll(self.id_users, text2, "game_without.json") # {КОСТИ} - Сообщение для всех пользователей
				self.vk_methods.sendMessageAllNoUser(self.id_users, "Задумывается о покупке бизнеса", user_id, "game_without.json")

				self.NEXT_INPUT, self.button = self.user[self.now_player].buyBusiness() # Направляем в функцию покупки бизнеса
				return "Купить бизнесс?"
		else:
			self.button = "game.json"
			return "Не понял"

	def AnswerBuyBusiness(self, command, user_id):
		if self.COMMANDS[1][0] == command: # покупаем бизнесс
			self.vk_methods.sendMessageAllNoUser(self.id_users, "Игрок купил предприятие",user_id, button="game_without.json")
			self.vk_methods.write_msg(user_id, "Вы купили предприятие", button="game_without.json")
			self.NEXT_INPUT, self.button = self.user[self.now_player].defaultValue()
			print(self.i)
			print(self.id_users)
			self.nextMove()
			print(self.i)
			return False
		elif self.COMMANDS[2][0] == command: # не покупаем бизнесс
			self.vk_methods.sendMessageAllNoUser(self.id_users, "Игрок не купил предприятие", user_id, button="game_without.json")
			self.vk_methods.write_msg(user_id, "Вы не купили предприятие", button="game_without.json")
			self.NEXT_INPUT, self.button = self.user[self.now_player].defaultValue()
			print(self.i)
			print(self.id_users)
			self.nextMove()
			print(self.i)
			return False
		else:
			self.button = self.user[self.now_player].button
			return "Не понял1"

	def nextMove(self):
		self.counterMove() # даем ход следующему игроку
		self.mesAboutNextMove()

	def rollDice(self):
		one = random.randint(1, 6)
		two = random.randint(1, 6)
		summa_dice = one + two
		text = "Выпало " + str(one) + ":" + str(two)
		return text, summa_dice

	def isMovePlayers(self, user_id): # Проверяет чтобы ходил тот игрок, которому дали ход
		if not self.move_players == user_id:
			return False
		else:
			return True

	def mesAboutNextMove(self): # уведомляет пользователей, кто будет ходить следующим
		text2 = 'Следующий ход делает ' + self.vk_methods.getNameById(self.move_players)
		text3 = 'Ваш ход'
		self.vk_methods.write_msg(self.move_players, text3, "game.json")
		self.vk_methods.sendMessageAllNoUser(self.id_users, text2, self.move_players, "game_without.json")

	def removePlayerFromLobby(self, id_user):
		self.id_users.remove(id_user)
		self.count_players = len(self.id_users)

	def playersSuicide(self, user_id):
		text = "Все игроки покончили с собой!\nПобедитель: " + self.vk_methods.getNameById(self.id_users[0])
		self.vk_methods.sendMessageAll(self.id_users, text)
		self.removePlayerFromLobby(self.id_users[0])

	def exitFromGame(self, user_id):
		last_players = False # если выходит последний игрок
		if user_id == self.id_users[self.count_players-1]:
			last_players = True

		self.vk_methods.sendMessageAllNoUser(self.id_users, "Игрок " + self.vk_methods.getNameById(user_id) + " вышел", user_id)
		self.removePlayerFromLobby(user_id)
		if (user_id == self.move_players): # если выходит пользователь, который ходит
			if last_players == True:
				self.move_players = self.id_users[0]
				self.i = 0
			else:
				self.move_players = self.id_users[self.i]

			text = 'Следующий ход делает ' + self.vk_methods.getNameById(self.move_players)
			self.vk_methods.write_msg(self.move_players, "Ваш ход", "game.json")
			self.vk_methods.sendMessageAllNoUser(self.id_users, text, self.move_players, "game_without.json")
		else:
			text = 'Следующий ход делает ' + self.vk_methods.getNameById(self.move_players)
			self.vk_methods.write_msg(self.move_players, "Ваш ход", self.NEXT_INPUT_AND_BUTTON[self.NEXT_INPUT])
			self.vk_methods.sendMessageAllNoUser(self.id_users, text, self.move_players, "game_without.json")

		if (self.count_players == 1): # если не осталось игроков - выводим поздравления
			self.playersSuicide(user_id)

		self.button = "null.json"
		return "Вы вышли из игры, не выдержав капиталистический гнет"

	def update_screen(self, input_value, user_id):

		if input_value == "ВЫХОД ИЗ ИГРЫ": # удаляем пользователя из игры
			return self.exitFromGame(user_id)

		self.now_player = user_id
		self.NEXT_INPUT = self.user[self.now_player].NEXT_INPUT1

		if self.NEXT_INPUT == "get_command" and self.isMovePlayers(user_id) == True: # выполняем действие
			return self.get_command(input_value, user_id)

		elif self.NEXT_INPUT == "isBuy_command" and self.isMovePlayers(user_id) == True:
			return self.AnswerBuyBusiness(input_value, user_id)

		else:
			return "Сейчас не ваш ход"
