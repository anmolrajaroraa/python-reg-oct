Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = a
>>> b
10
>>> type(a)
<class 'int'>
>>> #class (blueprint) -> object (model, instance)
>>> #everything in python is an object
>>> 99xdfc
SyntaxError: invalid syntax
>>> a
10
>>> b
10
>>> id(a)
4485873104
>>> hex(4485873104)   #convert decimal to hexadecimal number
'0x10b60fdd0'
>>> id(b)
4485873104
>>> hex(4485873104)
'0x10b60fdd0'
>>> id(a) == id(b) # = -> assignment operator, == -> comparison operator
True
>>> c = 20
>>> print(20)
20
>>> id(c)
4485873424
>>> hex(4485873424)
'0x10b60ff10'
>>> id(a) == id(c)
False
>>> input.__doc__
'Read a string from standard input.  The trailing newline is stripped.\n\nThe prompt string, if given, is printed to standard output without a\ntrailing newline before reading input.\n\nIf the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.\nOn *nix systems, readline is used if available.'
>>> print(input.__doc__)
Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available.
>>> input("Enter your name: ")
Enter your name: Anmol
'Anmol'
>>> input("Enter a number: ")
Enter a number: 10
'10'
>>> x = input("Enter a number: ")
Enter a number: 10
>>> print(x)
10
>>> y = input("Enter a number: ")
Enter a number: 20
>>> print(y)
20
>>> type(x)
<class 'str'>
>>> type(y)
<class 'str'>

>>> x - y
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x - y
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> int(x) - int(y)
-10
>>> x + y
'1020'
>>> int(x) + int(y)
30
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> str1 = 'python is very easy to learn'
>>> id(str1)
4537461856
>>> hex(id(str1))
'0x10e742c60'
>>> str1.capitalize()
'Python is very easy to learn'
>>> #print(str1.format(a,b,c))
>>> str1.casefold()
'python is very easy to learn'
>>> str1.lower()
'python is very easy to learn'
>>> str2 = 'HDKDLajdheuj'
>>> str1.casefold()
'python is very easy to learn'
>>> str2.casefold()
'hdkdlajdheuj'
>>> str2.lower()
'hdkdlajdheuj'
>>> print(str1)
python is very easy to learn
>>> len(str1)
28
>>> str1.center(100)
'                                    python is very easy to learn                                    '
>>> str1.center(70)
'                     python is very easy to learn                     '
>>> str1.center(250)
'                                                                                                               python is very easy to learn                                                                                                               '
>>> str1.center(120)
'                                              python is very easy to learn                                              '
>>> str1.center(20)
'python is very easy to learn'
>>> str1.center(100, '-')
'------------------------------------python is very easy to learn------------------------------------'
>>> #first argument in center is width for the new string and second is the character that needs to be filled
>>> str1.count('e')
3
>>> str1
'python is very easy to learn'
>>> str1.count('learn')
1
>>> str1 = 'python is very easy to learn learn'
>>> str1.count('learn')
2
>>> str1
'python is very easy to learn learn'
>>> str1[0]
'p'
>>> str1[1]
'y'
>>> str1[2]
't'
>>> str1[3]
'h'
>>> str1[4]
'o'
>>> str1[5]
'n'
>>> len(str1)
34
>>> str1[33]
'n'
>>> str1[34]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    str1[34]
IndexError: string index out of range
>>> str1.count('e')
4
>>> str1.find('e')
11
>>> str1[11]
'e'
>>> str1
'python is very easy to learn learn'
>>> str1.find('e')
11
>>> str1.find('e', 12)
15
>>> str1.find('e', 16)
24
>>> str1.find('e', 25)
30
>>> str1.find('e', 31)
-1
>>> str1.index('e')
11
>>> str1.index('w')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    str1.index('w')
ValueError: substring not found
>>> str1.find('e', 31)
-1
>>> str1.index('e', 31)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    str1.index('e', 31)
ValueError: substring not found
>>> #find() gives me index of the first occurence of substring
>>> #find() gives -1 if substring is not found
>>> #index() is same as find(), only difference is index() generates error of substring is not found
>>> str1.find('learn')
23
>>> str1[23]
'l'
>>> str1.find('learn', 24)
29
>>> str1
'python is very easy to learn learn'
>>> print('abc')
abc
>>> print('æłß')
æłß
>>> #python is utf-8 based
>>> print('राम ')
राम 
>>> #ASCII codes - 127 characters
>>> print('æłß')
æłß
>>> strNew = 'æłß'
>>> strNew.encode()
b'\xc3\xa6\xc5\x82\xc3\x9f'
>>> strNew  = 'æabcdłefghßjl;09'
>>> strNew.encode()
b'\xc3\xa6abcd\xc5\x82efgh\xc3\x9fjl;09'
>>> encodedString = strNew.encode()
>>> type(encodedString)
<class 'bytes'>
>>> #internationalization (I18N)
>>> encodedString.decode()
'æabcdłefghßjl;09'
>>> decodedString = encodedString.decode()
>>> type(decodedString)
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str1
'python is very easy to learn learn'
>>> str1.startswith('p')
True
>>> str1.startswith('python')
True
>>> str1.startswith('Python')
False
>>> str1.endswith('Python')
False
>>> str1.endswith('n')
True
>>> str1.endswith('learn')
True
>>> strNew = 'abcd efgh'
>>> print(strNew)
abcd efgh
>>> strNew = 'abcd \n efgh'    # \ is used for escape or non-printable or whitespace characters
>>> print(strNew)
abcd 
 efgh
>>> # \n - new line
>>> # \t - provide space of some 4 characters
>>> strNew = 'abcd\tefgh'
>>> print(strNew)
abcd	efgh
>>> print(strNew.expandtabs(20))
abcd                efgh
>>> strNew = 'abcd\t\efgh'
>>> strNew = 'abcd\t\t\t\t\tefgh'
>>> print(strNew)
abcd					efgh
>>> a = 10
>>> b = 20
>>> c = a + b
>>> print("Sum of {} and {} is {}".format(a,b,c))
Sum of 10 and 20 is 30
>>> employee = {
	eid: 10
	}
Traceback (most recent call last):
  File "<pyshell#139>", line 2, in <module>
    eid: 10
NameError: name 'eid' is not defined
>>> employee = {
	'id': 10,
	'name': 'Ram',
	'salary': 10000
	}
>>> employee
{'id': 10, 'name': 'Ram', 'salary': 10000}
>>> print("Employee details : {} {} {}".format(employee))
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print("Employee details : {} {} {}".format(employee))
IndexError: tuple index out of range
>>> print("Employee details : {} {} {}".format(employee, employee, employee))
Employee details : {'id': 10, 'name': 'Ram', 'salary': 10000} {'id': 10, 'name': 'Ram', 'salary': 10000} {'id': 10, 'name': 'Ram', 'salary': 10000}
>>> print("Employee details : {id} {name} {salary}".format_map(employee))
Employee details : 10 Ram 10000
>>> 'abcd'.isalpha()
True
>>> 'pyhton is a prog lang'.isalpha()
False
>>> '1234abcd'.isalnum()
True
>>> '1234 abcd'.isalnum()
False
>>> 'abcd1'.isalpha()
False
>>> 'abcd#$%~'.isascii()
True
>>> 'राम '.isascii()
False
>>> ' '.isascii()
True
>>> 2 * 2
4
>>> 2 ** 2
4
>>> 2 ** 4
16
>>> 2 * 4
8
>>> 123 ** 2
15129
>>> '4.5'.isnumeric()
False
>>> #isdigit works for '12344'
>>> #isdecimal works for '12344'
>>> a = 4.5
>>> type(a)
<class 'float'>
>>> #isdecimal works for '12344'
>>> #isdigit works for superscript and subscripts also
>>> #isnumeric works for fractions also
>>> #identifier is another name for variable
>>> 'a'.isidentifier()
True
>>> 'name'.isidentifier()
True
>>> ' name'.isidentifier()
False
>>> '$name'.isidentifier()
False
>>> name = 'hello'
>>> $name = 'hello'
SyntaxError: invalid syntax
>>> bool(1)
True
>>> bool = 'hello'
>>> True = 'hello'
SyntaxError: can't assign to keyword
>>> bool(1)
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    bool(1)
TypeError: 'str' object is not callable
>>> type(bool)
<class 'str'>
>>> 'True'isidentifier()
SyntaxError: invalid syntax
>>> 'True'.isidentifier()
True
>>> 'Name'.islower()
False
>>> nName'.islower()
SyntaxError: EOL while scanning string literal
>>> 'name'.islower()
True
>>> 'n'.isprintable()
True
>>> '\n'.isprintable()
False
>>> #varToStoreString  #camelcase
>>> #vartostorestring lowercase
>>> #Var To Store String   #titlecase
>>> 
>>> str1
'python is very easy to learn learn'
>>> str1.title()
'Python Is Very Easy To Learn Learn'
>>> str1.istitle()
False
>>> str1
'python is very easy to learn learn'
>>> str2 = str1.title()
>>> str2
'Python Is Very Easy To Learn Learn'
>>> str2.istitle()
True
>>> str2.upper()
'PYTHON IS VERY EASY TO LEARN LEARN'
>>> str2.isupper()
False
>>> str2
'Python Is Very Easy To Learn Learn'
>>> string1 = 'hello'
>>> string2 = 'this is'
>>> string3 = 'python'
>>> join(string1,string2,string3)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    join(string1,string2,string3)
NameError: name 'join' is not defined
>>> ' '.join(string1,string2,string3)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    ' '.join(string1,string2,string3)
TypeError: join() takes exactly one argument (3 given)
>>> ' '.join([string1,string2,string3])
'hello this is python'
>>> '$$$'.join([string1,string2,string3])
'hello$$$this is$$$python'
>>> '_'.join([string1,string2,string3])
'hello_this is_python'
>>> str1
'python is very easy to learn learn'
>>> str1.ljust(100)
'python is very easy to learn learn                                                                  '
>>> str1.rjust(100)
'                                                                  python is very easy to learn learn'
>>> str1.ljust(100, -)
SyntaxError: invalid syntax
>>> str1.ljust(100, '-')
'python is very easy to learn learn------------------------------------------------------------------'
>>> str1.rjust(100, '-')
'------------------------------------------------------------------python is very easy to learn learn'
>>> 
>>> 
>>> 
>>> 
>>> strNew = '         abcd
SyntaxError: EOL while scanning string literal
>>> strNew = '         abcd         '
>>> print(strNew)
         abcd         
>>> strNew = '         ab  cd         '
>>> strNew.strip()
'ab  cd'
>>> strNew.lstrip()
'ab  cd         '
>>> strNew.rstrip()
'         ab  cd'
>>> 
>>> 
>>> 
>>> 
>>> str1
'python is very easy to learn learn'
>>> str1 = 'python is very easy to learn learn, it has got easy syntax'
>>> str1.partition()
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    str1.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> str1.partition(',')
('python is very easy to learn learn', ',', ' it has got easy syntax')
>>> str1.partition(' ')
('python', ' ', 'is very easy to learn learn, it has got easy syntax')
>>> str1.partition('p')
('', 'p', 'ython is very easy to learn learn, it has got easy syntax')
>>> #partition is always going to make 3 parts of my string - before partition, partition substring itself, after partition
>>> str1.partition('is')
('python ', 'is', ' very easy to learn learn, it has got easy syntax')
>>> str1 = 'python is very easy to learn learn, it has got easy syntax, it''
SyntaxError: EOL while scanning string literal
>>> str1 = 'python is very easy to learn learn, it has got easy syntax, it\'s has very reliable data structures, but it has got no switch case'
>>> str1.count(',')
3
>>> str1.partition(',')
('python is very easy to learn learn', ',', " it has got easy syntax, it's has very reliable data structures, but it has got no switch case")
>>> str1.rpartition(',')
("python is very easy to learn learn, it has got easy syntax, it's has very reliable data structures", ',', ' but it has got no switch case')
>>> str1.split()
['python', 'is', 'very', 'easy', 'to', 'learn', 'learn,', 'it', 'has', 'got', 'easy', 'syntax,', "it's", 'has', 'very', 'reliable', 'data', 'structures,', 'but', 'it', 'has', 'got', 'no', 'switch', 'case']
>>> #tokenization
>>> tokens = str1.split()
>>> tokens
['python', 'is', 'very', 'easy', 'to', 'learn', 'learn,', 'it', 'has', 'got', 'easy', 'syntax,', "it's", 'has', 'very', 'reliable', 'data', 'structures,', 'but', 'it', 'has', 'got', 'no', 'switch', 'case']
>>> ' '.join(tokens)
"python is very easy to learn learn, it has got easy syntax, it's has very reliable data structures, but it has got no switch case"
>>> str1 = 'python is very easy to learn learn\n it has got easy syntax\n it\'s has very reliable data structures\n but it has got no switch case'
>>> str1.splitlines()
['python is very easy to learn learn', ' it has got easy syntax', " it's has very reliable data structures", ' but it has got no switch case']
>>> str1.split()
['python', 'is', 'very', 'easy', 'to', 'learn', 'learn', 'it', 'has', 'got', 'easy', 'syntax', "it's", 'has', 'very', 'reliable', 'data', 'structures', 'but', 'it', 'has', 'got', 'no', 'switch', 'case']
>>> str1 = 'python is very easy to learn learn, it has got easy syntax, it\'s has very reliable data structures, but it has got no switch case'
>>> str1.split(',')
['python is very easy to learn learn', ' it has got easy syntax', " it's has very reliable data structures", ' but it has got no switch case']
>>> str1.split('t')
['py', 'hon is very easy ', 'o learn learn, i', ' has go', ' easy syn', 'ax, i', "'s has very reliable da", 'a s', 'ruc', 'ures, bu', ' i', ' has go', ' no swi', 'ch case']
>>> str1.partition('t')
('py', 't', "hon is very easy to learn learn, it has got easy syntax, it's has very reliable data structures, but it has got no switch case")
>>> str1 = 'python is very easy to learn learn, it has got easy syntax, it\'s has "very" reliable data structures, but it has got no switch case'
>>> str1.split(',')
['python is very easy to learn learn', ' it has got easy syntax', ' it\'s has "very" reliable data structures', ' but it has got no switch case']
>>> '1234'.zfill(5)
'01234'
>>> '1234'.zfill(9)
'000001234'
>>> '1234'.zfill(4)
'1234'
>>> '1234'.zfill(3)
'1234'
>>> str1
'python is very easy to learn learn, it has got easy syntax, it\'s has "very" reliable data structures, but it has got no switch case'
>>> str1.isalpha()
False
>>> str1.replace(' ', '')
'pythonisveryeasytolearnlearn,ithasgoteasysyntax,it\'shas"very"reliabledatastructures,butithasgotnoswitchcase'
>>> str2 = str1.replace(' ', '')
>>> str2.isalpha()
False
>>> str1 = 'python is very easy to learn learn'
>>> str2 = str1.replace(' ', '')
>>> str2.isalpha()
True
>>> str2
'pythonisveryeasytolearnlearn'
>>> str1.replace('python', 'java')
'java is very easy to learn learn'
>>> str1.replace(' ', '', 3)
'pythonisveryeasy to learn learn'
>>> #function chaining
>>> str1.replace(' ', '').isaplha()
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    str1.replace(' ', '').isaplha()
AttributeError: 'str' object has no attribute 'isaplha'
>>> str1.replace(' ', '').isalpha()
True
>>> 
