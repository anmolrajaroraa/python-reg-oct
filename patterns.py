'''
$$$$*
$$$***
$$*****
$*******
*********
$*******
$$*****
$$$***
$$$$*
'''

for i in range(5):   #0,1,2,3,4
    for j in range(i+1):  #1,2,3,4,5
        print('*', end = '')
    print()

print(list(reversed(range(10))))

for i in range(5):   #0,1,2,3,4
    for j in range(4-i):     # 4,3,2,1,0   -> 4-i
        print(' ',end='')
    for k in range(i+1):   #1,2,3,4,5
        print('*',end='')
    print()

print()

for i in range(5):   #0,1,2,3,4
    for j in range(4-i):     # 4,3,2,1,0   -> 4-i
        print(' ',end='')
    for k in range(2*i+1):   #1,3,5,7,9
        print('*',end='')
    print()

print()

print("*" * 10)

print()

for i in range(5):   #0,1,2,3,4
    print('*' * (i + 1))

print()

for i in range(5):   #0,1,2,3,4
    print(' ' * (4-i),end='')
    print('*' * (2*i+1))