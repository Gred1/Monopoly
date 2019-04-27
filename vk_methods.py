import random

class VkMethods:
	def __init__(self, vk):
		self.vk = vk

	def write_msg(self, user_id, s, button='null.json'):
		self.vk.method('messages.send', {'peer_id': user_id, "random_id": random.randrange(1,30000, 1), 'message': s, "keyboard":open(button, "r", encoding="UTF-8").read()})

	def sendOnlyButton(self, user_id, button):
		self.vk.method('messages.send', {'peer_id': user_id, "random_id": random.randrange(1,30000, 1), "keyboard":open(button, "r", encoding="UTF-8").read()})

	def getNameById(self, user_id):
		return self.vk.method('users.get', {'user_ids' : user_id})[0]['first_name']

	def getNameByIdAllUsersInLobby(self, lobby):
		k = 1
		text = ''
		for i in range(len(lobby[0])):
			text = text + str(k) + ") " + self.getNameById(lobby[0][i]) + '\n'
			k = k + 1
		return "Участники: \n" + text

	def sendMessageAllNoUser(self, users, s, user_id, button="null.json"):
		for i in range(len(users)):
			if users[i] == user_id:
				continue
			else:
				user_ids = users[i]
				self.vk.method('messages.send', {'peer_id': user_ids, "random_id": random.randrange(1,30000, 1), 'message': s, "keyboard":open(button, "r", encoding="UTF-8").read()})

	def sendMessageAll(self, users, s, button="null.json" ):
		for i in range(len(users)):
			user_ids = users[i]
			self.vk.method('messages.send', {'peer_id': user_ids, "random_id": random.randrange(1,30000, 1), 'message': s, "keyboard":open(button, "r", encoding="UTF-8").read()})