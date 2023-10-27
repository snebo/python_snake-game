"""
snake game home
"""
import tkinter
import random

# the foundation
TILE_SIZE = 25
ROWS = 30
COL = 30
bg_color = "white"
win_width = TILE_SIZE*ROWS #750 cause of the screen i'm using
win_height = TILE_SIZE*COL
vel_x, vel_y = 0,0
snake_body=[]

class Tile:
    def __init__(self, x , y):
        self.x = x
        self.y = y

#to create the window
window = tkinter.Tk()
window.title("snake game")
window.resizable(False,False)

#draw the board
canvas = tkinter.Canvas(window, background=bg_color, width=win_width, height=win_height, borderwidth=0, highlightthickness=0)
canvas.pack() #applies the setting to the canva
window.update() # updates the window information

#center the window
win_w = window.winfo_width() #get the window dimensions
win_h = window.winfo_height()
scr_w = window.winfo_screenwidth() #get the screen dimensions
scr_h = window.winfo_screenheight()

print(f"{win_w}+{win_h}+{scr_w}+{scr_h}")

win_x = int((scr_w/2)- (win_w/2))
win_y = int((scr_h/2) -(win_h/2))
# moves the midpoint of the window to the midpoint of the screen

window.geometry(f"{win_w}x{win_h}+{win_x}+{win_y}") #sets the new screen pos

#draw function
def draw():
    canvas.delete("all")
    move()

    global food
    canvas.create_rectangle(food.x, food.y, food.x+TILE_SIZE, food.y+TILE_SIZE, fill="red")

    global snake 
    canvas.create_rectangle(snake.x, snake.y, snake.x+TILE_SIZE, snake.y+TILE_SIZE, fill="blue")

    #draw the snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x+TILE_SIZE, tile.y+TILE_SIZE, fill = "blue")

    window.after(100, draw) #after 100ms, draw again

#movement
def changedir(e):
    global vel_x, vel_y
    # print(e) #debug key pressed
    if e.keysym == "Up":
       vel_x=0
       vel_y=-1
    elif e.keysym == "Down":
       vel_x=0
       vel_y=1
    elif e.keysym == "Left":
       vel_x=-1
       vel_y=0
    elif e.keysym == "Right":
       vel_x=1
       vel_y=0

def move():
    global snake, vel_y,vel_x,food, snake_body
    snake.x+= vel_x*TILE_SIZE
    snake.y += vel_y*TILE_SIZE

    #check if food is eaten
    if(snake.x == food.x and snake.y== food.y):
        snake_body.append(Tile(food.x, food.y))

        #remove and reset food
        food.x = random.randint(0, ROWS-1)*TILE_SIZE
        food.y = random.randint(0, COL-1)*TILE_SIZE
    

    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if(i==0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

#initilize the characters
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE)
food = Tile(12*TILE_SIZE, 6*TILE_SIZE)

draw()
window.bind("<KeyRelease>", changedir)
window.mainloop()
