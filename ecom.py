# Requirements
# Login and register
# ask the user if he or she wants to login or register
# If the user says register ask for username and password and store this data in a file
# Elseif the user says login the ask for username and password and check this data in the file where user data is stored in such a way if the username and password matches print 'Login successfull' else 'Invalid credentials'
# if the user is buyer provide the choices of 1: View product 2. Purchase product 3. View products
# if the user is seller provide the choices of 1: Add product 2. View your product 3. View bills
# Add product logic
# Ask the user for product name, description and price
# Also write seller data in the product data
# then store this data as a relation data in file
# purchase product logic
# after the view product logic ask the user for product purchase
# ask him/her for the name of product he/she wants to purchase and get the price of the product then multiply the price with quantity and print it as total for buyer

# buyer view bill logic

# get all the bill data from bill.txt and print only those datas whose buyer key has same value as the logic user's name

import json


def Addproduct(seller_name):

    product_name = input("Enter product name:").casefold()
    product_description = input("Enter product description:").casefold()
    product_price = int(input("Enter product price:"))

    product_dict = {
        'product_name': product_name,
        'product_des': product_description,
        'product_price': product_price,
        'seller': seller_name
    }
    product_json_info = json.dumps(product_dict)
    f = open('productdata.txt', 'a')

    f.write(product_json_info + '-')
    f.close()


def viewYourProduct(user):
    f = open('productdata.txt', 'r')
    sellers_products = f.read()
    seller_dict_product = sellers_products.split('-')

    for i in seller_dict_product:
        if i != '':
            a = json.loads(i)
            if a.get('seller') == user:
                print(a)

    f.close()


def Viewproduct():
    f = open('productdata.txt', 'r')
    productview = f.read()
    f.close()
    list_product_data = productview.split('-')
    print(list_product_data)


def purchaseProduct(buyer_name):
    f = open('productdata.txt', 'r')
    productview = f.read()
    f.close()
    list_product_data = productview.split('-')
    print(list_product_data)
    user_purchase_choice = input(
        "Do you want to purchase a product?(y/n):").strip().lower()
    if user_purchase_choice == 'y':
        ask_product_name = input(
            "Enter name of the product you want to purchase:").strip().lower()
        ask_product_quantity = int(
            input("Enter the quantity you want to purchase:"))
    for i in list_product_data:
        if i != '':
            a = json.loads(i)
            if ask_product_name == a.get('product_name'):
                p = a.get('product_price')
                product_list = a
                total_amount = ask_product_quantity*p
                print(f"Your total billing amount is {total_amount}")
    billing_product = {'product': product_list.get(
        'product_name'), 'quantity': ask_product_quantity, 'total': total_amount, 'buyer': buyer_name}
    json_billing_product = json.dumps(billing_product)
    f = open('bill.txt', 'a')

    f.write(json_billing_product + '-')
    f.close()


def viewYourbill(buyer_id):
    f = open('bill.txt', 'r')
    buyer_bill = f.read()
    list_buyer_bill = buyer_bill.split('-')
 
    for i in list_buyer_bill:
        if i != '':
            billing = json.loads(i)
            if billing.get('buyer') == buyer_id:
                print(billing)

    f.close()


def register():
    user_name = input("Enter a username:")
    user_password = input("Enter a password:")
    user_type = input("Enter your usertype(buyer/seller):")
    user_dict = {
        'username': user_name,
        'user_password': user_password,
        'user_type': user_type
    }
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
    user_login = False
    user = None
    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)

            if dict_data.get('username') == user_name and dict_data.get('user_password') == user_password:
                user_login = True
                user = dict_data

    if user_login == True:
        print("Login sucessfull")
        while True:
            if user.get('user_type') == 'seller':

                print('''
                        1. Add product 
                        2. View bills
                        3. View your products
                        4. Exit''')
                seller_operation = int(
                    input("Enter the operation you want to run(1,2 or 3):"))
                if seller_operation == 1:
                    Addproduct(user.get('username'))
                elif seller_operation == 3:
                    viewYourProduct(user_name)
                elif seller_operation == 4:
                    break
            else:
                print('''
                        1. View product 
                        2. Purchase product
                        3. View your bills
                        4. Exit''')
                buyer_operation = int(
                    input("Enter the operation you want to perform(1,2 or 3):"))
                if buyer_operation == 1:
                    Viewproduct()
                elif buyer_operation == 2:
                    purchaseProduct(user_name)
                elif buyer_operation == 3:
                    viewYourbill(user_name)
                elif buyer_operation == 4:
                    break

    else:
        print("Invalid credentials")


while True:
    user_choice = input('Do you want to login or register?:').lower()
    if user_choice == 'login':
        Login()
    elif user_choice == 'register':
        register()
    else:
        print('Invalid input')
