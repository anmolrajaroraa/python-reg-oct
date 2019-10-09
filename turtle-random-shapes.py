import turtle
import random

fred = turtle.Pen()

fred.width(4)
fred.shape('turtle')
fred.turtlesize(2,2)
fred.speed(0)

colors = ['black', 'blue', 'red', 'green', 'yellow', 'maroon', 'violet', 'magenta', 'grey', 'turquoise']
shapes = ['square', 'circle', 'dot', 'triangle', 'hexagon']
coordinates = list(range(-300,301))

for i in range(50):

    turtleColor = random.choice(colors)
    print(turtleColor)
    fred.color(turtleColor)

    #x = random.choice(coordinates)
    #y = random.choice(coordinates)
    #print(x,y)
    fred.penup()
    #fred.setposition(x,y)
    fred.pendown()

    shape = random.choice(shapes)
    print(shape)

    '''if shape == 'square' :
        for i in range(4) :
            fred.forward( 100 )
            fred.left( 90 )
    elif shape == 'circle' :
        fred.circle( 50 )  # radius
    elif shape == 'dot' :
        fred.dot( 100 )  # diameter
    elif shape == 'triangle':'''
    for j in range(3):
        fred.forward(10 * i)
        fred.left(120)
    fred.right( 150 )
    fred.penup( )
    fred.forward( 5 )
    fred.pendown( )
    fred.left( 150 )
    '''fred.right(150)
    fred.penup()
    fred.forward(5)
    fred.pendown()
    fred.left(135)'''
    '''else:
        for i in range(6):
            fred.forward(100)
            fred.left(60)'''

while True:
    pass