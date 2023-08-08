class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.rowCheck(board) and self.colCheck(board) and self.squareCheck(board))
            
    
    def rowCheck(self, board):
        
        for i in range(9):
            contains = [0 for n in range(9)]
            for j in range(9):
                if (not board[i][j] == "."):
                    value = int(board[i][j])
                    contains[value-1] +=1
                    if (contains[value-1] == 2):
                        return False
        return True
    
    def colCheck(self, board):
        for i in range(9):
            contains = [0 for n in range(9)]
            for j in range(9):
                if (not board[j][i] == "."):
                    value = int(board[j][i])
                    contains[value-1] +=1
                    if (contains[value-1] == 2):
                        return False
        return True
    
    def squareCheck(self,board):
        keyPoints = [1,4,7]
        for x in keyPoints:
            for y in keyPoints:
                if (not self.squareCheckAux(x,y,board)):
                    return False
        return True
    
    def squareCheckAux(self,x,y,board):
        boxes = [board[y+i-1][x+j-1] for i in range(3) for j in range(3)]
        contains = [0 for n in range(9)]
        for box in boxes:
            if (not box == "."):
                value = int(box)
                contains[value-1] +=1
                if (contains[value-1] ==2):
                    return False
        return True
            