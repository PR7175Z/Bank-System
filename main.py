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
            return [userinfo.index(x), True]
            # print(userinfo.index(x))
        
    return [0, False]

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
        print(userdb)
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
    os.system('cls')
    print("1.Add user\n2.login\n3.Exit")
    fchoice = int(input("Enter your choice: "))
    match fchoice:
        case 1:
            os.system('cls')
            usersinfo.append(get_info())
        case 2: 
            os.system('cls')
            a, s = check_login(usersinfo)
            if(s):
                login = True
                while login:
                    os.system('cls')
                    print("1.Show Info\n2.withdrawal\n3.deposit\n4.Send Money\n5.Logout")
                    schoice = int(input('Enter your choice: '))
                    match schoice:
                        case 1:
                            os.system('cls')
                            print(usersinfo[a].showval())
                        case 2:
                            os.system('cls')
                            amt = int(input("Enter the amount you want to withdrawl"))
                            usersinfo[a].withdrawl(amt)
                        case 3:
                            os.system('cls')
                            amt = int(input("Enter the amount you want to deposit"))
                            usersinfo[a].deposit(amt)
                        case 4:
                            os.system('cls')
                            receiver_name = input("Enter receiver username: ")
                            amt = int(input("Enter amount to be transferred: "))
                            usersinfo[a].sendmoney(receiver_name,amt,usersinfo)
                        case 5:
                            os.system('cls')
                            login = False
            else:
                os.system('cls')
                print("There is error in login")
        case 3:
            os.system('cls')
            program = False
            print('exit')