from vk_methods import VkMethods

class Connect:

	def __init__(self, lobby):
		self.lobby = lobby
		self.i = 0
		self.players_r = ''
		self.k = 1

	def isUserInLobby(self, lobby, user_id):
		k = 0
		for i in range(len(lobby)):
			for j in range(len(lobby[i][0])):
				if user_id == lobby[i][0][j]:
					k = k+1
		if k == 0:
			return True
		else:
			return False

	
	def AddUserInLobby(self, user_id, vk):
		text = ''
		vk_methods = VkMethods(vk)
		name = vk_methods.getNameById(user_id)   

		if not self.isUserInLobby(self.lobby, user_id):
			text = "Вы уже в лобби"
			return text, self.lobby[self.i], self.i
		else:
			self.lobby[self.i][0].append(user_id)
			if len(self.lobby[self.i][0]) == 3:

				text = "Вы в лобби. Лобби заполнено\n"
				text = text + vk_methods.getNameByIdAllUsersInLobby(self.lobby[self.i])

				text2 = "Подключился " + name + '\n'
				text2 = text2 + "Лобби заполнено\n" + vk_methods.getNameByIdAllUsersInLobby(self.lobby[self.i])
				vk_methods.sendMessageAllNoUser(self.lobby[self.i][0], text2, user_id)

				self.lobby[self.i][1] = 1
				self.lobby.append([[], 0])
				self.i = self.i + 1

				self.players_r = ''
				print(self.lobby)

				return text, self.lobby[self.i-1], self.i-1
			else:

				text = "Вы в лобби. Ждите подключения других игроков...\n"
				text = text + vk_methods.getNameByIdAllUsersInLobby(self.lobby[self.i])

				text2 = "Подключился " + name + '\n'
				text2 = text2 + vk_methods.getNameByIdAllUsersInLobby(self.lobby[self.i])
				vk_methods.sendMessageAllNoUser(self.lobby[self.i][0], text2, user_id)
				print(self.lobby)

				return text, self.lobby[self.i], self.i




	def getLobbyByIdUser(self, user_id):
		for i in range(len(self.lobby)):
			for j in range(len(self.lobby[i][0])):
				if user_id == self.lobby[i][0][j]:
					return self.lobby[i], i
		return False, False



	def deleteUserFromLobby(self, user_id):
		self.lobby[self.i][0].remove(user_id)


	def AddUserInLobbyFind(self, user_id, vk):
		text, lobby, i = self.AddUserInLobby(user_id, vk)
		button = 'cancel.json'
		vk_methods = VkMethods(vk)
		vk_methods.write_msg(user_id, text, button)

		if lobby[1] == 1: # ЛОББИ ГОТОВО, НАЧИНАЕМ ИГРУ
			text = "ДА НАЧНЕТСЯ МОНОПОЛИЯ!\n\n"
			text = text + vk_methods.getNameByIdAllUsersInLobby(lobby) + '\n'
			first = vk_methods.getNameById(self.lobby[self.i-1][0][0])
			text = text + 'Первым ходит ' + first
			button = 'game.json'

			vk_methods.sendMessageAll(lobby[0], text, button="game.json")
			print(i)
			print("Если")
			return lobby, i, self.lobby[self.i-1][0][0]
		else:
			print(i)
			print("Иначе")
			return [0,0], i, 0

	def cancelSearchUsers(self, user_id, is_active, name, vk):
		self.deleteUserFromLobby(user_id)
		vk_methods = VkMethods(vk)
		text = name + " отменил поиск\n"
		text = text + vk_methods.getNameByIdAllUsersInLobby(is_active)
		button = 'keyboard.json'

		vk_methods.write_msg(user_id, 'Вы отменили поиск', button)
		vk_methods.sendMessageAllNoUser(is_active[0], text, user_id)