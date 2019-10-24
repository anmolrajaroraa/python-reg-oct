Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> keys = ['id', 'name', 'course', 'address', 'contact']
>>> dict.fromkeys(keys)
{'id': None, 'name': None, 'course': None, 'address': None, 'contact': None}
>>> dict.fromkeys(keys, '')
{'id': '', 'name': '', 'course': '', 'address': '', 'contact': ''}
>>> 
>>> student = {
	'id' : 101,
	'name' : 'Ram',
	'course' : 'BTech',
	'address' : {
		'home' : 'rohini',
		'hostel' : 'janakpuri'
		},
	'contact' : ['1234' , '4567']
	}
>>> student['address']
{'home': 'rohini', 'hostel': 'janakpuri'}
>>> student.get('address')
{'home': 'rohini', 'hostel': 'janakpuri'}
>>> student.get('address').get('home')
'rohini'
>>> student.pop('course')
'BTech'
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'contact': ['1234', '4567']}
>>> student.popitem()
('contact', ['1234', '4567'])
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}}
>>> 
>>> student['course'] = 'BTech'
>>> student['course'] = 'Fashion'
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion'}
>>> 
>>> student.setdefault('address', 'rohini')
{'home': 'rohini', 'hostel': 'janakpuri'}
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion'}
>>> student.setdefault('contact', 100)
100
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion', 'contact': 100}
>>> student.setdefault('contact', 101)
100
>>> 
>>> scholarship = {
	'amount' : 10000,
	'quota' : 'sports'
	}
>>> 
>>> student.update(scholarship)
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion', 'contact': 100, 'amount': 10000, 'quota': 'sports'}
>>> 
>>> student['scholarship'] = scholarship
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion', 'contact': 100, 'amount': 10000, 'quota': 'sports', 'scholarship': {'amount': 10000, 'quota': 'sports'}}
>>> 
>>> print("""
Id = {id}
Name = {name}
Address = {address}
Course = {course}
Contact = {contact}
Scholarship = {scholarship}
""")

Id = {id}
Name = {name}
Address = {address}
Course = {course}
Contact = {contact}
Scholarship = {scholarship}

>>> print(f"""
Id = {id}
Name = {name}
Address = {address}
Course = {course}
Contact = {contact}
Scholarship = {scholarship}
""")
Traceback (most recent call last):
  File "<pyshell#52>", line 8, in <module>
    """)
NameError: name 'name' is not defined
>>> print("""
Id = {id}
Name = {name}
Address = {address}
Course = {course}
Contact = {contact}
Scholarship = {scholarship}
""".format_map(student))

Id = 101
Name = Ram
Address = {'home': 'rohini', 'hostel': 'janakpuri'}
Course = Fashion
Contact = 100
Scholarship = {'amount': 10000, 'quota': 'sports'}


>>> tuple1 = (1,2,3,4,5,'hello', 'bye', True)
'
>>> tuple1 = (1,2,3,4,5,'hello', 'bye', True)
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> tuple1[0] = 100
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    tuple1[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del tuple1[0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del tuple1[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> set1 = {1,2,3,4,5,'hello', 'bye', True} #unique numbers, hashing algorithm is used - randomly placed in memory
>>> set1
{1, 2, 3, 4, 5, 'bye', 'hello'}
>>> set1 = {1,2,3,4,5,'hello', 'bye', True, 'Anmol'} #unique numbers, hashing algorithm is used - randomly placed in memory
>>> set1
{1, 2, 3, 4, 5, 'bye', 'Anmol', 'hello'}
>>> for element in set1:
	print(element)

	
1
2
3
4
5
bye
Anmol
hello
>>> dir(set)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> set1.add(False)
>>> set1
{False, 1, 2, 3, 4, 5, 'bye', 'Anmol', 'hello'}
>>> set1.add(0)
>>> set1
{False, 1, 2, 3, 4, 5, 'bye', 'Anmol', 'hello'}
>>> 
>>> set2 = {False, 1, 2, 3, 4}
>>> 
>>> #set1 - set2
>>> set1.difference(set1,set2)
set()
>>> set1.difference(set2)
{'bye', 'hello', 5, 'Anmol'}
>>> 
>>> set1 - set2
{'bye', 'hello', 5, 'Anmol'}
>>> 
>>> 
>>> 
>>> set3 = {100,200,300, 'Anmol'}
>>> 
>>> set1 - set2
{'bye', 'hello', 5, 'Anmol'}
>>> 
>>> set1.difference(set2, set3)
{'bye', 'hello', 5}
>>> set1 - set2 - set3
{'bye', 'hello', 5}
>>> set1.difference_update(set2, set3)
>>> set1
{5, 'bye', 'hello'}
>>> set1 = {1,2,3,4,5,'hello', 'bye', True, 'Anmol'} #unique numbers, hashing algorithm is used - randomly placed in memory
>>> set4 = set1.difference(set2, set3)
>>> set4
{'bye', 'hello', 5}
>>> 
>>> set1.discard(5)
>>> set1
{1, 2, 3, 4, 'bye', 'Anmol', 'hello'}
>>> set1.discard(5)
>>> set1
{1, 2, 3, 4, 'bye', 'Anmol', 'hello'}
>>> 
>>> 
>>> set1.intersection(set2)
{1, 2, 3, 4}
>>> set1.union(set2)
{False, 1, 2, 3, 4, 'bye', 'Anmol', 'hello'}
>>> 
>>> 
>>> set4 = {11, 22, 33, 44, 'byee', 'Anmoll', 'helloo'}
>>> set1.isdisjoint(set4)
True
>>> set1.isdisjoint(set2)
False
>>> set1.issuperset(set2)
False
>>> set1
{1, 2, 3, 4, 'bye', 'Anmol', 'hello'}
>>> set2
{False, 1, 2, 3, 4}
>>> set1.add(0)
>>> set1.issuperset(set2)
True
>>> set2.issubset(set1)
True
>>> set1.remove(5)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    set1.remove(5)
KeyError: 5
>>> set1.remove(4)
>>> set1
{0, 1, 2, 3, 'bye', 'Anmol', 'hello'}
>>> set1.pop()
0
>>> set1.pop()
1
>>> set1.pop()
2
>>> set1.pop()
3
>>> set1.pop()
'bye'
>>> set1.pop()
'Anmol'
>>> set1.pop()
'hello'
>>> help(set.symmetric_difference)
Help on method_descriptor:

symmetric_difference(...)
    Return the symmetric difference of two sets as a new set.
    
    (i.e. all elements that are in exactly one of the sets.)

>>> #set1 - set2 + set2 - set1
>>> 
>>> set1.symmetric_difference(set2)
{False, 1, 2, 3, 4}
>>> set1
set()
>>> set1 = {1, 2, 33, 44, 'bye', 'Anmoll', 'hello'}
>>> set2
{False, 1, 2, 3, 4}
>>> set1.symmetric_difference(set2)
{False, 'hello', 33, 3, 4, 'Anmoll', 'bye', 44}
>>> 
>>> 
>>> (set1 - set2).update(set2 - set)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    (set1 - set2).update(set2 - set)
TypeError: unsupported operand type(s) for -: 'set' and 'type'
>>> (set1 - set2).update(set2 - se1)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    (set1 - set2).update(set2 - se1)
NameError: name 'se1' is not defined
>>> (set1 - set2).update(set2 - set1)
>>> (set1 - set2).union(set2 - set1)
{False, 33, 'hello', 3, 4, 'Anmoll', 'bye', 44}
>>> 
>>> 
>>> a = 10
>>> b = 20
>>> c = a - b
>>> if a > b:
	c = a - b
else:
	c = b - a

	
>>> c
10
>>> c = a - b if a > b
SyntaxError: invalid syntax
>>> c = a - b if a > b else b - a
>>> c = (a - b) if (a > b) else ( b - a if b > a else 0 )
>>> c
10
>>> a  = 100
>>> b = 20
>>> c = (a - b) if (a > b) else ( b - a if b > a else 0 )
>>> c
80
>>> b = 100
>>> c = (a - b) if (a > b) else ( b - a if b > a else 0 )
>>> c
0
>>> evenList = []
>>> for i in range(1,101):
	if i % 2 == 0 :
		evenList.append(i)

		
>>> evenList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> 
>>> newList = [i for i in range(1,101) if i % 2 == 0]
>>> newList
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> 
>>> 
>>> #  expression to append things     for loop     if condition (optional)
>>> 
>>> newList = [i**2 for i in range(1,101) if i % 2 == 0]
>>> newList
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604, 10000]
>>> newList = [i**2 for i in range(1,101) if i % 2 == 0 or i % 3 == 0]
>>> newList
[4, 9, 16, 36, 64, 81, 100, 144, 196, 225, 256, 324, 400, 441, 484, 576, 676, 729, 784, 900, 1024, 1089, 1156, 1296, 1444, 1521, 1600, 1764, 1936, 2025, 2116, 2304, 2500, 2601, 2704, 2916, 3136, 3249, 3364, 3600, 3844, 3969, 4096, 4356, 4624, 4761, 4900, 5184, 5476, 5625, 5776, 6084, 6400, 6561, 6724, 7056, 7396, 7569, 7744, 8100, 8464, 8649, 8836, 9216, 9604, 9801, 10000]
>>> newList = [i**2 for i in range(1,101) if i % 2 == 0 or i % 3 == 0 else 'X']
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> newList = [i**2 if i % 2== 0 or i % 3 == 0 else 'X' for i in range(1,101)]
>>> newList
['X', 4, 9, 16, 'X', 36, 'X', 64, 81, 100, 'X', 144, 'X', 196, 225, 256, 'X', 324, 'X', 400, 441, 484, 'X', 576, 'X', 676, 729, 784, 'X', 900, 'X', 1024, 1089, 1156, 'X', 1296, 'X', 1444, 1521, 1600, 'X', 1764, 'X', 1936, 2025, 2116, 'X', 2304, 'X', 2500, 2601, 2704, 'X', 2916, 'X', 3136, 3249, 3364, 'X', 3600, 'X', 3844, 3969, 4096, 'X', 4356, 'X', 4624, 4761, 4900, 'X', 5184, 'X', 5476, 5625, 5776, 'X', 6084, 'X', 6400, 6561, 6724, 'X', 7056, 'X', 7396, 7569, 7744, 'X', 8100, 'X', 8464, 8649, 8836, 'X', 9216, 'X', 9604, 9801, 10000]
>>> 
>>> student
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion', 'contact': 100, 'amount': 10000, 'quota': 'sports', 'scholarship': {'amount': 10000, 'quota': 'sports'}}
>>> keys = student.keys()
>>> keys = student.values()
>>> keys = student.keys()
>>> values = student.values()
>>> 
>>> keys
dict_keys(['id', 'name', 'address', 'course', 'contact', 'amount', 'quota', 'scholarship'])
>>> values
dict_values([101, 'Ram', {'home': 'rohini', 'hostel': 'janakpuri'}, 'Fashion', 100, 10000, 'sports', {'amount': 10000, 'quota': 'sports'}])
>>> 
>>> student2 = {i:j for i,j in keys, values}
SyntaxError: invalid syntax
>>> student2 = {i:j for i,j in (keys, values)}
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    student2 = {i:j for i,j in (keys, values)}
  File "<pyshell#197>", line 1, in <dictcomp>
    student2 = {i:j for i,j in (keys, values)}
ValueError: too many values to unpack (expected 2)
>>> student2 = {i:j for i,j in enumerate(keys, values)}
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    student2 = {i:j for i,j in enumerate(keys, values)}
TypeError: 'dict_values' object cannot be interpreted as an integer
>>> student2 = {i:j for (i,j) in enumerate(keys, values)}
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    student2 = {i:j for (i,j) in enumerate(keys, values)}
TypeError: 'dict_values' object cannot be interpreted as an integer
>>> 
>>> 
>>> keys = [key for key in student]
>>> values = [value for value in student]
>>> student2 = {i:j for i,j in keys, values}
SyntaxError: invalid syntax
>>> student2 = {i:j for i,j in (keys, values)}
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    student2 = {i:j for i,j in (keys, values)}
  File "<pyshell#205>", line 1, in <dictcomp>
    student2 = {i:j for i,j in (keys, values)}
ValueError: too many values to unpack (expected 2)
>>> student2 = {i:j for (i,j) in enumerate(keys, values)}
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    student2 = {i:j for (i,j) in enumerate(keys, values)}
TypeError: 'list' object cannot be interpreted as an integer
>>> student2 = {i:j for (i,j) in zip(keys, values)}
>>> student2
{'id': 'id', 'name': 'name', 'address': 'address', 'course': 'course', 'contact': 'contact', 'amount': 'amount', 'quota': 'quota', 'scholarship': 'scholarship'}
>>> 
>>> 
>>> 
>>> keys = student.keys()
>>> values = student.values()
>>> zip(keys,values)
<zip object at 0x10a99adc8>
>>> list(zip(keys,values))
[('id', 101), ('name', 'Ram'), ('address', {'home': 'rohini', 'hostel': 'janakpuri'}), ('course', 'Fashion'), ('contact', 100), ('amount', 10000), ('quota', 'sports'), ('scholarship', {'amount': 10000, 'quota': 'sports'})]
>>> 
>>> 
>>> student2 = {i:j for i,j in zip(keys, values)}
>>> student2
{'id': 101, 'name': 'Ram', 'address': {'home': 'rohini', 'hostel': 'janakpuri'}, 'course': 'Fashion', 'contact': 100, 'amount': 10000, 'quota': 'sports', 'scholarship': {'amount': 10000, 'quota': 'sports'}}
>>> 
>>> 
>>> 
>>> set1
{1, 2, 33, 'bye', 44, 'hello', 'Anmoll'}
>>> fixSet = frozenset(set1)
>>> fixSet
frozenset({1, 2, 33, 'hello', 'Anmoll', 'bye', 44})
>>> fixSet.add(100)
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    fixSet.add(100)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> dir(frozenset)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> 
