Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> '1234'.isdigit()
True
>>> '1234.1234'.isdigit()
False
>>> 'name'.isidentifier()
True
>>> '$name'.isidentifier()
False
>>> name = 'anmol'
>>> $name = 'anmol'
SyntaxError: invalid syntax
>>> str1 = 'hello'
>>> str2 = 'this is python'
>>> str3 = 'are you enjoying it'
>>> '.'.join([str1,str2,str3])
'hello.this is python.are you enjoying it'
>>> '\n'.join([str1,str2,str3])
'hello\nthis is python\nare you enjoying it'
>>> newStr = '\n'.join([str1,str2,str3])
>>> print(newStr)
hello
this is python
are you enjoying it
>>> ' '.join([str1,str2,str3])
'hello this is python are you enjoying it'
>>> 'hello this is python'
'hello this is python'
>>> 'hello this is python'.center(100)
'                                        hello this is python                                        '
>>> 'hello this is python'.ljust(100)
'hello this is python                                                                                '
>>> 'hello this is python'.rjust(100)
'                                                                                hello this is python'
>>> 'hello this is python'.rjust(100,'#')
'################################################################################hello this is python'
>>> '################################################################################hello this is python'
'################################################################################hello this is python'
>>> 
>>> 
>>> '   hwehfkfk     '.strip()
'hwehfkfk'
>>> '   hw ehf kfk     '.strip()
'hw ehf kfk'
>>> '   hw ehf kfk     '.lstrip()
'hw ehf kfk     '
>>> '   hw ehf kfk     '.rstrip()
'   hw ehf kfk'
>>> 
>>> 'hello this is python'.replace(' ', '')
'hellothisispython'
>>> #['h', 'e', 'l', 'l', 'o']
>>> 
>>> #string is immutable
>>> 
>>> str1 = 'hello this is python'
>>> del str1[5]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    del str1[5]
TypeError: 'str' object doesn't support item deletion
>>> 
>>> 
>>> str1[5] = 'x'
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    str1[5] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> str1 = 'bye'
>>> str1
'bye'
>>> hex(id(str1))
'0x1034ceae8'
>>> str1 = 'hello'
>>> hex(id(str1))
'0x1034ebfb8'
>>> 
>>> str1 = 'hello'
>>> str2 = 'bye'
>>> str1 is str2
False
>>>  str1 = 'hello'
 
SyntaxError: unexpected indent
>>> str1 = 'hello'
>>> str2 = 'hello'
>>> str1 is str2
True
>>> hex(id(str1))
'0x1034ebfb8'
>>> hex(id(str2))
'0x1034ebfb8'
>>> 
>>> 
>>> 
>>> str1 = 'python is very interesting'
>>> str2 = "python is very interesting"
>>> str1 is str2
False
>>> hex(id(str1))
'0x1034e8df0'
>>> hex(id(str2))
'0x1034e8ee0'
>>> str1 == str2
True
>>> str1.replace('python', 'java')
'java is very interesting'
>>> str1
'python is very interesting'
>>> str2 str1.replace('python', 'java')
SyntaxError: invalid syntax
>>> str2  = str1.replace('python', 'java')
>>> str2
'java is very interesting'
>>> str1 is str2
False
>>> str1  = str1.replace('python', 'java')
>>> str1
'java is very interesting'
>>> str1 is str2
False
>>> str1 == str2
True
>>> str1
'java is very interesting'
>>> str1.replace('e', 1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    str1.replace('e', 1)
TypeError: replace() argument 2 must be str, not int
>>> str1.replace('e', '1')
'java is v1ry int1r1sting'
>>> str1.replace('very', 'good')
'java is good interesting'
>>> str1
'java is very interesting'
>>> 
>>> str1 = 't20 world cup is going to happen soon'
>>> str1.replace('t', 'f')
'f20 world cup is going fo happen soon'
>>> str1.replace('2', '5')
't50 world cup is going to happen soon'
>>> str2 = 'acnakjcnaknk,iallvlm.kjbkjn!klfmlka?'
>>> str2.replace(',.!?', '')
'acnakjcnaknk,iallvlm.kjbkjn!klfmlka?'
>>> str2.replace(', .!?', '')
'acnakjcnaknk,iallvlm.kjbkjn!klfmlka?'
>>> 
>>> str2.maketrans(',.!?', 'xyz$')
{44: 120, 46: 121, 33: 122, 63: 36}
>>> table = str2.maketrans(',.!?', 'xyz$')
>>> str2.translate(table)
'acnakjcnaknkxiallvlmykjbkjnzklfmlka$'
>>> str2.maketrans(',.!?', 'xyz$', 'l')
{44: 120, 46: 121, 33: 122, 63: 36, 108: None}
>>> table = str2.maketrans(',.!?', 'xyz$', 'l')
>>> str2.translate(table)
'acnakjcnaknkxiavmykjbkjnzkfmka$'
>>> 
>>> 
>>> str1
't20 world cup is going to happen soon'
>>> str1.split()
['t20', 'world', 'cup', 'is', 'going', 'to', 'happen', 'soon']
>>> #tokenization
>>> 
>>> str1.split(maxsplit = 3)
['t20', 'world', 'cup', 'is going to happen soon']
>>> str1.split(' ',3)
['t20', 'world', 'cup', 'is going to happen soon']
>>> str1.split(3)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    str1.split(3)
TypeError: must be str or None, not int
>>> 
>>> str1.split('o')
['t20 w', 'rld cup is g', 'ing t', ' happen s', '', 'n']
>>> 
>>> str1.split('world')
['t20 ', ' cup is going to happen soon']
>>> str1.split('oo')
['t20 world cup is going to happen s', 'n']
>>> 
>>> str1.partition()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    str1.partition()
TypeError: partition() takes exactly one argument (0 given)
>>> 
>>> str1.partition('oo')
('t20 world cup is going to happen s', 'oo', 'n')
>>> str1.partition('o')
('t20 w', 'o', 'rld cup is going to happen soon')
>>> str1.rpartition('o')
('t20 world cup is going to happen so', 'o', 'n')
>>> 
>>> str1.find('a')
27
>>> str1 = 't20 world cup\nis going to happen soon'
>>> str1.splitlines()
['t20 world cup', 'is going to happen soon']
>>> 
>>> 
>>> '100'.zfill(5)
'00100'
>>> '1'.zfill(5)
'00001'
>>> '01'.zfill(5)
'00001'
>>> '01'.zfill(5)
'00001'
>>> '10'.zfill(5)
'00010'
>>> '100'.zfill(5)
'00100'
>>> '1000'.zfill(5)
'01000'
>>> '10000'.zfill(5)
'10000'
>>> '100000'.zfill(5)
'100000'
>>> 
>>> 
>>> 'abcd'.encode()
b'abcd'
>>> 
>>> 
>>> 'ŠČæłßabcd1234'.encode()
b'\xc5\xa0\xc4\x8c\xc3\xa6\xc5\x82\xc3\x9fabcd1234'
>>> 'ŠČæłßabcd1234'.encode()
b'\xc5\xa0\xc4\x8c\xc3\xa6\xc5\x82\xc3\x9fabcd1234'

>>> 
>>> encodedString = 'ŠČæłßabcd1234'.encode()
>>> encodedString
b'\xc5\xa0\xc4\x8c\xc3\xa6\xc5\x82\xc3\x9fabcd1234'
>>> type(encodedString)
<class 'bytes'>
>>> 
>>> encodedString.decode()
'ŠČæłßabcd1234'
>>> 
>>> 
>>> 
>>> #I18N  Internationalization
>>> 
>>> name = input('What\'s your name: ')
What's your name: अनमोल 
>>>  name
 
SyntaxError: unexpected indent
>>> 
>>> name
'अनमोल '
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep/turtle-shapes.py ==
13
>>> '''
this is a
multi-lint
comment
'''
'\nthis is a\nmulti-lint\ncomment\n'
>>> print('''this is a
multi-line
string''')
this is a
multi-line
string
>>> name
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> 
== RESTART: /Users/anmolrajarora/Documents/python-wknd-sep/turtle-shapes.py ==
13
yellow
navy
skyblue
red
turquoise
violet
orange
yellow
blue
turquoise
yellow
yellow
blue
maroon
blue
purple
red
turquoise
turquoise
maroon
violet
purple
turquoise
navy
turquoise
skyblue
purple
turquoise
violet
red
blue
navy
navy
yellow
purple
purple
cyan
blue
navy
violet
cyan
navy
cyan
maroon
red
turquoise
cyan
skyblue
skyblue
orange
gold
cyan
red
navy
red
blue
cyan
yellow
maroon
red
red
turquoise
navy
violet
yellow
turquoise
red
orange
cyan
violet
magenta
maroon
blue
purple
red
red
red
red
gold
orange
navy
red
red
gold
turquoise
violet
skyblue
cyan
purple
orange
magenta
yellow
orange
cyan
cyan
skyblue
orange
red
skyblue
maroon
>>> import turtle
>>> turtle.Pen()
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    turtle.Pen()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 3816, in __init__
    visible=visible)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2557, in __init__
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2660, in _update
    self._update_data()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> 
