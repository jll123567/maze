# import
import turtle

# init screen, turtle
window = turtle.Screen()
turt = turtle.Turtle()
moveable = turtle.Turtle(shape="turtle")
turt.speed(5)
moveable.speed(2)
moveable.color("green", "green")


# turtle instructions
for _ in range(0, 3):
    for _ in range(0, 18):
        turt.forward(50)
        turt.left(20)

    for _ in range(0, 18):
        turt.forward(50)
        turt.right(20)
turt.ht()


# key functions
def up():
    moveable.forward(10)


def left():
    moveable.left(10)


def right():
    moveable.right(10)


# key events
window.onkeypress(up, "w")
window.onkeypress(left, "a")
window.onkeypress(right, "d")

# window await
window.listen()
window.mainloop()
