# Capture_mechanic.py

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
        return sum(1 for row in self.grid for card in row if card and card.owner == owner)

    def is_full(self):
        return all(card is not None for row in self.grid for card in row)


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


# --- Example playable simulation ---

# Host cards
host_cards = [
    SkystoneCard("h1", "Rock", 3, 2, 5, 1, owner="Host"),
    SkystoneCard("h2", "Stone", 2, 4, 1, 3, owner="Host"),
    SkystoneCard("h3", "Boulder", 4, 1, 2, 5, owner="Host"),
    SkystoneCard("h4", "Quartz", 1, 5, 3, 2, owner="Host"),
    SkystoneCard("h5", "Granite", 2, 3, 4, 1, owner="Host"),
    SkystoneCard("h6", "Obsidian", 3, 3, 2, 2, owner="Host"),
    SkystoneCard("h7", "Lava", 4, 2, 1, 5, owner="Host"),
    SkystoneCard("h8", "Marble", 1, 4, 3, 2, owner="Host")
]

# Visitor cards
visitor_cards = [
    SkystoneCard("v1", "Spike", 2, 4, 3, 2, owner="Visitor"),
    SkystoneCard("v2", "Blade", 5, 1, 2, 3, owner="Visitor"),
    SkystoneCard("v3", "Shard", 3, 3, 1, 4, owner="Visitor"),
    SkystoneCard("v4", "Crystal", 2, 5, 4, 1, owner="Visitor"),
    SkystoneCard("v5", "Fang", 4, 2, 3, 2, owner="Visitor"),
    SkystoneCard("v6", "Dagger", 1, 3, 5, 1, owner="Visitor"),
    SkystoneCard("v7", "Saber", 3, 1, 2, 4, owner="Visitor"),
    SkystoneCard("v8", "Claw", 2, 4, 1, 3, owner="Visitor")
]

game = SkystonesGame(host_cards, visitor_cards)

# Predefined moves for demonstration (row, col)
moves = [
    (2,2), (2,3), (1,2), (1,3), (3,2), (3,3), (4,2), (4,3),
    (1,1), (1,4), (4,1), (4,4), (2,1), (2,4), (3,1), (3,4)
]

# Simulate game
while not game.is_game_over():
    player = game.current_player()
    card_list = game.player_cards[player]
    if not card_list:
        game.next_turn()
        continue

    card_to_play = card_list[0]  # Pick first available card

    for r, c in moves:
        if game.board.is_empty(r, c):
            game.play_turn(card_to_play, r, c)
            break

# Final results
winner = game.check_winner()
print("\n--- Game Over ---")
print(f"Host stones: {game.board.count_owner_cards('Host')}")
print(f"Visitor stones: {game.board.count_owner_cards('Visitor')}")
print(f"Winner: {winner}")
        
