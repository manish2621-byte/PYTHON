import tkinter as tk
import random

WIDTH = 400
HEIGHT = 600

root = tk.Tk()
root.title("Car Racing Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="gray")
canvas.pack()

# Road lines
for i in range(0, HEIGHT, 40):
    canvas.create_line(200, i, 200, i + 20, fill="white", width=5)

# Player Car
player = canvas.create_rectangle(170, 500, 230, 580, fill="blue")

# Enemy Car
enemy = canvas.create_rectangle(170, 50, 230, 130, fill="red")

score = 0
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

def move_left(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x1 > 0:
        canvas.move(player, -20, 0)

def move_right(event):
    x1, y1, x2, y2 = canvas.coords(player)
    if x2 < WIDTH:
        canvas.move(player, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

def game_loop():
    global score

    canvas.move(enemy, 0, 10)

    ex1, ey1, ex2, ey2 = canvas.coords(enemy)

    if ey2 > HEIGHT:
        lane = random.choice([70, 170, 270])
        canvas.coords(enemy, lane, 0, lane + 60, 80)
        score += 1
        score_label.config(text=f"Score: {score}")

    px1, py1, px2, py2 = canvas.coords(player)

    # Collision Detection
    if (px1 < ex2 and px2 > ex1 and
        py1 < ey2 and py2 > ey1):
        canvas.create_text(
            WIDTH//2,
            HEIGHT//2,
            text="GAME OVER",
            font=("Arial", 25, "bold"),
            fill="yellow"
        )
        return

    root.after(50, game_loop)

game_loop()
root.mainloop()