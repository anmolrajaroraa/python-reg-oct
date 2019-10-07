import turtle
import random

fred = turtle.Pen()

fred.width(4)
fred.shape('turtle')
fred.turtlesize(2,2)
fred.speed(0)
colors = ['black', 'blue', 'red', 'green', 'yellow', 'maroon', 'violet', 'magenta', 'grey', 'turquoise']
for i in range(100):
    turtleColor = random.choice( colors )
    print( turtleColor )
    fred.color( turtleColor )
    fred.circle((5 * i))
    fred.left(10)

    '''fred.right(90)
    fred.penup()
    fred.forward(10)
    fred.pendown()
    fred.left(90)'''

    #For triangle
    '''for j in range(3):
            fred.forward(5 * i)
            fred.left(120)'''


while True:
    pass