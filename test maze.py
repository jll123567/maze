# import
import turtle
from time import sleep

# init screen, turtle
turtle.setup(300, 300, None, None)
window = turtle.Screen()
turt= turtle.Turtle()
turt.speed(0)


# turtle instructions
def drawBoard():
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
    turt.goto(-25,125)
    turt.left(90)
    turt.st()
    turt.shape("turtle")
    turt.color("green", "green")


# gameplay
def play():
# define keys
    def up():
        turt.forward(50)
    def down():
        turt.backward(50)
    def left():
        turt.left(90)
    def right():
        turt.right(90)
    turt.pd()
    turt.speed(1)


    print(window.onkey(up(),"Up"))
        #turtle.onkeyrelease(down(),"Down")
        #turtle.onkeyrelease(left(),"Left")
        #turtle.onkeyrelease(right(),"Right")





#runtime
drawBoard()
while turt.pos() != (125,-125):
    print("working on it")
    #play()
    turt.goto((125,-125),None)
else:
    turtle.bye()


# close
window.mainloop()
