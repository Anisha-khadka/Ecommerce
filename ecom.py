# Requirements
# Login and register
# ask the user if he or she wants to login or register
# If the user says register ask for username and password and store this data in a file
# Elif the user says login the ask for username and password and check this data in the file where user data is stored in such a way if the username and password matches print 'Login successfull' else 'Invalid credentials'


import json

user_choice = input('Do you want to login or register?:')


def register():
    user_name = input("Enter a username:")
    user_password = input("Enter a password:")
    user_dict = {user_name: user_password}
    json_user_dict = json.dumps(user_dict)
    f = open('userdata.txt', 'a')
    f.write(json_user_dict+'-')
    f.close()


def Login():
    user_name = input("Enter your username:")
    user_password = input("Enter your password:")

    f = open("userdata.txt", 'r')
    user_data = f.read()
    f.close()
    list_user_data = user_data.split("-")

    for i in list_user_data:
        if i!='':
            dict_data=json.loads(i)
            try:
                if user_name in dict_data and dict_data.get(user_name)==user_password :
                    print("Login successful")
            except:
                print("Invalid credentials")
            


if user_choice == 'login':
    Login()
elif user_choice == 'register':
    register()
else:
    print('Invalid input')
