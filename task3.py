import getpass
import copy
import collections
from collections import Counter
from collections import defaultdict


# users Database
database = {"ahmed": "123", "shehta": "456"}
# products 
products = {
    1:{"banna":"20"},
    2:{"apple":"10"},
    3:{"fg":"4"},
}

# its used for return the choice list for Owner
def choice():   
    print("""	
=================                
1- show products
2- Add product
3- change cost
4- delete product
=================	
""")
    operation = int(input("select operation:"))
    if operation == 1 :
        showProduct()
    elif operation == 2 :
        addProduct()
    elif operation == 3 :
        ChangeProduct()
    elif operation == 4 :
        DeletePrdocut()  


# Customer methods
# this array used for store what is buy Checkout
arr= []

# checkout and print bill for customer
def Bills():
    x = 0
    print("hello mr")
    output = defaultdict(int)
    for key,value in products.items():
        for key,value in value.items():
            for row in arr:
                if key in row:
                    output[row[key]] += 1
                    # print(output.keys())
            
            if str(output[value]) != '0':     
                print(key + "  " + str(output[value]) + " * " + str(value)  + "    cost =  " +  str(int(output[value])*int(value)))
                x = (int(output[value])*int(value))  + x 
    print("total " + str(x))
    print("thank you ")

# used for buy new product and save it innew array
def Buy():
    product_id = input("enter product id: ")
    if int(product_id) in products:
    # arr.append(products[key])
        arr.append(products[int(product_id)])
        print(arr)
        soc = input("[enter esc to back to last board and ignor last uncomplete changeable] # must press enter to active value")
        while str(soc) != "esc" :   
            Buy()
            break
        Customer()
    else:
        print("there is no number 5 'product' ")
# show list of products used by  customer
def showProduct_cus():
    print("id product cost")
    for key  in products.copy():
        for key2 in (products[int(key)]):   
            print(str(key) + "  " + str(key2) + "   " + str((products[key][key2])))
    print("=" * 50)
    out = input("enter esc to back to last board : ")
    print("=" * 50)
    if out == "esc" :
        Customer()
    else :
        Customer()
# Owner method
# Delete Product
def DeletePrdocut():
    res_type = ["y","Y" , "yes" "YES"  , "Yes" , "YeS","yeS"]
    product_id = input("enter product id: ")
    for key in products.copy():
        if key == int(product_id):
            for key2, value in products[int(product_id)].items():
                print("delete product  [" + key2 + "], cost [" +  value +"]")
                conf = input("(yes/no): ")
                for x in res_type :
                    if x == conf :
                        products.pop(key)
                        print("done Delete product [" + key2 +"], cost [" +  value +"]" )

# Change Product
def ChangeProduct():
    product_id = input("enter product id: ")
    for key  in products.copy():
        if key == int(product_id):
            for key2, value in (products[int(product_id)].items()):
                print("product name [" + key2 + "], cost [" +  value +"]")
                new_cost = input("enter new cost:")
                products[key][key2] = new_cost
                print("done product [ "+ key2 +"], cost [" +  new_cost +"]" )

# show list of products used by owner 
def showProduct():
    print("id product cost")
    for key  in products.copy():
        for key2 in (products[int(key)]):   
            print(str(key) + "  " + str(key2) + "   " + str((products[key][key2])))
    print("=" * 50)
    out = input("enter esc to back to last board : ")
    print("=" * 50)
    if out == "esc" :
        choice()
    else :
        Owner()

# add new product
def addProduct():
    dic ={}
    last_key = list(products.keys())[-1]
    prdouct_name = input("product name: ")
    cost = input("product cost: ")
    dic={prdouct_name:cost}
    newdic={last_key+1:dic}
    products.update(newdic) 
    print(products)
    print("Done")
    print("=" * 50)
    out = input("enter esc to back to last board : ")
    print("=" * 50)
    if out == "esc" :
        choice()
    else :
        Owner()       


        
# Owner Master Function   
def Owner():
    count=0
    for key, value in database.items():
        while count < 3:
            username = input('Enter username: ')
            password = input('Enter password: ')
            if password== value and username == key:
                print('Welcome ' + username)
                choice()
            
            else:
                print('Access denied. Try again.')
                count += 1
        break    

# Customer Master Function
def Customer():
    print("""
=================
Welcome Customer  
1- show products
2- Buy products
3- print bill
""")
    choice = int(input("select operation :  "))
    if choice == 1:
        showProduct_cus()
    elif choice == 3:
            Bills()         
    elif choice == 2:   
        Buy() 
      
def welcome():
    print("=" * 100)
    print("Welcome to ITI Shop \n")
    print("""1- Owner
2- user
3- exit
Select Mode For customer press 1 , for owner press two , to exist press 0 :   \n""")
    print("=" * 100)
    option = input()
    if int(option) == 1:
        Owner()
    elif int(option) == 2 :
        Customer()    
    elif int(option) == 0 :
        print("Thank You ")
        exit()    



welcome()