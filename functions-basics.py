# a = 10
# b = 20
# c = 50
#
# #def fn_name(  args  )
# def add():
#     print(a + b)
#
# def sub(a = 0,b = 0):   #default arguments
#     print(a - b)
#
# def div(a = 100, b = 1):
#     print(a/b)
#
# def mul(a = 1, b =1):
#     c = a * b
#     #return None
#     #return c
#     return a * b
#
# def calc(a = 1, b =1):
#     print()
#     return a + b, a - b, a * b, a / b, a % b, a ** b   #packing
#     #return a - b
#     #return a * b
#     #return a / b
#
# #f name   ( arguments )
# add()    #  fn call
# sub(100,50)
# sub(10)
# sub()
# div(50, b=50)  #mapping the arguments
#
# div(c,b = 50)
#
# result = mul(100,200)
# print(result)
#
# results = calc(100,50)
# print(results)
#
# add_result, sub_result, mul_result, div_result , *otherResult = calc(33,22)    #unpacking
#
# #    *args  -> multiple args variable  -> creates a tuple/list
# #    **kwargs  -> keyword arguments  -> creates a dictionary
#
# print(add_result)
# print(sub_result)
# print(mul_result)
# print(div_result)
# print(otherResult)

def student(id, name, course, address, **otherDetails):
    print(f'''   Id : {id}
    Name : {name}
    Course : {course}
    Address : {address}
    Other Details : {otherDetails}''')

student(101,'Ram' , 'BTech', 'Rohini')
student( 101, 'Ram' , 'BTech', marks=26, age = 26, contact= '1234', attendance = 50)
student( 101, 'Ram' , 'BTech', marks=26, age = 26, contact= '1234', attendance = 50, address = 'Rohini')