 Skystones 4x4 – Python Prototype
A Python-based prototype of a **4×4 Skystones board game**, adapted from *Skylanders: Giants*. Designed for mobile-style logic, featuring tap-to-select and tap-to-place mechanics
## Features

* **4×4 Game Board**
  Fully represented in Python with coordinate-based access.
  Supports placement of stones/cards at `(row, column)` coordinates.

* **Card Object**
  Each Skystone card has four directional values (`top`, `bottom`, `left`, `right`) and optional image reference.

* **Quadrant System**
  Board divided into four quadrants for AI or gameplay logic (top-left, top-right, bottom-left, bottom-right).

* **Coordinate Utilities**

  * Convert coordinates to string format (`1.1`) and back.
  * Check if a cell is empty.
  * List all cells in a given quadrant.

* **Error Handling**

  * Invalid coordinates.
  * Attempted placement on occupied cells.

* **Display**

  * ASCII-style 4×4 board.
  * Optional coordinate mapping for debugging.


## Installation

Requires **Python 3.7+**.

```bash
git clone <repo_url>
cd skystones_4x4
python main.py
```

---

## Usage

```python
from board4x4 import Board4x4
from card import SkystoneCard

# Initialize board
board = Board4x4()

# Create a card
rock_chomp = SkystoneCard(
    card_id="stone_001",
    name="Rock Chomp",
    top=3,
    bottom=4,
    left=2,
    right=5
)

# Place card at row 3, column 4
board.set_cell(3, 4, rock_chomp.name)

# Display board
board.display()

# Check if a cell is empty
board.is_empty(2, 2)  # Returns True/False

# Convert coordinates to string
coord_str = board.coord_to_str(3, 4)  # "3.4"
```

---

## Quadrants

```
1 | 2
-----
3 | 4
```

* **1 (top-left):** Rows 1-2, Cols 1-2
* **2 (top-right):** Rows 1-2, Cols 3-4
* **3 (bottom-left):** Rows 3-4, Cols 1-2
* **4 (bottom-right):** Rows 3-4, Cols 3-4

Useful for AI, spawn logic, or organizing game strategies.

---

## Future Features

* Full gameplay logic (capture rules).
* Player turns (host vs visitor).
* Single-player AI and multiplayer support.
* Integration with a GUI for mobile (e.g., Kivy or Unity).

---

## License
This project is *inspired by Skylanders: Giants*, but uses **original assets and Python code**. For non-commercial purposes only.
