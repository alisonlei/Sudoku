from collections import deque
class Sudoku:
    def __init__(self,puzzle):
        self.puzzle=puzzle
        self.visited_cells=[]
        
    def __str__(self):
        return f'{self.puzzle}'

    def solve(self)->bool:
        row,col=self.get_blank_cell()
        #when there is no more blank cell, self.get_blank_cell returns None, None
        if row==None:
            return True
        self.visited_cells.append((row,col))
        #if no number can be filled without conflict, return False to previous cell
        return self.fill_in_num(row,col)
        
    
    def get_blank_cell(self)->tuple:
        if not self.visited_cells:
            start_col,start_row=0,0
        else:
            start_row=self.visited_cells[-1][0]
            

        for row in range(start_row,9):
            for col in range(9):
                if self.puzzle[row][col]==-1:
                    return row,col
        return None,None

    

    
    def fill_in_num(self,row,col):
        
        for num in range(1,10):
            conflict=self.check_conflict(row,col,num)
            if not conflict:
                self.puzzle[row][col]=num
                
                solved=self.solve()
                #when solved is false, it means though the num has no conflict with previous cells,
                #it leads to conflict at later cells, so another num has to be chosen.
                if solved:
                    return True
                
        self.puzzle[row][col]=-1#erase cell
        self.visited_cells.pop()
        return False
        
    
    def check_conflict(self,row,col,num):
        for i in range(9):
           
            if self.puzzle[row][i]==num:
                return True
        for j in range(9):
                
            if self.puzzle[j][col]==num:
                return True
        sqr_row=3*(row//3)
        sqr_col=3*(col//3)
        for i in range(sqr_row,sqr_row+3):
            for j in range(sqr_col,sqr_col+3):
                if self.puzzle[i][j]==num:
                    return True
        return False
        



if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    puzzle=Sudoku(example_board)
    
    solved=puzzle.solve()
    if solved:
        print(puzzle)
