import tkinter as tk
from random import randint


class Raindrop:
    def __init__(self, canvas, x, y, yspeed, length, color='blue'):
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.length = length
        self.canvas = canvas
        self.line = canvas.create_line(self.x, self.y, self.x, self.y+length, fill=color)

    def move(self):
        self.y += self.yspeed
        self.canvas.move(self.line, 0, self.yspeed)
        if self.y > 500:
            self.canvas.move(self.line, 0, -(500+self.length))
            self.y -= 500 + self.length


def redraw():
    for drop in drops:
        drop.move()

    root.after(10, redraw)


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

drops = [Raindrop(canvas, x=randint(0, 500), y=randint(0, 500), 
                  yspeed=randint(1, 7), length=randint(50, 100)) for i in range(101)]

redraw()

root.mainloop()