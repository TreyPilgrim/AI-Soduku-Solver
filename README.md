# AI-Soduku-Solver (change to code view to see properly)
Backtracking Algorithm in Python

When the program is run it will prompt the user:
1 - Easy
2 - Medium
3 - Hard

Users will enter the number of choice. 
The game will then display the game board in its unsolved state.

Here is your new game!
  0 2 0 | 3 7 0 | 0 8 0
  5 0 0 | 0 0 8 | 0 0 0
  6 0 0 | 0 0 0 | 0 0 0
-------------------------
  0 0 2 | 0 0 0 | 0 4 0
  0 0 0 | 0 0 0 | 0 0 0
  0 0 5 | 0 3 0 | 0 0 0
-------------------------
  0 0 0 | 0 0 0 | 0 0 0
  0 0 0 | 7 6 3 | 8 0 0
  0 0 0 | 0 0 0 | 0 3 0
  
It will then compute the solution. If one is found, it will say:

Winner!
  1 2 4 | 3 7 5 | 6 8 9
  5 3 7 | 6 9 8 | 1 2 4
  6 8 9 | 1 2 4 | 3 5 7
-------------------------
  3 1 2 | 5 8 7 | 9 4 6
  4 6 8 | 2 1 9 | 5 7 3
  7 9 5 | 4 3 6 | 2 1 8
-------------------------
  8 5 3 | 9 4 1 | 7 6 2
  2 4 1 | 7 6 3 | 8 9 5
  9 7 6 | 8 5 2 | 4 3 1

In situations where a winning state cannot be found, the game will go as followed:
Here is your new game!
  6 0 0 | 9 0 0 | 0 8 0
  9 0 0 | 0 0 0 | 4 0 0
  0 2 0 | 0 0 0 | 0 3 0
-------------------------
  0 0 0 | 2 0 0 | 0 0 0
  0 0 7 | 0 0 6 | 0 9 0
  4 8 0 | 0 1 0 | 0 0 0
-------------------------
  2 0 0 | 0 0 9 | 0 0 0
  0 0 0 | 0 0 0 | 0 0 0
  0 0 5 | 0 4 0 | 0 0 1
Loser!
  6 0 0 | 9 0 0 | 0 8 0
  9 0 0 | 0 0 0 | 4 0 0
  0 2 0 | 0 0 0 | 0 3 0
-------------------------
  0 0 0 | 2 0 0 | 0 0 0
  0 0 7 | 0 0 6 | 0 9 0
  4 8 0 | 0 1 0 | 0 0 0
-------------------------
  2 0 0 | 0 0 9 | 0 0 0
  0 0 0 | 0 0 0 | 0 0 0
  0 0 5 | 0 4 0 | 0 0 1
