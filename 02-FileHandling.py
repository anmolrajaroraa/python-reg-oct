import csv, io, os

# users = [
#     {
#         'username' : 'ram',
#         'email' : 'ram@gmail.com',
#         'password' : 'ram123'
#     },
#     {
#         'username' : 'shyam',
#         'email' : 'shyam@gmail.com',
#         'password' : 'shyam123'
#     },
#     {
#         'username' : 'mohan',
#         'email' : 'mohan@gmail.com',
#         'password' : 'mohan123'
#     }
# ]
#
# with open('users.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for user in users:
#         writer.writerow(user.values())

users = []
path = 'users.csv'
try:
    with open(path) as file:
        data = csv.reader(file)
        for row in data:
            # print(row[0], row[1], row[2])
            user = {
                'username' : row[0],
                'email' : row[1],
                'password' : row[2]
            }
            users.append(user)

    print(users)
except FileNotFoundError as err:
    print(err)
except io.UnsupportedOperation as err:
    print(err)
except BaseException as err:
    print(err)
finally:
    print("Finally ran")
    if os.path.exists(path):
        file.close()



        # ram , ram @ gmail.com , ram123
        # shyam , shyam @ gmail.com , shyam123
        # mohan , mohan @ gmail.com , mohan123