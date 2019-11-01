# def temp_convert(c):
#     return 9/5 * c + 32
#
# temp = [0,11,22,33,44,55,66,77,88,99]
# #f_temp = temp_convert(temp)
# #print(f_temp)
# f_temp = []
#
# for t in temp:
#     f_temp.append(temp_convert(t))
#
# print(f_temp)
#
# #expression   for loop    if  (optional)   -> list comprehension
#
# f_temp = [temp_convert(t) for t in temp]
# print(f_temp)
#
# f_temp = [  (lambda c : 9/5 * c + 32)(t)    for t in temp]   #anonymous fn
# print(f_temp)
#
# f_temp = list(map(temp_convert,temp))
# print(f_temp)
#
# f_temp = list(map(lambda c: 9/5 * c + 32,temp))
# print(f_temp)
#
#
#
# def even(n):
#     return n % 2 == 0
#
# numbers = list(range(1,101))
#
# #newList = [number for number in numbers if even(number)]
#
# newList = list(filter(lambda n:n % 2 == 0, numbers))
#
# print(newList)
#
#
# names = ['Ram', 'Shyam', 'Mohan']
#
# for i in range(len(names)):
#     print(f"{i+1}. {names[i]}")
#
# for index,name in enumerate(names):
#     print(f"{index+1}. {name}")

list1 = [i**2 if i % 2 ==0 else 0 for i in range(1,101)]
print(list1)