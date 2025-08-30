class SkystoneCard:
    def __init__(self, card_id, name, top, bottom, left, right, owner=None):
        self.card_id = card_id
        self.name = name
        self.values = {
            "top": top,
            "bottom": bottom,
            "left": left,
            "right": right
        }
        self.owner = owner  # Player who owns the card

    def __repr__(self):
        return f"<{self.name} T:{self.values['top']} B:{self.values['bottom']} L:{self.values['left']} R:{self.values['right']} Owner:{self.owner}>"

class Board4x4:
    def __init__(self):
        self.size = 4
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def validate_coords(self, row, col):
        return 1 <= row <= self.size and 1 <= col <= self.size

    def is_empty(self, row, col):
        if not self.validate_coords(row, col):
            return False
        return self.grid[row-1][col-1] is None

    def get_card(self, row, col):
        if not self.validate_coords(row, col):
            return None
        return self.grid[row-1][col-1]

    def place_card(self, row, col, card: SkystoneCard):
        if not self.validate_coords(row, col):
            raise ValueError("Invalid coordinates. Use 1..4 for row and column.")
        if not self.is_empty(row, col):
            raise ValueError(f"Cell {row}.{col} is already occupied.")

        self.grid[row-1][col-1] = card
        self.capture_adjacent(row, col, card)

    def capture_adjacent(self, row, col, card: SkystoneCard):
        directions = {
            "top": (row-1, col, "bottom"),
            "bottom": (row+1, col, "top"),
            "left": (row, col-1, "right"),
            "right": (row, col+1, "left")
        }
        for dir_name, (r, c, opposite) in directions.items():
            if self.validate_coords(r, c):
                neighbor = self.get_card(r, c)
                if neighbor and neighbor.owner != card.owner:
                    if card.values[dir_name] > neighbor.values[opposite]:
                        neighbor.owner = card.owner  # Flip card

    def display(self):
        header = "   " + " ".join(f" {c} " for c in range(1, self.size+1))
        print(header)
        print("  +" + "---+" * self.size)
        for r in range(1, self.size+1):
            row_cells = []
            for c in range(1, self.size+1):
                val = self.get_card(r, c)
                if val is None:
                    row_cells.append(" . ")
                else:
                    row_cells.append(f"{val.name[0]}{val.owner[0]}")
            print(f"{r} |" + "|".join(row_cells) + "|")
            print("  +" + "---+" * self.size)

    def count_ownership(self):
        """Count cards owned by each player."""
        counts = {}
        for r in range(1, self.size+1):
            for c in range(1, self.size+1):
                card = self.get_card(r, c)
                if card and card.owner:
                    counts[card.owner] = counts.get(card.owner, 0) + 1
        return counts

class SkystonesGame:
    def __init__(self, host_deck, visitor_deck):
        self.board = Board4x4()
        self.decks = {
            "Host": host_deck.copy(),
            "Visitor": visitor_deck.copy()
        }
        self.turn_order = ["Host", "Visitor"]
        self.current_turn_idx = 0

    def next_turn(self):
        self.current_turn_idx = (self.current_turn_idx + 1) % len(self.turn_order)
        return self.turn_order[self.current_turn_idx]

    def current_player(self):
        return self.turn_order[self.current_turn_idx]

    def is_game_over(self):
        # Game over when all cells are filled
        for r in range(1, self.board.size+1):
            for c in range(1, self.board.size+1):
                if self.board.is_empty(r, c):
                    return False
        return True

    def play_turn(self, row, col):
        player = self.current_player()
        if not self.decks[player]:
            raise ValueError(f"{player} has no cards left!")

        card = self.decks[player].pop(0)
        card.owner = player
        self.board.place_card(row, col, card)

        print(f"{player} placed {card.name} at {row}.{col}")
        self.board.display()
        self.next_turn()

    def get_winner(self):
        counts = self.board.count_ownership()
        if counts.get("Host", 0) > counts.get("Visitor", 0):
            return "Host"
        elif counts.get("Visitor", 0) > counts.get("Host", 0):
            return "Visitor"
        return "Draw"

# --- Example usage ---
if __name__ == "__main__":
    # Create some cards for each player
    host_deck = [
        SkystoneCard("stone_001", "Rock Chomp", 3, 4, 2, 5),
        SkystoneCard("stone_003", "Water Surge", 2, 5, 3, 4)
    ]
    visitor_deck = [
        SkystoneCard("stone_002", "Flame Blast", 4, 3, 5, 2),
        SkystoneCard("stone_004", "Wind Slash", 3, 3, 4, 4)
    ]

    game = SkystonesGame(host_deck, visitor_deck)
    game.board.display()

    # Simulate turns
    game.play_turn(1, 1)  # Host
    game.play_turn(1, 2)  # Visitor
    game.play_turn(2, 1)  # Host
    game.play_turn(2, 2)  # Visitor

    if game.is_game_over():
        winner = game.get_winner()
        print(f"Game Over! Winner: {winner}")
    else:
        print("Game in progress...")
