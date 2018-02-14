# import
import turtle
from time import sleep

# init screen, turtle
window = turtle.Screen()
turt = turtle.Turtle()
turt.speed(5)

# turtle instructions
#for _ in range(0,1):
#    for _ in range(0, 18):
#        turt.forward(50)
#        turt.left(20)
#
#    for _ in range(0, 18):
#        turt.forward(50)
#        turt.right(20)

def up():
    turt.forward(10)
def left():
    turt.left(10)
def right():
    turt.right(10)
while True==True:
    turtle.onkey(up(), "Up")
    turtle.onkey(left(), "Left")
    #turtle.onkey(right(), "Right")

# window await
turtle.listen()
window.mainloop()