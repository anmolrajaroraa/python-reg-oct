import random

userWins = 0
cpuWins = 0
draw = 0

while True:

    print('''1. Stone
2. Paper
3. Scissors''')

    print(f"Score -> User : {userWins}, CPU : {cpuWins}, Drawn : {draw}, Matches Played : {userWins + cpuWins + draw}")
    if userWins >= 3 or cpuWins >= 3:
        quit()
    userChoice = int(input( "Enter your choice : " ))
    gameChoicesList = ['stone', 'paper', 'scissors']
    gameChoices = range(3)
    cpuChoice = random.choice( gameChoices ) + 1
    print(f"User Choice : {gameChoicesList[userChoice - 1]}, CPU Choice : {gameChoicesList[cpuChoice - 1]}")

    if userChoice == 1:
        if cpuChoice == 1:
            print("game draw")
            draw = draw + 1
        elif cpuChoice == 2:
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1
    elif userChoice == 2:
        if cpuChoice == 2:
            print("game draw")
            draw = draw + 1
        elif cpuChoice == 3:
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1
    elif userChoice == 3:
        if cpuChoice == 3:
            print("game draw")
            draw = draw + 1
        elif cpuChoice == 1:
            print('Cpu won')
            cpuWins = cpuWins + 1
        else:
            print('User won')
            userWins = userWins + 1
    else:
        print('Wrong choice')