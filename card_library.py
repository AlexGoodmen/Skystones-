# card_library.py

"""
Card Library
------------
This module defines the full set of cards available in the game.
The library can be imported anywhere in the project so the game
always has access to every card, regardless of player deck choices.
"""

CARD_LIBRARY = {
    "drow_lance_master_1": {"name": "Drow Lance Master 1", "element": None, "north": 1, "south": 0, "east": 0, "west": 1},
    "drow_lance_master_2": {"name": "Drow Lance Master 2", "element": None, "north": 2, "south": 0, "east": 0, "west": 2},
    "drow_lance_master_3": {"name": "Drow Lance Master 3", "element": None, "north": 3, "south": 0, "east": 0, "west": 3},
    "drow_lance_master_4": {"name": "Drow Lance Master 4", "element": None, "north": 3, "south": 1, "east": 1, "west": 3},

    "mohawk_cyclops_1": {"name": "Mohawk Cyclops 1", "element": None, "north": 1, "south": 0, "east": 1, "west": 0},
    "mohawk_cyclops_2": {"name": "Mohawk Cyclops 2", "element": None, "north": 2, "south": 0, "east": 2, "west": 0},
    "mohawk_cyclops_3": {"name": "Mohawk Cyclops 3", "element": None, "north": 3, "south": 0, "east": 3, "west": 0},
    "mohawk_cyclops_4": {"name": "Mohawk Cyclops 4", "element": None, "north": 3, "south": 1, "east": 3, "west": 1},

    "mace_major_1": {"name": "Mace Major 1", "element": None, "north": 0, "south": 1, "east": 0, "west": 1},
    "mace_major_2": {"name": "Mace Major 2", "element": None, "north": 0, "south": 2, "east": 0, "west": 2},
    "mace_major_3": {"name": "Mace Major 3", "element": None, "north": 0, "south": 3, "east": 0, "west": 3},
    "mace_major_4": {"name": "Mace Major 4", "element": None, "north": 1, "south": 3, "east": 1, "west": 3},

    "chompy_bot_9000_1": {"name": "Chompy Bot 9000 1", "element": None, "north": 1, "south": 1, "east": 0, "west": 0},
    "chompy_bot_9000_2": {"name": "Chompy Bot 9000 2", "element": None, "north": 1, "south": 1, "east": 1, "west": 1},
    "chompy_bot_9000_3": {"name": "Chompy Bot 9000 3", "element": None, "north": 2, "south": 2, "east": 1, "west": 1},
    "chompy_bot_9000_4": {"name": "Chompy Bot 9000 4", "element": None, "north": 2, "south": 2, "east": 2, "west": 2},
    "chompy_bot_9000_5": {"name": "Chompy Bot 9000 5", "element": None, "north": 3, "south": 3, "east": 2, "west": 2},
    "chompy_bot_9000_6": {"name": "Chompy Bot 9000 6", "element": None, "north": 3, "south": 3, "east": 3, "west": 3},

    "arkeyan_jouster_1": {"name": "Arkeyan Jouster 1", "element": None, "north": 2, "south": 0, "east": 1, "west": 1},
    "arkeyan_jouster_2": {"name": "Arkeyan Jouster 2", "element": None, "north": 3, "south": 0, "east": 1, "west": 1},
    "arkeyan_jouster_3": {"name": "Arkeyan Jouster 3", "element": None, "north": 3, "south": 0, "east": 2, "west": 2},
    "arkeyan_jouster_4": {"name": "Arkeyan Jouster 4", "element": None, "north": 3, "south": 1, "east": 2, "west": 2},
    "arkeyan_jouster_5": {"name": "Arkeyan Jouster 5", "element": None, "north": 3, "south": 2, "east": 2, "west": 2},

    "conquertron": {"name": "CONQUERTRON", "element": None, "north": 4, "south": 4, "east": 4, "west": 4},
    "arkeyan_ultron": {"name": "Arkeyan Ultron", "element": "tech", "north": 2, "south": 2, "east": 2, "west": 2},

    "enfuego_chompy_1": {"name": "Enfuego Chompy 1", "element": "fire", "north": 1, "south": 0, "east": 0, "west": 0},
    "frigid_chompy_1": {"name": "Frigid Chompy 1", "element": "water", "north": 0, "south": 1, "east": 0, "west": 0},
    "goliath_drow": {"name": "Goliath Drow", "element": "life", "north": 4, "south": 0, "east": 1, "west": 1},
    "dragonet": {"name": "Dragonet", "element": "air", "north": 1, "south": 2, "east": 3, "west": 2},
    "shadow_duke": {"name": "Shadow Duke", "element": None, "north": 4, "south": 0, "east": 0, "west": 0},
    "boulder_bowler": {"name": "Boulder Bowler", "element": "earth", "north": 2, "south": 0, "east": 2, "west": 2},
    "life_spell_punk": {"name": "Life Spell Punk", "element": "magic", "north": 2, "south": 0, "east": 1, "west": 3},
}


# --- Helper functions ---
def get_card(card_id: str) -> dict:
    """Return a card by its ID, or None if not found."""
    return CARD_LIBRARY.get(card_id)


def list_all_cards() -> list:
    """Return a list of all card IDs in the library."""
    return list(CARD_LIBRARY.keys())


def search_by_element(element: str) -> dict:
    """Return all cards matching a given element."""
    return {cid: c for cid, c in CARD_LIBRARY.items() if c["element"] == element}
