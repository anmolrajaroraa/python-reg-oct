#try -> write all logic here
#except -> catches all the exceptions and do the needful
#else -> will execute if try completes normally, if exception occurs, else will not execute

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#
#     quotient = num1 / num2
#
#     print(quotient)
# except TypeError:
#     print("Cannot divide two strings")
# #except ValueError:
# #    print("Please enter valid integers")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except BaseException as error:
#     print("Some error occured", error)





def atm():
    balance = 10000
    pin = 1234
    pinInput = int(input("Enter pin: "))
    #if pin != pinInput:
        #raise ValueError("Pin incorrect")
    assert(pin == pinInput), "Pin incorrect"
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
    print("Remaining balance is",balance)

try:
    atm()
except ValueError as error:
    print(error)
except AssertionError as error:
    print(error)
except BaseException as error:
    print("Sorry can't proceed further", error)
else:
    print("Thanks for visiting us!")
