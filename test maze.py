# import
import turtle
from time import sleep

# init screen, turtle
window = turtle.Screen()
window.setup(300, 300, None, None)
goal = turtle.Turtle()
turt = turtle.Turtle()
turt.speed(0)
goal.speed(0)


# turtle instructions
def drawBoard():
    goal.ht()
    goal.pu()
    goal.goto(75, -125)
    turt.ht()
    turt.pu()
    turt.goto(-100, 100)
    turt.pd()
    turt.right(90)
    turt.forward(200)
    turt.left(90)
    turt.forward(150)
    turt.pu()
    turt.forward(50)
    turt.pd()
    turt.left(90)
    turt.forward(200)
    turt.left(90)
    turt.forward(100)
    turt.pu()
    turt.forward(50)
    turt.pd()
    turt.forward(50)
    turt.left(180)
    turt.forward(50)
    turt.left(180)
    turt.left(90)
    turt.forward(100)
    turt.pu()
    turt.left(180)
    turt.forward(100)
    turt.right(90)
    turt.forward(50)
    turt.right(90)
    turt.forward(50)
    turt.pd()
    turt.forward(100)
    turt.pu()
    turt.left(180)
    turt.forward(150)
    turt.right(90)
    turt.forward(50)
    turt.right(90)
    turt.forward(50)
    turt.pd()
    turt.forward(100)
    turt.pu()
    turt.right(180)
    turt.forward(150)
    turt.left(90)
    turt.forward(150)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(100)
    turt.pd()
    turt.forward(50)
    turt.pu()
    turt.right(90)
    turt.forward(100)
    turt.right(90)
    turt.forward(50)
    turt.pd()
    turt.forward(100)
    turt.pu()
    turt.goto(-25, 125)
    turt.left(90)
    turt.st()
    turt.shape("turtle")
    turt.color("green", "green")
    goal.shape("turtle")
    goal.color("red", "red")
    goal.left(90)
    goal.st()


# gameplay
def play():
    # define keys
    def up():
        turt.forward(50)

    def left():
        turt.speed(0)
        turt.left(90)
        turt.speed(1)

    def right():
        turt.speed(0)
        turt.right(90)
        turt.speed(1)

    turt.pd()
    turt.speed(1)

    window.onkey(up, "Up")
    window.onkey(left, "Left")
    window.onkey(right, "Right")
    window.listen()


# runtime
drawBoard()
while str(turt.pos()) != str(goal.pos()):
    print(str(turt.pos()) + " : " + str(goal.pos()))
    play()
else:
    sleep(1)
    window.bye()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nyou win")
    sleep(4)
    quit()

# close
window.mainloop()
