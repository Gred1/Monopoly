from User import User
from vk_methods import VkMethods
from Connection import Connect
import random

class Monopoly:
	"""docstring for Monopoly"""
	def __init__(self, id_lobby, id_users, move_players, vk):

		self.move_players = move_players # определяет, какого игрока ход
		self.id_users = id_users
		self.hai = "Привет, Лобби "
		self.id_lobby = id_lobby # ID лобби в котором находится игрок
		self.NEXT_INPUT = "get_command" # Следующая команда для пользователя
		self.COMMANDS = [
						["БРОСИТЬ КУБИКИ"] # 0
					]
		self.i = 0
		self.count_players = len(self.id_users)

		# типы корпораций: 1 - ы
		# ключ : [Название, Владелец, Тип корпорации, уровень филиала]
		self.map = { 
			0 : ["start", 0, 0, 0],

			1 : ["CHANEL", 0, 1, 0],
			2 : ["event", 0, 1, 0],
			3 : ["BOSS", 0, 1, 0],
			4 : ["tax", 0, 1, 0],
			5 : ["MERS", 0, 11, 0],
			6 : ["ADIDAS", 0, 2, 0],
			7 : ["event", 0, 1, 0],
			8 : ["PUMA" , 0, 2, 0],
			9 : ["LACOSTE" , 2, 1, 0],
			10 : ["jail" , 0, 1, 0],

			11 : ["VK" , 0, 3, 0],
			12 : ["ROCKSTAR" , 0, 22, 0],
			13 : ["FACEBOOK" , 0, 3, 0],
			14 : ["TWITTER" , 0, 3, 0],
			15 : ["AUDI" , 0, 11, 0],
			16 : ["COCA-COLA" , 4, 1, 0],
			17 : ["event" , 0, 1, 0],
			18 : ["PEPSI"  , 0, 4, 0],
			19 : ["FANTA" , 0, 4, 0],
			20 : ["casino" , 0, 1, 0],

			21 : ["Columbia" , 0, 5, 0],
			22 : ["event", 0, 1, 0],
			23 : ["GUCCI", 0, 5, 0],
			24 : ["TOYOTA", 0, 5, 0],
			25 : ["FORD", 0, 11, 0],
			26 : ["MACDONALDS", 0, 6, 0],
			27 : ["BURGERKING", 0, 6, 0],
			28 : ["ROVIO", 0, 22, 0],
			29 : ["KFC", 0, 6, 0],			
			30 : ["jail", 0, 0, 0],

			31 : ["MOTOROLLA", 0, 7, 0],
			32 : ["LEVIS", 0, 7, 0],
			33 : ["event", 0, 1, 0],
			34 : ["NOVOTEL", 0, 7, 0],
			35 : ["LAND-ROVER", 0, 11, 0],
			36 : ["tax", 0, 0, 0],
			37 : ["APPLE", 0, 8, 0],
			38 : ["event", 0, 1, 0],
			39 : ["NOKIA", 0, 8, 0],
		}
		self.user = {}

		self.vk_methods = VkMethods(vk) 
		for i in range(len(self.id_users)):
			self.user[self.id_users[i]] = User(self.id_users[i], self.id_lobby ) 

	def counterMove(self):
		if self.i == self.count_players-1:
			self.i = 0
		else:
			self.i = self.i + 1

	def get_command(self, command, user_id):
		if self.COMMANDS[0][0] == command:
			text = 'Ход: ' + self.vk_methods.getNameById(self.move_players)
			self.vk_methods.sendMessageAll(self.id_users, text)

			text, summa_dice = self.rollDice()
			self.vk_methods.sendMessageAll(self.id_users, text)


			self.counterMove() # даем ход следующему игроку
			self.move_players = self.id_users[self.i] # даем ход следующему игроку

			self.mesAboutNextMove()

			next_input = self.user[user_id].returnNextMove()
			print(next_input)

			return False
		else:
			return "Не понял"

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
		self.vk_methods.sendMessageAll(self.id_users, text2)

	def removePlayerFromLobby(self, id_user):
		self.id_users.remove(id_user)
		self.count_players = len(self.id_users)

	def playersSuicide(self, user_id):
		text = "Все игроки покончили с собой!\nПобедитель: " + self.vk_methods.getNameById(self.id_users[0])
		self.vk_methods.sendMessageAll(self.id_users, text)
		self.removePlayerFromLobby(user_id)

	def update_screen(self, input_value, user_id):
		if input_value == "ВЫХОД ИЗ ИГРЫ": # удаляем пользователя из игры
			self.removePlayerFromLobby(user_id)
			print(self.id_users)
			self.vk_methods.sendMessageAll(self.id_users, "Игрок " + self.vk_methods.getNameById(user_id) + " вышел")

			if (user_id == self.move_players): # если выходит пользователь, который ходит
				self.move_players = self.id_users[self.i]

			self.mesAboutNextMove()

			if (self.count_players == 1): # если не осталось игроков - выводим поздравления
				self.playersSuicide(user_id)

			return "Вы вышли из игры, не выдержав капиталистический гнет"

		elif self.NEXT_INPUT == "get_command" and self.isMovePlayers(user_id) == True: # выполняем действие
			return self.get_command(input_value, user_id)
		else:
			return "Сейчас не ваш ход"
