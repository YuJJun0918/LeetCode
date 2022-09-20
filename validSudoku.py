"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the Sudoku rules.
"""

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    
    return self.isValidSquare(board) and self.isValidRow(board) and self.isValidCol(board)
  
  def isValidSquare(self, board):
    
    for i in (0, 3, 6):
      for j in (0, 3, 6):
        square = [board[x][y] for x in range(i, i+3) for y in (j, j+3)]
        
        if not self.ValidUnit(square):
          return False
        
    return True
  
  
  def isValidCol(self, board):
    
    for col in zip(*board):
      if not self.isValidUnit(col):
        return False
    
    return True
  
  
  def isValidRow(self, board):
    
    for row in board:
      if not self.isValidUnit(row):
        return False
    
    return True
  
  
  def isValidUnit(self, unit):
    
    unit = [i for i in unit if i != '.']
    return len(set(unit)) == len(unit)
      
