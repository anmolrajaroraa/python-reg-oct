# def outer():
#     print("Outer called")
#     def inner1():
#         return "inner1 fn"
#     def inner2():
#         return "inner2 fn"
#
#     return inner1,inner2
#     #print( inner1( ) )
#     #print(inner2())
#
#
# result = outer()
# print(result[0]())
# print(outer()[1]())




'''x = 10
y = 20
def add():
    global x
    x = x + 10
    return x + y

print(add())
print(x)'''











def outer():
    x = 10
    print("X in outer is",x)
    def inner():
        global x
        x = 100
        print("X in inner is",x)

    inner()
    print( "X in outer is" , x )


outer()
print("X globally is ", x)