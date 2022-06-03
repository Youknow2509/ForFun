from turtle import *
import turtle
wn = turtle.Screen()
wn.setup(width=1000, height=800)
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()
if __name__ == '__main__':
    pensize(5)
    speed(100)
    my_goto(-100, 100)
    write('dm thinh', font=("Bradley Hand ITC", 30, "bold"))
    mainloop() 

