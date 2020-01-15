class Spreadsheet():
	def __init__(self, rows, cols):
		self.sheet = []
		for r in range(rows):
			self.sheet.append(['' for i in range(cols)])

	def print_sheet(self):
		for row in self.sheet:
			line = ''
			for cell in row:
				line += str(cell) + '|'
			line = line[:len(line)-1]
			print(line)

	def pretty_print(self):

		max_cols = [0 for i in range(len(self.sheet[0]))]

		for col in range(len(self.sheet[0])):
			for r in range(len(self.sheet)):
				if(len(self.sheet[r][col]) > max_cols[col]):
					max_cols[col] = self.sheet[r][col]

		for row in self.sheet:
			line = ''
			for i in range(len(row)):
				line += str(row[i])
				line.ljust(max_cols[i], ' ')
				line += '|'
			line = line[:len(line)-1]
			print(line)

	def enter_cell(self, row, col, content):
		if(self.validate_val(row,col)):
			self.sheet[row][col] = content

	def validate_val(self, row, col):
		if(row < 0 or col < 0 or row > len(self.sheet) or col > len(self.sheet[0])):
			return False
		return True


ss = Spreadsheet(4,3)
ss.enter_cell(0,0, 'bob')
ss.enter_cell(0,1,10)
ss.enter_cell(0,2,'foo')
ss.enter_cell(1,0,'alice')
ss.enter_cell(1,1,5)
ss.pretty_print()