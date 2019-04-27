class User:

	def __init__(self, user_id, lobby_id):
		self.id = user_id
		self.lobby_id = lobby_id
		self.money = 2000
		self.position = 0
		self.NEXT_INPUT1 = "get_command"
		self.button = "game.json"

	def defaultValue(self):
		self.NEXT_INPUT1 = "get_command"
		self.button = "game.json"
		return self.NEXT_INPUT1, self.button

	def buyBusiness(self):
		self.NEXT_INPUT1 = 'isBuy_command'
		self.button = "isBuy.json"
		return self.NEXT_INPUT1, self.button
		