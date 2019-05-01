class User:

	def __init__(self, user_id, lobby_id):
		self.id = user_id
		self.lobby_id = lobby_id
		self.money = 2000
		self.position = 0
		self.NEXT_INPUT1 = "get_command"
		self.button = "game_without.json"
		self.property = []

	def defaultValue(self):
		self.NEXT_INPUT1 = "get_command"
		self.button = "game_without.json"
		return self.NEXT_INPUT1, self.button

	def buyBusiness(self):
		self.NEXT_INPUT1 = 'isBuy_command'
		self.button = "isBuy.json"
		return self.NEXT_INPUT1, self.button

	def getPosition(self, num_move):
		self.position = self.position + num_move
		if (self.position > 39):
			self.position = self.position - 40
		return self.position

	def getRent(self):
		self.NEXT_INPUT1 = 'rent_command'
		self.button = "rent.json"
		return self.NEXT_INPUT1, self.button

	def game(self):
		self.button = "game.json"
		self.NEXT_INPUT1 = "get_command"
		return self.NEXT_INPUT1, self.button

		