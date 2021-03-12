

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
        
    

def find_zero(board):
    
    for r_o in range(len(board)):
        for c_o in range (len(board[0])):
          if board[r_o][c_o]==0:
              

              return (r_o,c_o)
    return None
          


def is_valid(board, row , col ,val):
  

  for r_v in range(len(board)):
    if str(val) == str(board[r_v][col]):
          return False
        
  for c_v in range(len(board[0])):
    if str(val) == str(board[row][c_v]):
          return False

  box_x=col //3
  box_y=row //3
  for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == val :
                return False


  
  return True

      
     
def test(board):
  sol=[]
  find = find_zero(board)
  if find==None:
      print_board(board)
      return True
  else:
      row, col = find
      for i in range(1,10):
        if is_valid(board,row,col,i):
            board[row][col] = i
            if test(board)==True:
                return True
            board[row][col]=0
  return False
  
      
      
          
      
      
    
 

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]


#print_board(board)
#find_zero(board)
#is_valid(board, 0, 2, 1)

#is_valid(board, 0, 2, 6)
#is_valid(board, 3, 5, 9)
test(board)


