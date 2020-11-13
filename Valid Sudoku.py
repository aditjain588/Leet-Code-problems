class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[]
        col=[]
        dia=[]
        for i in range(9):
            for j in range(9):
                if(board[i][j]!="."):
                    r_key=(i,board[i][j])
                    c_key=(j,board[i][j])
                    d_key=(i//3,j//3,board[i][j])
                    
                    if((r_key in row) or (c_key in col) or(d_key in dia)):
                        return False
                    
                    row.append(r_key)
                    col.append(c_key)
                    dia.append(d_key)
        return True