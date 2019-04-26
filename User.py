class User:

	def __init__(self, user_id, lobby_id):
		self.id = user_id
		self.lobby_id = lobby_id
		self.money = 15000
		self.position = 0
		self.NEXT_INPUT = "buyOrAu"
		
	def returnNextMove(self):
		return self.NEXT_INPUT