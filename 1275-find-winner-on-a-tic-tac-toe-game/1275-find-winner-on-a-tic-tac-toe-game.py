class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Initialize 3x3 board
        board = [['' for _ in range(3)] for _ in range(3)]
        
        # Helper function to check if someone has won
        def check_winner():
            # Check rows
            for i in range(3):
                if board[i][0] != '' and board[i][0] == board[i][1] == board[i][2]:
                    return board[i][0]
                    
            # Check columns
            for j in range(3):
                if board[0][j] != '' and board[0][j] == board[1][j] == board[2][j]:
                    return board[0][j]
                    
            # Check diagonals
            if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
                return board[0][0]
            if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
                return board[0][2]
                
            return None
        
        # Place moves alternately
        for i, (row, col) in enumerate(moves):
            # Place 'X' for player A (even moves), 'O' for player B (odd moves)
            board[row][col] = 'X' if i % 2 == 0 else 'O'
            
            # Check for winner after each move
            winner = check_winner()
            if winner:
                return 'A' if winner == 'X' else 'B'
        
        # If no winner, return Draw if board is full (9 moves), else Pending
        return "Draw" if len(moves) == 9 else "Pending"