# 4x4 board with coordinate helpers and quadrant (quarter) mapping.
# Coordinates are 1-based: row and col in 1..4. Quadrants are 1..4:
# 1 = top-left, 2 = top-right, 3 = bottom-left, 4 = bottom-right.

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
        """Return 'r.c' string, e.g. '3.4'."""
        return f"{row}.{col}"

    @staticmethod
    def str_to_coord(coord_str):
        """Parse 'r.c' and return (row, col) as ints. Raises ValueError on bad format."""
        try:
            r, c = coord_str.split(".")
            return int(r), int(c)
        except Exception:
            raise ValueError("Coordinate must be in 'row.col' format with integers, e.g. '3.4'.")

    # --- Quadrant / quarter helpers ---
    def get_quadrant(self, row, col):
        """
        Return quadrant id (1..4) and label.
        Quadrant layout:
          1 | 2
         -----
          3 | 4
        Top rows are 1-2, bottom rows 3-4.
        Left cols are 1-2, right cols 3-4.
        """
        if not self.validate_coords(row, col):
            raise ValueError("Coordinates out of range. Use 1..4 for row and column.")
        top = row <= 2
        left = col <= 2
        if top and left:
            return 1, "top-left"
        if top and not left:
            return 2, "top-right"
        if not top and left:
            return 3, "bottom-left"
        return 4, "bottom-right"

    def cells_in_quadrant(self, quadrant):
        """Return list of (row, col) for a given quadrant id (1..4)."""
        if quadrant == 1:
            rows, cols = range(1, 3), range(1, 3)
        elif quadrant == 2:
            rows, cols = range(1, 3), range(3, 5)
        elif quadrant == 3:
            rows, cols = range(3, 5), range(1, 3)
        elif quadrant == 4:
            rows, cols = range(3, 5), range(3, 5)
        else:
            raise ValueError("Quadrant must be 1..4.")
        return [(r, c) for r in rows for c in cols]

    # Optional: get quadrant occupancy summary
    def quadrant_summary(self):
        """Return dict mapping quadrant id to number of occupied cells and list of coords."""
        summary = {}
        for q in (1, 2, 3, 4):
            cells = self.cells_in_quadrant(q)
            occupied = [(r, c) for (r, c) in cells if not self.is_empty(r, c)]
            summary[q] = {"occupied_count": len(occupied), "occupied_coords": occupied}
        return summary

    # --- Display (simple) ---
    def display(self):
        header = "   " + " ".join(f" {c} " for c in range(1, self.size+1))
        print(header)
        print("  +" + "---+" * self.size)
        for r in range(1, self.size+1):
            row_cells = []
            for c in range(1, self.size+1):
                val = self.get_cell(r, c)
                cell_text = "." if val is None else str(val)
                row_cells.append(f" {cell_text} ")
            print(f"{r} |" + "|".join(row_cells) + "|")
            print("  +" + "---+" * self.size)


# --- Example usage ---
if __name__ == "__main__":
    board = Board4x4()
    # place markers for demonstration
    board.set_cell(1, 1, "A")   # top-left quadrant
    board.set_cell(2, 4, "B")   # top-right quadrant
    board.set_cell(3, 2, "C")   # bottom-left quadrant
    board.set_cell(4, 4, "D")   # bottom-right quadrant

    board.display()

    print("\nCoordinate examples:")
    print("3.4 ->", board.coord_to_str(3, 4))
    print("'2.1' ->", board.str_to_coord("2.1"))

    print("\nQuadrant map for some coords:")
    for coord in [(1,1),(1,4),(3,2),(4,4)]:
        qid, qlabel = board.get_quadrant(*coord)
        print(f"{coord} -> quadrant {qid} ({qlabel})")

    print("\nCells in quadrant 2 (top-right):", board.cells_in_quadrant(2))
    print("\nQuadrant occupancy summary:", board.quadrant_summary())
    
