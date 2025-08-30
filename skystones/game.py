class SkystonesGame:
    def __init__(self, size=4):
        # Initialize an empty board
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.current_player = "Opponent"  # Opponent always goes first
        self.moves_played = 0

    def switch_turn(self):
        """Switch between players."""
        self.current_player = "Player" if self.current_player == "Opponent" else "Opponent"

    def play_move(self, row, col):
        """
        Place a stone on the board if the cell is empty.
        row, col are 1-indexed for convenience.
        """
        if self.board[row-1][col-1] is not None:
            print("Invalid move! That spot is already taken.")
            return False

        # Place stone
        self.board[row-1][col-1] = self.current_player
        self.moves_played += 1

        print(f"{self.current_player} placed a stone at ({row},{col})")

        # Check if the board is full
        if self.moves_played == self.size * self.size:
            self.end_game()
            return True

        # Switch turn
        self.switch_turn()
        return True

    def end_game(self):
        """Count stones and declare a winner."""
        player_count = sum(row.count("Player") for row in self.board)
        opponent_count = sum(row.count("Opponent") for row in self.board)

        print("\nGame Over!")
        print(f"Player Stones: {player_count}")
        print(f"Opponent Stones: {opponent_count}")

        if player_count > opponent_count:
            print("Player Wins!")
        elif opponent_count > player_count:
            print("Opponent Wins!")
        else:
            print("It's a Tie!")

    def display_board(self):
        """Show the current board in a readable format."""
        for row in self.board:
            print(["." if cell is None else cell[0] for cell in row])
        print()
