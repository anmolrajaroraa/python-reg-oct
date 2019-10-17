Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list [mutable], tuple (immutable), set {random positioning - hashing algorithm - no indexing - mutable}, dict {key value pair - mutable}, frozen set{same as set - immutable}
>>> 
>>> student = {
	'eno': 101,
	'name': 'Ram',
	'contact' : '1234'
	}
>>> student
{'eno': 101, 'name': 'Ram', 'contact': '1234'}
>>> student['eno']
101
>>> student['name']
'Ram'
>>> 
>>> student['contact']
'1234'
>>> student = {
	'eno': 101,
	'name': 'Ram',
	'contact' : '1234','4567
	}
SyntaxError: EOL while scanning string literal
>>> student = {
	'eno': 101,
	'name': 'Ram',
	'contact' : '1234','4567'
	}
SyntaxError: invalid syntax
>>> student = {
	'eno': 101,
	'name': 'Ram',
	'contact' : ['1234','4567']
	}
>>> student['contact']
['1234', '4567']
>>> student['contact'][0]
'1234'
>>> student['contact'][1]
'4567'
>>> student = {
	'eno': 101,
	'name': 'Ram',
	'contact' : ['1234','4567'],
	'address' : {
		'temp' : 'rohini',
		'perm' : 'pitampura'
		}
	}
>>> student['address']
{'temp': 'rohini', 'perm': 'pitampura'}
>>> student['address']['perm']
'pitampura'
>>> 
>>> 
>>> student
{'eno': 101, 'name': 'Ram', 'contact': ['1234', '4567'], 'address': {'temp': 'rohini', 'perm': 'pitampura'}}
>>> 
>>> for i in range(len(list):
	       
SyntaxError: invalid syntax
>>> '''for i in range(len(list)):
	print(list[i])'''
'for i in range(len(list)):\n\tprint(list[i])'
>>> 
>>> for key in student:
	print(key)

	
eno
name
contact
address
>>> for key in student:
	print(student[key])

	
101
Ram
['1234', '4567']
{'temp': 'rohini', 'perm': 'pitampura'}
>>> student.keys()
dict_keys(['eno', 'name', 'contact', 'address'])
>>> 
>>> student.values()
dict_values([101, 'Ram', ['1234', '4567'], {'temp': 'rohini', 'perm': 'pitampura'}])
>>> 
>>> for value in student.values():
	print(value)

	
101
Ram
['1234', '4567']
{'temp': 'rohini', 'perm': 'pitampura'}
>>> 
>>> 
>>> for key in student:
	print(f"{key} : {student[key]")
	
SyntaxError: f-string: expecting '}'
>>> 
>>> for key in student:
	print(f"{key} : {student[key]}")

	
eno : 101
name : Ram
contact : ['1234', '4567']
address : {'temp': 'rohini', 'perm': 'pitampura'}
>>> 
>>> 
>>> student.items()
dict_items([('eno', 101), ('name', 'Ram'), ('contact', ['1234', '4567']), ('address', {'temp': 'rohini', 'perm': 'pitampura'})])
>>> 
>>> 
>>> for key,value in student.items():
	print(key,value,sep=' : ')

	
eno : 101
name : Ram
contact : ['1234', '4567']
address : {'temp': 'rohini', 'perm': 'pitampura'}
>>> 
>>> username = input("Enter username: ")
Enter username: ram123
>>> email = input("Enter email: ")
Enter email: ram123@gmail.com
>>> pwd = input("Enter pwd: ")
Enter pwd: ram123
>>> 
>>> users = []
>>> #[['ram123','ram123@gmail.com', 'ram123'], ['shyam123','shyam123@gmail.com', 'shyam123']]
>>> [
	{
		#user1
		'username' : 'ram123',
		'email' : 'ram123@gmail.com',
		'pwd' : '12345'
		},
	{
		#user2
		'username' : 'shyam123',
		'email' : 'shyam123@gmail.com',
		'pwd' : '123456'
		}
	]
[{'username': 'ram123', 'email': 'ram123@gmail.com', 'pwd': '12345'}, {'username': 'shyam123', 'email': 'shyam123@gmail.com', 'pwd': '123456'}]
>>> 
>>> 
>>> user = {}
>>> user['username'] = username
>>> user
{'username': 'ram123'}
>>> user['email'] = email
>>> user['pwd'] = pwd
>>> user
{'username': 'ram123', 'email': 'ram123@gmail.com', 'pwd': 'ram123'}
>>> 
>>> users.append(user)
>>> users
[{'username': 'ram123', 'email': 'ram123@gmail.com', 'pwd': 'ram123'}]
>>> username = input("Enter username: ")
Enter username: shyam123
>>> email = input("Enter email: ")
Enter email: shyam123@gmail.com
>>> pwd = input("Enter pwd: ")
Enter pwd: 12345
>>> user = {}
>>> user['username'] = username
>>> user['email'] = email
>>> user['pwd'] = pwd
>>> users.append(user)
>>> users
[{'username': 'ram123', 'email': 'ram123@gmail.com', 'pwd': 'ram123'}, {'username': 'shyam123', 'email': 'shyam123@gmail.com', 'pwd': '12345'}]
>>> for i in range(len(users)):
	if username == users[i]['username']:
		pwd = pwd
		if pwd == users[i]['pwd']:
			print('Login successful')
		else:
			print('Invalid username/password')
	else:
		print('Register first')

		
Register first
Login successful
>>> for i in range(len(users)):
	if username == users[i]['username']:
		pwd = pwd
		if pwd == users[i]['pwd']:
			print('Login successful')
		else:
			print('Invalid username/password')
		break
else:
	print('Register first')

	
Login successful
>>> username = 'anmol'
>>> for i in range(len(users)):
	if username == users[i]['username']:
		pwd = pwd
		if pwd == users[i]['pwd']:
			print('Login successful')
		else:
			print('Invalid username/password')
		break
else:
	print('Register first')

	
Register first
>>> 
>>> 
>>> gamePositions = [1,2,3,4,5,6,7,8,9]
>>> 
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
''')

{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}

>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

1 | 2 | 3
------------
4 | 5 | 6
------------
7 | 8 | 9


>>> userChoice = int(input("Enter the position at which you want to input X: "))
Enter the position at which you want to input X: 5
>>> 
>>> userChoice = userChoice - 1
>>> 
>>> gamePositions[userChoice] = 'X'
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

1 | 2 | 3
------------
4 | X | 6
------------
7 | 8 | 9

>>> gamePositions[0] = 'O'
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

O | 2 | 3
------------
4 | X | 6
------------
7 | 8 | 9

>>> gamePositions[1] = 'X'
>>> gamePositions[2] = 'X'
>>> gamePositions[3] = 'O'
>>> gamePositions[8] = 'O'
>>> print('''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(gamePositions[0], gamePositions[1], gamePositions[2], gamePositions[3], gamePositions[4], gamePositions[5], gamePositions[6], gamePositions[7], gamePositions[8]))

O | X | X
------------
O | X | 6
------------
7 | 8 | O

>>> 
