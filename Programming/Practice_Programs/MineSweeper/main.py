import sys
from minesweeper import MineSweeper

if __name__ == '__main__' :
	ms = MineSweeper(10,10)
	quit = False

	while(not quit):
		print('Enter position you want to reveal.')
		pos = input().split()

		
