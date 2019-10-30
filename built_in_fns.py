def temp_convert(c):
    return 9/5 * c + 32

temp = [0,11,22,33,44,55,66,77,88,99]
#f_temp = temp_convert(temp)
#print(f_temp)
f_temp = []

for t in temp:
    f_temp.append(temp_convert(t))

print(f_temp)

#expression   for loop    if  (optional)   -> list comprehension

f_temp = [temp_convert(t) for t in temp]
print(f_temp)

f_temp = [  (lambda c : 9/5 * c + 32)(t)    for t in temp]
print(f_temp)

f_temp = list(map(temp_convert,temp))
print(f_temp)

f_temp = list(map(lambda c: 9/5 * c + 32,temp))
print(f_temp)