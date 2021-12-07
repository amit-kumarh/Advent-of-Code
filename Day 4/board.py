import copy

class Board:
    '''
    Class to represent a square grid-based game board

    Attributes
    ----------

    num: int
        the length of each side of the board

    board: list
        the board object itself

    Methods
    -------

    drawBoard()
        Prints the board onto the console
    '''    
    def __init__(self, num, vals = ' '):
        '''
        Constructs the necessary parameters and generates the board object

        Parameters
        ----------
        num: int
            the length of each side of the board

        vals: any
            what to fill each grid spot with
        '''
        self.winner = False # to prevent multiple wins on the same board 
        self.num = num
        self.board = [[vals[i*num + j] for j in range(num)] for i in range(num)]

    def drawBoard(self):
        '''Prints board onto the console with labeled row/columns'''
        for i in range(self.num):
            print(f'    {str(i+1)}   ', end='')
        print()
        print('--------'*len(self.board))
        for row in self.board:
            print('|\t' * (len(row)+1))
            for tile in row:
                print(f'|   {tile}   ', end='')
            print(f'|{str(self.board.index(row)+1)}')
            print('|\t' * (len(row)+1))
            print('--------'*len(self.board))

    def makeMove(self, call):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col == call:
                    self.board[i][j] = 'X'
    
    def hasWon(self):
        if self.winner:
            return False

        for row in self.board:
            has_won = True
            for col in row:
                if col != 'X':
                    has_won = False
            if has_won:
                self.winner = True
                return has_won

        for col in range(self.num):
            has_won = True
            for row in self.board:
                if row[col] != 'X':
                    has_won = False
            if has_won:
                self.winner = True
                return has_won
        
        return False

    def board_score(self, call):
        #Find sum
        count = 0
        for row in self.board:
            for col in row:
                if col != 'X':
                    count += int(col)
        
        return count * int(call)
