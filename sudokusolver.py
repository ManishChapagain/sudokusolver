def solve(puzzle):
	find = find_empty(puzzle)
	if not find:
		return True
	else:
		row , col = find

	for z in range(1,10):
		puzzle[row][col] = z

		if valid(puzzle,row,col) != True:
			puzzle[row][col] = 0

		else:
			if solve(puzzle):
				return True

			puzzle[row][col] = 0

	return False


def valid(puzzle,row,column):
	if check_horizontal(puzzle,row,column) != 0 and check_vertical(puzzle,row,column) != 0 and check_box(puzzle,row,column) != 0:
		return True


def check_horizontal(puzzle,row,column):
	for x in range(9):
		if puzzle[row][column] == puzzle[row][x] and x != column:
			return 0

def check_vertical(puzzle,row,column):
	for x in range(0,9):
		if puzzle[row][column] == puzzle[x][column] and x != row:
			return 0

def check_box(puzzle,row,column):
	a = row // 3
	b = column // 3

	for x in range(a*3,3+a*3):
		for y in range(b*3,3+b*3):
			if puzzle[row][column] == puzzle[x][y] and x != row and y != column :
				return 0

def find_empty(puzzle):
	for x in range(9):
		for y in range(9):
			if puzzle[x][y] == 0:
				return (x,y)
	return None

def main():
	puz = [[3,7,0,0,0,1,0,0,0],
		   [0,0,0,9,0,2,0,0,0],
		   [0,0,0,0,0,6,5,1,0],
		   [0,0,2,0,0,0,6,4,0],
		   [1,9,0,0,0,0,0,0,0],
		   [0,4,0,0,0,9,0,2,0],
		   [0,0,4,0,0,0,1,5,0],
		   [0,0,0,8,0,0,0,0,0],
		   [6,0,0,5,0,0,7,0,0]]
	solve(puz)
	for each in puz:
		print (each)
main()


