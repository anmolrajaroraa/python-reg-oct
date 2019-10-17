# number = int(input("Enter number to check if it's prime or not: "))
#
# isPrime = True
#
# if number <= 1:
#     print('Invalid number')
# else:
#     for i in range(2, number//2 + 1):
#         if number % i == 0:
#             print("Number is not prime")
#             isPrime = False
#             break
#
# if isPrime:
#     print('Number is prime')

number = int(input("Enter number to check if it's prime or not: "))

if number <= 1:
    print('Invalid number')
else:
    for i in range(2, number//2 + 1):
        if number % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")