"""
Battleship CLI
A terminal-based Battleship game built with Python and Object-Oriented Programming (OOP).
"""

import random
import sys
from typing import List, Set, Tuple

# Ensure UTF-8 output encoding across terminals (including Windows cp1252 default)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


class Board:
    """Represents the Battleship game board and state."""

    def __init__(self, size: int = 5, num_ships: int = 3):
        """
        Initialize the game board.

        :param size: Dimension of the square grid (default: 5 for 5x5).
        :param num_ships: Number of hidden enemy ships to place (default: 3).
        """
        self.size = size
        self.num_ships = num_ships
        self.grid: List[List[str]] = [["O"] * size for _ in range(size)]
        self.ships: Set[Tuple[int, int]] = set()

        self.place_ships()

    def place_ships(self) -> None:
        """Randomly position ships on the board ensuring no overlapping locations."""
        while len(self.ships) < self.num_ships:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.ships.add((row, col))

    def display(self, reveal_ships: bool = False) -> str:
        """
        Generate a formatted string representation of the board.

        :param reveal_ships: If True, reveals remaining un-sunk ships marked with 'S'.
        :return: Formatted board grid string.
        """
        output = ["\n  " + " ".join(str(i) for i in range(self.size))]
        for idx, row in enumerate(self.grid):
            row_display = []
            for col_idx, cell in enumerate(row):
                if reveal_ships and (idx, col_idx) in self.ships and cell == "O":
                    row_display.append("S")
                else:
                    row_display.append(cell)
            output.append(f"{idx} " + " ".join(row_display))
        output.append("")
        return "\n".join(output)

    def print_board(self, reveal_ships: bool = False) -> None:
        """Print the game board to the console."""
        print(self.display(reveal_ships=reveal_ships))

    def make_guess(self, row: int, col: int) -> Tuple[bool, str]:
        """
        Process a player's shot at the given coordinates.

        :param row: Row index chosen by the player.
        :param col: Column index chosen by the player.
        :return: Tuple (is_valid_turn, message)
                 is_valid_turn indicates whether this guess consumes an attempt.
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False, f"⚠️ Out of bounds! Please pick numbers between 0 and {self.size - 1}."

        if self.grid[row][col] != "O":
            return False, "⚠️ You already fired at these coordinates! Choose another target."

        if (row, col) in self.ships:
            self.grid[row][col] = "X"
            self.ships.remove((row, col))
            return True, "🎯 DIRECT HIT! You sank an enemy battleship!"

        self.grid[row][col] = "#"
        return True, "🌊 Splash... Missed into open water."

    def is_victory(self) -> bool:
        """Check whether all enemy ships have been sunk."""
        return len(self.ships) == 0


def play_game() -> None:
    """Run the main Battleship command-line game loop."""
    print("=" * 45)
    print("        🚢 BATTLESHIP CLI GAME 🚢        ")
    print("=" * 45)
    print("Locate and sink all hidden enemy ships!")
    print("Legend: [O] Unexplored Sea | [X] Ship Sunk | [#] Missed Shot | [S] Revealed Ship\n")

    # Game Configuration
    board = Board(size=5, num_ships=3)
    attempts = 10

    while attempts > 0:
        board.print_board()
        print(f"Attempts remaining: {attempts}")
        print(f"Enemy ships remaining: {len(board.ships)}")

        try:
            row_input = input(f"Select ROW (0-{board.size - 1}): ").strip()
            col_input = input(f"Select COL (0-{board.size - 1}): ").strip()

            row = int(row_input)
            col = int(col_input)

            valid_turn, message = board.make_guess(row, col)
            print(f"\n---> {message}")

            if valid_turn:
                attempts -= 1

            if board.is_victory():
                board.print_board()
                print("=" * 45)
                print("🏆 VICTORY! You successfully sunk all enemy ships!")
                print("=" * 45)
                break

        except ValueError:
            print("\n❌ Invalid input: Please enter valid integer coordinates!")

    if not board.is_victory():
        print("\n" + "=" * 45)
        print("💀 GAME OVER! You ran out of attempts.")
        print("Here is where the remaining enemy fleet was hiding:")
        board.print_board(reveal_ships=True)
        print("=" * 45)


if __name__ == "__main__":
    play_game()
