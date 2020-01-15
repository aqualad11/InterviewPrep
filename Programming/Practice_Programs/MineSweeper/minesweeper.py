import random

class MineSweeper():

	def __init__(self, col, row):
		self.rendered_field = []
		self.field = []
		self.cols = col
		self.rows = row
		self.pseudo_init_field()
		self.render_field()

	# Initializes an emoty field
	def pseudo_init_field(self):
		for r in range(self.rows):
			self.field.append([' ' for i in range(self.cols)])

	# Initalizes field after first move
	def init_field(self):
		bombs = 0
		exp_bombs = (self.cols * self.rows) // 10
		while(bombs < exp_bombs):
			row = random.random() * (self.rows-1)
			col = random.random() * (self.cols-1)
			if(self.field[row][col] != 'B'):
				self.field[row][col] = 'B'
				bombs += 1



	def validate_input(self,row,col):
		if(row < 0 or col < 0 or row > self.rows-1 or col > self.cols-1):
			return False
		return True

	def render_field(self):
		field = '   '
		floor = field

		for i in range(self.cols):
			field += str(i) + ' '
			floor += '- ' 

		field += '\n'
		field += floor

		for r in range(self.rows):
			field += str(r) + ' |'
			for c in self.field[r]:
				field += str(c) + '|'

			field += '\n'
			field += floor
			field += '\n'

		print(field)


	def open_pos(self, row, col):
		if not validate_input(row,col):
			return False


