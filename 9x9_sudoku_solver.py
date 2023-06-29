import numpy as np
import copy
import re

'''
Puzzle Form:
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
_____________________
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
_____________________
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 0 0 | 0 0 0
'''

puzzle = np.zeros((9,9), dtype=int)
puzzle = np.ndarray.tolist(puzzle)

def initialize_puzzle():
    range_arr = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
         for k in range(9):
            if puzzle[i][k]==0:
                puzzle[i][k] = copy.deepcopy(range_arr)

def print_puzzle():
    for i in range(9):
        if i%3==0 and i!=0:
            print("______________________")
        line = ""
        for k in range(9):
            if k%3==0 and k!=0:
                line += "| "
            if type(puzzle[i][k]) is list:
                line += '0 '
            else:
                line += f'{float(puzzle[i][k]):g} '
        print(line)

def print_puzzle_with_guide():
    print("  A B C   D E F   G H I")
    for i in range(9):
        if i%3==0 and i!=0:
            print(" ______________________")
        line = str(i+1)+" "
        for k in range(9):
            if k%3==0 and k!=0:
                line += "| "
            line += f'{float(puzzle[i][k]):g} '
        print(line)

def check_col_contains_value(value, column):
    for i in range(9):
        if puzzle[i][column]==value:
            return True
    return False

def check_row_contains_value(value, row):
    if value in puzzle[row]:
        return True
    return False

def collapse_cells():
    for i in range(9):
        for k in range(9):
            if type(puzzle[i][k]) is list and len(puzzle[i][k])==1:
                puzzle[i][k] = puzzle[i][k][0]

def check_finished():
    for i in range(9):
        for k in range(9):
            if type(puzzle[i][k]) is list:
                return False
    return True

'''
def check_cell_copies():
    for i in range(9):
        for k in range(9):
            if 

def check_double_stacked():
    for i in range(9):
        for k in range(9):
            if type(puzzle[i][k]) is list and len(puzzle[i][k])==2:
                return False
'''

#add double stacked instances for rows and columns and vertical vs horizontal

'''  
  A B C   D E F   G H I
1 0 0 0 | 0 0 0 | 0 0 0
2 0 0 0 | 0 0 0 | 0 0 0
3 0 0 0 | 0 0 0 | 0 0 0
 ______________________
4 0 0 0 | 0 0 0 | 0 0 0
5 0 0 0 | 0 0 0 | 0 0 0
6 0 0 0 | 0 0 0 | 0 0 0
 ______________________
7 0 0 0 | 0 0 0 | 0 0 0
8 0 0 0 | 0 0 0 | 0 0 0
9 0 0 0 | 0 0 0 | 0 0 0
'''
user_in = ''
print("Please fill out the puzzle's starting state by choosing the row and column then entering the number of the cell \n  e.g. A1=2 and type run when finished: ")
while(user_in!='run'):
    print_puzzle_with_guide()
    user_in = input()
    if(re.match('^[A-Z][0-9]=[0-9]$', user_in)):
        row = int(user_in[1])-1
        col = ord(user_in[0])-65
        puzzle[row][col] = int(user_in[3])
    elif(user_in=='run'):
        break
    elif(user_in=='raw input'):
        print("Please paste the puzzle in with spaces between characters: ")
        matrix = input()
        puzzle = np.matrix(matrix).tolist()
    else:
        print("Invalid input, please try again")

initialize_puzzle()
iter_count = 0

while check_finished()==False:
    iter_count+=1
    for i in range(9):
        for k in range(9):
            if type(puzzle[i][k]) is list:
                cell = puzzle[i][k]
                for element in reversed(range(len(cell))):
                    if check_col_contains_value(cell[element], k):
                        del cell[element]
                    elif check_row_contains_value(cell[element], i):
                        del cell[element]
    collapse_cells()
    print("Iteration: ", iter_count)
    print_puzzle()
