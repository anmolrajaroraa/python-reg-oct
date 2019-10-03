import turtle
import random

'''choice = input("What do you want to draw: ")

gameContinue = true

s = turtle.Screen()
s.bgcolor('black')

fred = turtle.Pen()
fred.width(4)
fred.shape('turtle')
fred.color('white')
fred.turtlesize(2,2)'''

gameChoices = ['stone', 'paper', 'scissors']
cpuChoice = random.choice(gameChoices)
print(cpuChoice)

'''if choice == 'square':
    for i in [ 0 , 1 , 2 , 3 ] :
        fred.forward( 100 )
        fred.left( 90 )
elif choice == 'circle':
    fred.circle(50)   #radius
elif choice == 'dot':
    fred.dot(100)   #diameter
else:
    print('Shape not found!')

while gameContinue:
    pass
'''

if userChoice == 'end':
    #gameContinue = False
    quit()
elif userChoice == 'stone':
    if cpuChoice == 'stone':
        print("game draw")
    elif cpuChoice == 'paper':
        print('Cpu won')
        cpuWins = cpuWins + 1
    else:
        print('User won')
        userWins = userWins + 1
elif userChoice == 'paper':
    pass
elif userChoice == 'scissors':
    pass
else:
    print('Wrong choice')

quit()
