import os

import getpass
print('Bank System')

def get_info():
    name = input("Enter name: ")
    username = input(f"Enter {name}'s username: ")
    password = input(f"Enter {name}'s password: ")
    blc = input(f"Enter {name}'s balance: ")
    obj = account(name, username, password, blc)
    return obj

def check_login(userinfo):
    os.system('cls')
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

    def showval(self):
        return f'Name: {self.name} \nBalance: {self.balance}'

n = int(input('Enter number of new accounts'))
usersinfo = [get_info() for x in range(0,n)]

a = check_login(usersinfo)
print(usersinfo[a].showval())