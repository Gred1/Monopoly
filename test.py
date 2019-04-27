x = 23

class FuncBly:
	def __init__(self):
		self.sasi = 2

	def func_my(self):
		global x
		print(x)
		x = 25

func = FuncBly()
func.func_my()

print(x)