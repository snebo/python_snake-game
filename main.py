import tkinter as tk
import random

# Constants
TILE_SIZE = 25
ROWS = 30
COLS = 30
bg_color = "white"
win_width = TILE_SIZE * COLS
win_height = TILE_SIZE * ROWS
INITIAL_VELOCITY = (0, 0)
INITIAL_SNAKE_LENGTH = 1

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Snake Game")
        self.window.resizable(False, False)
        
        self.canvas = tk.Canvas(window, background=bg_color, width=win_width, height=win_height, borderwidth=0, highlightthickness=0)
        self.canvas.pack()
        
        self.set_window_position()
        
        self.vel_x, self.vel_y = INITIAL_VELOCITY
        self.snake_body = [Tile(5 * TILE_SIZE, 5 * TILE_SIZE)]
        self.food = Tile(random.randint(0, COLS - 1) * TILE_SIZE, random.randint(0, ROWS - 1) * TILE_SIZE)
        
        self.window.bind("<KeyPress>", self.changedir)
        self.draw()

    def set_window_position(self):
        win_w = self.window.winfo_width()
        win_h = self.window.winfo_height()
        scr_w = self.window.winfo_screenwidth()
        scr_h = self.window.winfo_screenheight()
        win_x = int((scr_w / 2) - (win_w / 2))
        win_y = int((scr_h / 2) - (win_h / 2))
        self.window.geometry(f"{win_w}x{win_h}+{win_x}+{win_y}")

    def draw(self):
        self.canvas.delete("all")
        self.move()
        self.canvas.create_rectangle(self.food.x, self.food.y, self.food.x + TILE_SIZE, self.food.y + TILE_SIZE, fill="red")
        
        for tile in self.snake_body:
            self.canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="blue")
        
        if self.check_collision():
            self.canvas.create_text(win_width // 2, win_height // 2, text="Game Over", font=('Arial', 30), fill='red')
        else:
            self.window.after(100, self.draw)

    def changedir(self, e):
        if e.keysym == "Up" and self.vel_y == 0:
            self.vel_x, self.vel_y = 0, -1
        elif e.keysym == "Down" and self.vel_y == 0:
            self.vel_x, self.vel_y = 0, 1
        elif e.keysym == "Left" and self.vel_x == 0:
            self.vel_x, self.vel_y = -1, 0
        elif e.keysym == "Right" and self.vel_x == 0:
            self.vel_x, self.vel_y = 1, 0

    def move(self):
        new_head = Tile(self.snake_body[0].x + self.vel_x * TILE_SIZE, self.snake_body[0].y + self.vel_y * TILE_SIZE)
        
        if new_head.x == self.food.x and new_head.y == self.food.y:
            self.food = Tile(random.randint(0, COLS - 1) * TILE_SIZE, random.randint(0, ROWS - 1) * TILE_SIZE)
        else:
            self.snake_body.pop()

        self.snake_body.insert(0, new_head)

    def check_collision(self):
        head = self.snake_body[0]
        
        if head.x < 0 or head.x >= win_width or head.y < 0 or head.y >= win_height:
            return True
        
        for tile in self.snake_body[1:]:
            if tile.x == head.x and tile.y == head.y:
                return True
        
        return False

if __name__ == "__main__":
    window = tk.Tk()
    game = SnakeGame(window)
    window.mainloop()
