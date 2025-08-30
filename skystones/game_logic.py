class Stone:
    def __init__(self, owner, blades):
        """
        owner: 'Player' or 'Opponent'
        blades: dict with values for each side {"up": int, "down": int, "left": int, "right": int}
        """
        self.owner = owner
        self.blades = blades

class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def place_stone(self, row, col, stone):
        """Place a stone and apply flipping rules"""
        if self.grid[row][col] is not None:
            raise ValueError("That cell is already occupied!")

        self.grid[row][col] = stone

        # Check adjacency
        directions = {
            "up": (-1, 0, "down"),
            "down": (1, 0, "up"),
            "left": (0, -1, "right"),
            "right": (0, 1, "left"),
        }

        for direction, (dr, dc, opposite) in directions.items():
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                neighbor = self.grid[nr][nc]
                if neighbor:  # if there’s a stone there
                    # Compare blades
                    if stone.blades[direction] > neighbor.blades[opposite]:
                        neighbor.owner = stone.owner  # flip ownership

    def is_full(self):
        """Check if the board is completely filled"""
        return all(self.grid[r][c] is not None for r in range(self.size) for c in range(self.size))

    def score(self):
        """Return current stone counts per player"""
        player_count = sum(1 for row in self.grid for s in row if s and s.owner == "Player")
        opponent_count = sum(1 for row in self.grid for s in row if s and s.owner == "Opponent")
        return {"Player": player_count, "Opponent": opponent_count}

board = Board()

# Define some stones
stone1 = Stone("Opponent", {"up":2,"down":3,"left":1,"right":4})
stone2 = Stone("Player", {"up":5,"down":2,"left":3,"right":1})

# Opponent goes first
board.place_stone(1, 1, stone1)

# Player places next to it
board.place_stone(1, 2, stone2)

# Stone2 has left=3 vs Stone1.right=4 → no flip
# But if left > 4, Stone1 would flip to Player
