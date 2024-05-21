import unittest
from main import SnakeGame, Tile, TILE_SIZE, win_width, win_height
import tkinter as tk

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.game = SnakeGame(self.window)

    def test_move(self):
        # Initial snake head position
        initial_head = self.game.snake_body[0]
        initial_x, initial_y = initial_head.x, initial_head.y

        # Set direction to right and move
        self.game.vel_x, self.game.vel_y = 1, 0
        self.game.move()

        # New head position after move
        new_head = self.game.snake_body[0]
        self.assertEqual(new_head.x, initial_x + TILE_SIZE)
        self.assertEqual(new_head.y, initial_y)

        # Test growth when eating food
        self.game.food = Tile(new_head.x + TILE_SIZE, new_head.y)
        self.game.move()
        self.assertEqual(len(self.game.snake_body), 2)  # Snake should grow

    def test_check_collision(self):
        # Test collision with wall
        self.game.snake_body[0] = Tile(win_width, self.game.snake_body[0].y)
        self.assertTrue(self.game.check_collision())

        # Test collision with self
        self.game.snake_body = [
            Tile(5 * TILE_SIZE, 5 * TILE_SIZE),
            Tile(6 * TILE_SIZE, 5 * TILE_SIZE),
            Tile(7 * TILE_SIZE, 5 * TILE_SIZE),
            Tile(7 * TILE_SIZE, 4 * TILE_SIZE),
            Tile(6 * TILE_SIZE, 4 * TILE_SIZE),
            Tile(5 * TILE_SIZE, 4 * TILE_SIZE),
            Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
        ]
        self.assertTrue(self.game.check_collision())

        # Test no collision
        self.game.snake_body = [
            Tile(5 * TILE_SIZE, 5 * TILE_SIZE),
            Tile(6 * TILE_SIZE, 5 * TILE_SIZE),
            Tile(7 * TILE_SIZE, 5 * TILE_SIZE)
        ]
        self.assertFalse(self.game.check_collision())

if __name__ == "__main__":
    unittest.main()