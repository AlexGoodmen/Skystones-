class Board4x4:
    def __init__(self):
        self.size = 4
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]

    # --- Basic cell helpers (1-based) ---
    def validate_coords(self, row, col):
        return 1 <= row <= self.size and 1 <= col <= self.size

    def set_cell(self, row, col, value):
        if not self.validate_coords(row, col):
            raise ValueError("Coordinates out of range. Use 1..4 for row and column.")
        if self.grid[row-1][col-1] is not None:
            raise ValueError(f"Cell {row}.{col} is already occupied.")
        self.grid[row-1][col-1] = value

    def get_cell(self, row, col):
        if not self.validate_coords(row, col):
            raise ValueError("Coordinates out of range. Use 1..4 for row and column.")
        return self.grid[row-1][col-1]

    def is_empty(self, row, col):
        return self.get_cell(row, col) is None

    # --- Coordinate string helpers ---
    @staticmethod
    def coord_to_str(row, col):
        return f"{row}.{col}"

    @staticmethod
    def str_to_coord(coord_str):
        try:
            r, c = coord_str.split(".")
            return int(r), int(c)
        except Exception:
            raise ValueError("Coordinate must be in 'row.col' format with integers, e.g. '3.4'.")

    # --- Quadrant helpers ---
    def get_quadrant(self, row, col):
        top = row <= 2
        left = col <= 2
        if top and left: return 1, "top-left"
        if top and not left: return 2, "top-right"
        if not top and left: return 3, "bottom-left"
        return 4, "bottom-right"

    def cells_in_quadrant(self, quadrant):
        if quadrant == 1: rows, cols = range(1,3), range(1,3)
        elif quadrant == 2: rows, cols = range(1,3), range(3,5)
        elif quadrant == 3: rows, cols = range(3,5), range(1,3)
        elif quadrant == 4: rows, cols = range(3,5), range(3,5)
        else: raise ValueError("Quadrant must be 1..4.")
        return [(r,c) for r in rows for c in cols]

    def quadrant_summary(self):
        summary = {}
        for q in range(1,5):
            cells = self.cells_in_quadrant(q)
            occupied = [(r,c) for (r,c) in cells if not self.is_empty(r,c)]
            summary[q] = {"occupied_count": len(occupied), "occupied_coords": occupied}
        return summary

    # --- Display ---
    def display(self):
        header = "   " + " ".join(f" {c} " for c in range(1, self.size+1))
        print(header)
        print("  +" + "---+"*self.size)
        for r in range(1, self.size+1):
            row_cells = []
            for c in range(1, self.size+1):
                val = self.get_cell(r,c)
                row_cells.append(f" {val if val is not None else '.'} ")
            print(f"{r} |" + "|".join(row_cells) + "|")
            print("  +" + "---+"*self.size)


# --- Example usage ---
if __name__ == "__main__":
    board = Board4x4()
    
    # Place markers using your coordinates
    coordinates = [
        (1,1),(1,2),(1,3),(1,4),
        (2,1),(2,2),(2,3),(2,4),
        (3,1),(3,2),(3,3),(3,4),
        (4,1),(4,2),(4,3),(4,4)
    ]
    
    for idx, (r,c) in enumerate(coordinates, start=1):
        board.set_cell(r, c, f"{idx}")  # assign unique number to each cell for demo
    
    board.display()
    
    print("\nQuadrant summary:")
    print(board.quadrant_summary())
