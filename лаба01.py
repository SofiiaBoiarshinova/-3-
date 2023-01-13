from tkinter import *
from math import pi, cos, sin
import time
root = Tk()
reverse, speed, check = True, 0.1, False


def inc_speed():
    global speed
    speed = speed * 0.5


def dec_speed():
    global speed
    speed = speed * 1.5


def rev():
    global reverse
    if reverse:
        reverse = False
    else:
        reverse = True


def stop_anim():
    global check
    check = True
    root.destroy()





def motion():
    n = 500
    x = 295
    dtheta = (2 * pi) / n
    r = 200
    xc = x - r
    yc = r
    theta = 0
    for i in range(10):
        for a in range(n):
            if check:
                break
            else:
                if reverse:
                    theta -= dtheta
                else:
                    theta += dtheta
                x = 290 + (r * cos(theta))
                y = 290 + (r * sin(theta))
                point = c.create_oval(x, y, x + 20, y + 20, fill='white', tag='point')
                root.update()
                time.sleep(speed)
                c.delete('point')
                root.update()


c = Canvas(root, width=600, height=600, bg="black")
c.pack()
trajectory = c.create_oval(100, 100, 500, 500, outline='green')
but1 = Button(text='+ speed', command=inc_speed)
but2 = Button(text='- speed', command=dec_speed)
but3 = Button(text='reverse', command=rev)
but1.pack()
but2.pack()
but3.pack()

motion()
root.mainloop()
