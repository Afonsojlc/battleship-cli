import unittest
from battleship import Board


class TestBoard(unittest.TestCase):
    """Unit tests for the Battleship Board class."""

    def setUp(self):
        """Create a default 5x5 board before each test."""
        self.board = Board(size=5, num_ships=3)

    def test_board_initialization(self):
        """Verify the board initializes with correct size and ship count."""
        self.assertEqual(self.board.size, 5)
        self.assertEqual(self.board.num_ships, 3)
        self.assertEqual(len(self.board.grid), 5)
        self.assertEqual(len(self.board.grid[0]), 5)
        self.assertEqual(len(self.board.ships), 3)

        # Ensure all cells start as unrevealed ocean 'O'
        for row in self.board.grid:
            for cell in row:
                self.assertEqual(cell, "O")

    def test_ships_within_bounds(self):
        """Ensure all randomly generated ships are inside grid boundaries."""
        for row, col in self.board.ships:
            self.assertTrue(0 <= row < self.board.size)
            self.assertTrue(0 <= col < self.board.size)

    def test_out_of_bounds_guess(self):
        """Ensure guesses outside the grid boundaries are rejected without penalty."""
        invalid_coords = [(-1, 0), (0, -1), (5, 0), (0, 5), (10, 10)]
        for row, col in invalid_coords:
            valid, message = self.board.make_guess(row, col)
            self.assertFalse(valid)
            self.assertIn("Out of bounds", message)

    def test_repeated_guess(self):
        """Ensure firing twice at the same coordinates is rejected without penalty."""
        # Force a miss on (0, 0)
        self.board.ships.discard((0, 0))
        valid, _ = self.board.make_guess(0, 0)
        self.assertTrue(valid)

        # Second guess at the same coordinates
        second_valid, second_message = self.board.make_guess(0, 0)
        self.assertFalse(second_valid)
        self.assertIn("already fired", second_message)

    def test_successful_hit(self):
        """Ensure a hit updates the grid, removes the ship, and consumes a turn."""
        self.board.ships = {(1, 2)}
        self.board.grid = [["O"] * 5 for _ in range(5)]

        valid, message = self.board.make_guess(1, 2)
        self.assertTrue(valid)
        self.assertIn("DIRECT HIT", message)
        self.assertEqual(self.board.grid[1][2], "X")
        self.assertNotIn((1, 2), self.board.ships)
        self.assertTrue(self.board.is_victory())

    def test_miss_shot(self):
        """Ensure a missed shot marks '#' and consumes a turn."""
        self.board.ships = {(3, 3)}
        self.board.grid = [["O"] * 5 for _ in range(5)]

        valid, message = self.board.make_guess(1, 1)
        self.assertTrue(valid)
        self.assertIn("Missed", message)
        self.assertEqual(self.board.grid[1][1], "#")
        self.assertIn((3, 3), self.board.ships)
        self.assertFalse(self.board.is_victory())

    def test_reveal_ships_display(self):
        """Ensure un-sunk ships are displayed as 'S' when reveal_ships is enabled."""
        self.board.ships = {(0, 0)}
        self.board.grid = [["O"] * 5 for _ in range(5)]

        normal_view = self.board.display(reveal_ships=False)
        self.assertNotIn("S", normal_view)

        revealed_view = self.board.display(reveal_ships=True)
        self.assertIn("S", revealed_view)


if __name__ == "__main__":
    unittest.main()
