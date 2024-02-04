class Solution:
    #dfs traversval for each X element 
    def dfs(self,board, row, col):
         if( row >= len(board) 
             or row<0 or col>=len(board[0]) 
             or col<0 or board[row][col]=='X' 
             or board[row][col]=='#'):
            return
            
         board[row][col]='#'

        #up,down, left, right directions
         self.dfs(board,row+1,col)
         self.dfs(board,row-1,col)
         self.dfs(board,row,col+1)
         self.dfs(board,row,col-1)

    def solve(self, board) -> None:

        n,m= len(board), len(board[0])
        
        # treversing across the border
        for index in range(0,m):
            self.dfs(board,0, index)
        for index in range(0,m):
            self.dfs(board,n-1, index)
        for index in range(0,n):
            self.dfs(board,index, 0)
        for index in range(0,n):
            self.dfs(board,index,m-1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j]='O'
                else :
                    board[i][j]='X'

ob1 = Solution()
board,row = [],[]
n = int(input("The no. of rows in boards:\n"))
m = int(input("The no. of columns in boards:\n"))
print(f"Enter {m*n} values:")

for i in range(n):
    row= input().split()[:m]
    board.append(row)

print("*"*10 + " solution matrix " + "*"*10)

ob1.solve(board)
for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print("")
