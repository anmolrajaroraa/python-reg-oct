def calc(x,y,operator):
    print(eval(x + operator + y))

print('''
1. Add
2. Subtract
3. Multiply
4. Divide''')

choice = input("Enter your choice: ")

operators = {"1" : '+', "2" : '-', "3": '*', "4": '/'}

num1 = input( "Enter first number: " )
num2 = input( "Enter second number: " )

calc(num1,num2,operators[choice])