Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> date
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    date
NameError: name 'date' is not defined
>>> from datetime import date
>>> date
<class 'datetime.date'>
>>> time
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    time
NameError: name 'time' is not defined
>>> datetime
<module 'datetime' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/datetime.py'>
>>> from datetime import *
>>> date
<class 'datetime.date'>
>>> tim
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tim
NameError: name 'tim' is not defined
>>> time
<class 'datetime.time'>
>>> datetime
<class 'datetime.datetime'>
>>> date.today()
datetime.date(2019, 10, 9)
>>> today = date.today()
>>> print(today)
2019-10-09
>>> 
>>> 
>>> datetime.now()
datetime.datetime(2019, 10, 9, 14, 3, 43, 220436)
>>> print(datetime.now())
2019-10-09 14:03:57.799546
>>> 
>>> 
>>> now = datetime.now()
>>> type(now)
<class 'datetime.datetime'>
>>> 
>>> 
>>> now.strftime("%y")   #string formatting time
'19'
>>> now.strftime("%Y")
'2019'
>>> now.strftime("%a")
'Wed'
>>> now.strftime("%A")
'Wednesday'
>>> now.strftime("%b")
'Oct'
>>> now.strftime("%B")
'October'
>>> now.strftime("%c")
'Wed Oct  9 14:04:15 2019'
>>> now.strftime("%d")
'09'
>>> now.strftime("%D")
'10/09/19'
>>> now.strftime("%m")
'10'
>>> now.strftime("%M")
'04'
>>> now.strftime("%h")
'Oct'
>>> now.strftime("%H")
'14'
>>> now.strftime("%I")
'02'
>>> 
>>> 
>>> now.strftime("%a %d %b %Y %I:%M:%S %p")
'Wed 09 Oct 2019 02:04:15 PM'
>>> now = datetime.now()
>>> now.strftime("%a %d %b %Y %I:%M:%S %p")
'Wed 09 Oct 2019 02:10:20 PM'
>>> 
>>> 
>>> 
>>> import os
>>> os.getcwd()  #get current working directory
'/Users/anmolrajarora/Documents'
>>> #os.chdir('C:\\Users\\Hitesh\\Music')
>>> os.chdir('/Users/anmolrajarora/Documents/python')
>>> os.getcwd()
'/Users/anmolrajarora/Documents/python'
>>> os.listdir()
['01-PythonIntroduction.wmv', 'PythonPygame_2.wmv', '.DS_Store', 'PythonPygame_!.wmv', '01-Python.wmv', 'PythonFunctionsIntro_1.wmv', 'PythonFunctions_2.wmv', 'PythonFilterMapLambda.wmv', 'PythonFunctionsIntro.wmv', 'Crawling_2.wmv', 'PythonIfElse.wmv', 'Crawling_1.wmv', 'Python_IfElse+List.wmv']
>>> songs = os.listdir()
>>> import random
>>> random.choice(songs)
'PythonFunctions_2.wmv'

>>> random.choice(songs)
'Python_IfElse+List.wmv'
>>> random.choice(songs)
'.DS_Store'
>>> random.choice(songs)
'.DS_Store'
>>> random.choice(songs)
'PythonPygame_!.wmv'
>>> song = random.choice(songs)
>>> os.startfile(song)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    os.startfile(song)
AttributeError: module 'os' has no attribute 'startfile'
>>> # for windows   ->    os.startfile(song)
>>> 
>>> 
>>> import subprocess
>>> subprocess.call(['open', song])
0
>>> subprocess.call(['open', 'Users/anmolrajarora/Documents/python-reg-oct/chatbot.py'])
1
>>> subprocess.call(['open', 'Users/anmolrajarora/Documents/python-reg-oct/chatbot.py'])
1
>>> subprocess.call(['open', 'Users/anmolrajarora/Documents/python-reg-oct/turtle-spiral.py'])
1
>>> subprocess.call(['open', '/Users/anmolrajarora/Documents/python-reg-oct/turtle-spiral.py'])
0

>>> subprocess.call(['open', '/Applications/Github Desktop.app'])
0
>>> 
