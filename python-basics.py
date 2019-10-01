Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #number, string, boolean
>>> number
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    number
NameError: name 'number' is not defined
>>> #number, string, boolean
>>> # is used for single-line comments
>>> # comments are not executed (python skips them)
>>> '''
let's start learning python
this is a multi-line comment
'''
"\nlet's start learning python\nthis is a multi-line comment\n"
>>> """
this comment
uses double quotes
three times
"""
'\nthis comment\nuses double quotes\nthree times\n'
>>> #number, string, boolean
>>> #Native data types
>>> a = 10
>>> print(a)
10
>>> b = 10.5
>>> print(b)
10.5
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> c = -20
>>> d = -0.8765435468782
>>> type(c)
<class 'int'>
>>> type(d)
<class 'float'>
>>> print
<built-in function print>
>>> print()

>>> print('hello')
hello
>>> # () -> paranthesis are called as function call
>>> s1 = 'hello'
>>> s2 = "hello"
>>> type(s1)
<class 'str'>
>>> type(s2)
<class 'str'>
>>> s1 = "India is an "incredible" country"
SyntaxError: invalid syntax
>>> s1 = 'India is an "incredible" country'
>>> print(s1)
India is an "incredible" country
>>> s1
'India is an "incredible" country'
>>> s2 = 'let's learn python'
SyntaxError: invalid syntax
>>> s2 = "let's learn python"
>>> print(s2)
let's learn python
>>> s3 = 'india\'s "great" a country'
>>> print(s3)
india's "great" a country
>>> s4 = '''
abcd
efgh
'''
>>> print(s4)

abcd
efgh

>>> print('''hello
bye''')
hello
bye
>>> print('hello
bye')
      
SyntaxError: EOL while scanning string literal
>>> print('''hello
bye''')
hello
bye
>>> 
============== RESTART: /Users/anmolrajarora/Documents/demo2.py ==============
lkdjkd
vlskvnlksv
skvklsv
>>> b1 = True
>>> b2 = False
>>> type(b1)
<class 'bool'>
>>> #boolean
>>> type(b2)
<class 'bool'>
>>> b1 = true
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b1 = true
NameError: name 'true' is not defined
>>> True = 'hello'
SyntaxError: can't assign to keyword
>>> input("What's your name: ")
What's your name: Anmol
'Anmol'
>>> input = 'hello'
>>> input("What's your name: ")
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    input("What's your name: ")
TypeError: 'str' object is not callable
>>> type(input)
<class 'str'>
>>> type(sum)
<class 'builtin_function_or_method'>
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
30
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Traceback (most recent call last):
  File "/Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py", line 8, in <module>
    print("Total is " + total)  #string concatenation (joining)
TypeError: can only concatenate str (not "int") to str
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is 30
>>> a = 10
>>> type(a)
<class 'int'>
>>> int() #convert string to integer
0
>>> str() #convert integer to string
''
>>> #built-in functions
>>> bool() #convert integer or string into boolean
False
>>> str(a)
'10'
>>> a = str(a)
>>> type(a)
<class 'str'>
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is 30
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of a and b is c
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of 10 and 20 is 30
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of 10 and 20 is 30
Sum of {} and {} is {}
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
Sum of {a} and {b} is {total}
>>> 
= RESTART: /Users/anmolrajarora/Documents/python-reg-sept-11/print-basics.py =
Total is30
Total is 30
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
Sum of 10 and 20 is 30
>>> 
