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
        self.owner = owner

    def __repr__(self):
        return f"<{self.name} T:{self.values['top']} B:{self.values['bottom']} L:{self.values['left']} R:{self.values['right']} Owner:{self.owner}>"


class Board4x4:
    def __init__(self):
        self.size = 4
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    def validate_coords(self, row, col):
        return 1 <= row <= self.size and 1 <= col <= self.size

    def is_empty(self, row, col):
        return self.grid[row-1][col-1] is None

    def get_card(self, row, col):
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
                        neighbor.owner = card.owner

    def display(self):
        header = "   " + " ".join(f" {c} " for c in range(1, self.size+1))
        print(header)
        print("  +" + "---+"*self.size)
        for r in range(1, self.size+1):
            row_cells = []
            for c in range(1, self.size+1):
                val = self.get_card(r, c)
                if val is None:
                    row_cells.append(" . ")
                else:
                    row_cells.append(f"{val.name[0]}{val.owner[0]}")
            print(f"{r} |" + "|".join(row_cells) + "|")
            print("  +" + "---+"*self.size)

    def count_owner_cards(self, owner):
        count = 0
        for row in self.grid:
            for card in row:
                if card and card.owner == owner:
                    count += 1
        return count

    def is_full(self):
        for row in self.grid:
            for card in row:
                if card is None:
                    return False
        return True


# --- Turn-based game logic ---
class SkystonesGame:
    def __init__(self, host_cards, visitor_cards):
        self.board = Board4x4()
        self.turn_order = ["Host", "Visitor"]
        self.current_turn_idx = 0
        self.player_cards = {
            "Host": host_cards,
            "Visitor": visitor_cards
        }

    def next_turn(self):
        self.current_turn_idx = (self.current_turn_idx + 1) % 2

    def current_player(self):
        return self.turn_order[self.current_turn_idx]

    def play_turn(self, card: SkystoneCard, row, col):
        player = self.current_player()
        if card.owner != player:
            raise ValueError(f"This card does not belong to {player}.")
        self.board.place_card(row, col, card)
        self.player_cards[player].remove(card)
        self.board.display()
        self.next_turn()

    def check_winner(self):
        host_count = self.board.count_owner_cards("Host")
        visitor_count = self.board.count_owner_cards("Visitor")
        if host_count > visitor_count:
            return "Host"
        elif visitor_count > host_count:
            return "Visitor"
        else:
            return "Tie"

    def is_game_over(self):
        return self.board.is_full()


# --- Example usage ---
if __name__ == "__main__":
    # Create cards for each player
    host_cards = [
        SkystoneCard("H1", "RockChomp", 3, 4, 2, 5, owner="Host"),
        SkystoneCard("H2", "WaterSurge", 2, 5, 3, 4, owner="Host"),
        SkystoneCard("H3", "EarthSmash", 4, 2, 5, 3, owner="Host")
    ]
    visitor_cards = [
        SkystoneCard("V1", "FlameBlast", 4, 3, 5, 2, owner="Visitor"),
        SkystoneCard("V2", "WindStrike", 3, 5, 4, 2, owner="Visitor"),
        SkystoneCard("V3", "ShadowFang", 5, 2, 3, 4, owner="Visitor")
    ]

    # Initialize game
    game = SkystonesGame(host_cards, visitor_cards)

    # Sample turns
    game.play_turn(host_cards[0], 2, 2)     # Host places RockChomp at 2,2
    game.play_turn(visitor_cards[0], 2, 3)  # Visitor places FlameBlast at 2,3
    game.play_turn(host_cards[1], 1, 3)     # Host places WaterSurge at 1,3
    game.play_turn(visitor_cards[1], 3, 2)  # Visitor places WindStrike at 3,2
    game.play_turn(host_cards[2], 4, 4)     # Host places EarthSmash at 4,4
    game.play_turn(visitor_cards[2], 1, 1)  # Visitor places ShadowFang at 1,1

    # Game end check
    if game.is_game_over():
        winner = game.check_winner()
        print("\nGame Over! Winner:", winner)
