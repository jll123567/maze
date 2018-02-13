# import
import turtle
from time import sleep

# init screen, turtle
window = turtle.Screen()
turt = turtle.Turtle()
turt.speed(5)

# turtle instructions
for _ in range(0,10):
    for _ in range(0, 18):
        turt.forward(50)
        turt.left(20)

    for _ in range(0, 18):
        turt.forward(50)
        turt.right(20)

turt.ht()
sleep(3)
turtle.bye()

# window await
window.mainloop()
