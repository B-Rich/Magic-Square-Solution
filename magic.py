import subprocess #Mainly used in the case of doing command prompt or a terminal behaviour
import sys
import re

def flap(magic_matrix,i,j):
    temp = magic_matrix[i][j]
    swap_i = 3 - i
    swap_j = 3 - j
    magic_matrix[i][j] = magic_matrix[swap_i][swap_j]
    magic_matrix[swap_i][swap_j] = temp
    return magic_matrix
    
def reverse(magic_matrix,control=0):
    if control == 0:
        magic_matrix = flap(magic_matrix,0,0)
        magic_matrix = flap(magic_matrix,0,3)
        magic_matrix = flap(magic_matrix,1,1)
        magic_matrix = flap(magic_matrix,1,2)
    return magic_matrix
    

def main():
  print "hello"
  init = 1
  magic_matrix = [[0 for x in range(4)] for x in range(4)]
  for x in range(4):
      for y in range(4):
          magic_matrix[x][y] = init
          init = init + 1
  magic_matrix = reverse(magic_matrix)
  
  sum_row = [0 for x in range(4)]
  sum_col = [0 for x in range(4)]
  sum_diag = [0 for x in range(2)]
  for x in range(4):
      for y in range(4):
          sum_row[x] = sum_row[x] + magic_matrix[x][y]
          sum_col[y] = sum_col[y] + magic_matrix[x][y]
          if x == y:
              sum_diag[0] = sum_diag[0] + magic_matrix[x][y]
          elif x == 3-y or y == 3-x:
              sum_diag[1] = sum_diag[1] + magic_matrix[x][y]
              
  print "Sum of all rows"
  print sum_row
  print "Sum of all columns"
  print sum_col
  print "Sum of all diagonals"
  print sum_diag
  print "Magic Matrix (4 X 4)"
  print magic_matrix
  

if __name__ == '__main__':
    main()