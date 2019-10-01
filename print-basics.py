#basic calculator

a = 10  #integer
b = 20  #integer

total = a + b  #integer

#int(), str(), bool() are used for type casting

print("Total is" + str(total))  #string concatenation (joining)
print("Total is", total)  #benefits - a blank space is provided and type conversion is done automatically
print("Sum of", a ,"and", b ,"is", total)
print("Sum of {} and {} is {}".format(a,b,total))
print(f"Sum of {a} and {b} is {total}")
