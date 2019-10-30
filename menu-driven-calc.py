def takeInput():
    num1 = int( input( "Enter first number: " ) )
    num2 = int( input( "Enter second number: " ) )
    return num1,num2

def add():
    x,y = takeInput()
    print(x + y)
def sub():
    x , y = takeInput( )
    print(x - y)
def mul():
    x , y = takeInput( )
    print(x * y)
def div():
    x , y = takeInput( )
    print(x / y)
def errorHandler(*args):
    print('Invalid choice')

while True:
    print('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit''')

    choice = input("Enter your choice: ")

    '''if choice < 1 or choice > 5:
        print( "Invalid choice" )
        continue
    elif choice == 5:
        quit()'''

    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))

    '''if choice == 1:
        add(num1, num2)
    elif choice == 2:
        sub(num1,num2)
    elif choice == 3:
        mul(num1,num2)
    elif choice == 4:
        div(num1,num2)'''

    '''switch(choice):
        case 1: add()
        case 2: sub()
        default: quit()'''

    operations = {"1" : add, "2" : sub, "3" : mul, "4" : div, "5": quit}
    #operations[choice](num1,num2)
    operations.get(choice,errorHandler)()
    #print(operations)