import os

import getpass
print('Bank System')

def get_info():
    name = input("Enter name: ")
    username = input(f"Enter {name}'s username: ")
    password = input(f"Enter {name}'s password: ")
    blc = int(input(f"Enter {name}'s balance: "))
    obj = account(name, username, password, blc)
    return obj

def check_login(userinfo):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    for x in userinfo:
        if username == x.username and password == x.password:
            return userinfo.index(x)
            # print(userinfo.index(x))
        

class account(object):
    def __init__(self, name, username, password, balance):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def withdrawl(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount  

    def sendmoney(self, receiver_username, amount, userdb):
        # self.balance -= amount
        for x in userdb:
            if receiver_username == x.username:
                self.balance = self.balance - amount
                x = userdb.index(x)
                userdb[x].balance = userdb[x].balance + amount
                # print('user exist')
                return x
            else:
                print('no user')
        # receiver_username.balance += amount

    def showval(self):
        return f'Name: {self.name} \nBalance: {self.balance}'
    
program = True
usersinfo = []
while program:
    print("1.Add user\n2.login\n3.Exit")
    fchoice = int(input("Enter your choice: "))
    match fchoice:
        case 1:
            os.system('cls')
            usersinfo.append(get_info())
        case 2: 
            os.system('cls')
            a = check_login(usersinfo)
            try:
                print("1.Show Info\n2.withdrawal\n3.deposit\n4.Send Money")
                schoice = int(input('Enter your choice: '))
                match schoice:
                    case 1:
                        print(usersinfo[a].showval())
                    case 2:
                        amt = int(input("Enter the amount you want to withdrawl"))
                        usersinfo[a].withdrawl(amt)
                    case 3:
                        amt = int(input("Enter the amount you want to deposit"))
                        usersinfo[a].deposit(amt)
                    case 4:
                        receiver_name = input("Enter receiver username: ")
                        amt = int(input("Enter amount to be transferred: "))
                        userinfo[a].sendmoney(receiver_name,amt,usersinfo)
            except:
                print("There is error in login")
        case 3:
            program = False
            print('exit')

# n = int(input('Enter number of new accounts'))
# usersinfo = [get_info() for x in range(0,n)]

# a = check_login(usersinfo)
# try:
#     print(usersinfo[a].showval())
# except:
#     print("There is error in login")
# # sendmoney
# x = usersinfo[a].sendmoney('admin', 200, usersinfo)
# try:
#     print(usersinfo[a].showval())
#     print(usersinfo[x].name, usersinfo[x].username, usersinfo[x].balance)
# except:
#     print("There is error in login")