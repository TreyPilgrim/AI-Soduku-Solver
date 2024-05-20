# Sudoku

import random

def createBoard(diff):
	row0 = [0] * 9
	row1 = [0] * 9
	row2 = [0] * 9
	row3 = [0] * 9
	row4 = [0] * 9
	row5 = [0] * 9
	row6 = [0] * 9
	row7 = [0] * 9
	row8 = [0] * 9

	board = [row0, row1, row2, row3, row4, row5, row6, row7, row8]
	helpers = 0
	counter = 0
	if diff == 1: # Easy mode
		helpers = random.randint(15, 21) # How many boxes will be filled in
		
		while counter < helpers:
		
			goodNums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Options
			val = random.choice(goodNums) # Number selected
			
			# Select a random box on the board
			row = random.randint(0, 8)
			col = random.randint(0, 8) 
			
			if not valid(board, val, (row, col)):
				continue # try again @ a new spot
			else:
				# Update the board and increment the counter if valid
				board[row][col] = val
				counter += 1
			
				
	elif diff == 2: # Medium mode
		helpers = random.randint(10, 15) # How many boxes will be filled in
		
		while counter < helpers:
		
			goodNums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Options
			val = random.choice(goodNums) # Number selected
			
			# Select a random box on the board
			row = random.randint(0, 8)
			col = random.randint(0, 8) 
			
			if not valid(board, val, (row, col)):
				continue # try again @ a new spot
			else:
				# Update the board and increment the counter if valid
				board[row][col] = val
				counter += 1
				
				
	elif diff == 3: # Hard Mode
		helpers = random.randint(7, 10) # How many boxes will be filled in
		
		while counter < helpers:
		
			goodNums = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Options
			val = random.choice(goodNums) # Number selected
			
			# Select a random box on the board
			row = random.randint(0, 8)
			col = random.randint(0, 8) 
			
			if not valid(board, val, (row, col)):
				continue # try again @ a new spot
			else:
				# Update the board and increment the counter if valid
				board[row][col] = val
				counter += 1
				
	return board
	
def drawBoard(board):
	# Function prints the board that is passsed
	
	# "board" is a list of 9 lists. 1 List per 3x3 (each subproblem
	for i in range(9):
		
		print('  ' + str(board[i][0]) + ' ' + str(board[i][1]) + ' ' + str(board[i][2]) + ' | ' + str(board[i][3]) + ' ' + str(board[i][4]) + ' ' + str(board[i][5]) + ' | ' + str(board[i][6]) + ' ' + str(board[i][7]) + ' ' + str(board[i][8]))
		
		if i == 2 or i == 5:
			print("-------------------------")
	i = 0
	

def valid(board, val, pos):
	# Determine if a move is valid
	
	# Check Rows
	for i in range(len(board[0])):
		if board[pos[0]][i] == val and pos[1] != i:
			return False
		
	# Check Columns
	for i in range(len(board)):
		if board[i][pos[1]] == val and pos[0] != i:
			return False
	
	# Check Box
	box_x = pos[1] // 3
	box_y = pos[0] // 3
	
	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x * 3 + 3):
			if board[i][j] == val and (i,j) != pos:
				return False
				
	return True

def getNextEmpty(board):
	
	for row in range(9):
		for col in range(9):
			if board[row][col] == 0:
				coord = [row, col]
				return coord
	
	return None


def Solve(board):
	
	found = getNextEmpty(board)
	
	
	if found == None:
		return True
	
	row, col = found
	
	for i in range(1, 10):
		if(valid(board, i, (row, col))):
			board[row][col] = i
			
			
			if Solve(board):
				return True
				
			board[row][col] = 0
	
	return False
		
		
			
difficulty = 4
print("Welcome to Sodoku")

while difficulty > 3 or difficulty < 1:
	print("Which difficulty would you like the computer to solve?")
	print("1 - Easy\n2 - Medium\n3 - Hard\n")
	difficulty = int(input("\n"))
	

gameState = createBoard(difficulty)

print("Here is your new game!")
drawBoard(gameState)

if(Solve(gameState)):
	print("Winner!") 
	drawBoard(gameState)
else:
	print("Loser!")
	drawBoard(gameState)
































