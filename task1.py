def Seintific(operation , num1 , num2):
    if operation == 1 :
        print("sum=" , num1 + num2)
    elif  operation == 2 :
        print("sub=" , num1 - num2)
    elif operation == 3:
        print("mult=", num1 * num2)
    elif operation == 4:
        print("div=", num1 / num2)
    elif operation == 5:
        print("Mod=", num1 % num2)
    elif operation == 5:
        print("exp=", num1 ** num2)
    else :
        print("Error sign")

def programming(input_type , num) :
    if input_type == 1 :
       binary_num = bin(num).replace("0b", "")
       octal_num = oct(num)
       hex_num = hex(num)
       print(f"binary num = {binary_num} , octal number = {octal_num}, hex number = {hex_num}")
    elif input_type == 2 :
        decimal_num = int(num , 2)
        octal_num = oct(decimal_num)[2:]
        hex_num = hex(decimal_num)
        print(f"decimal_num = {decimal_num} , octal number = {octal_num}, hex number = {hex_num}")
    elif input_type == 3 :
        decimal_num = int(num,8)
        binary_num = bin(decimal_num)
        hex_num = hex(decimal_num)
        print(f"decimal_num = {decimal_num} , binary_num = {binary_num}, hex number = {hex_num}")
    elif input_type == 4 :
        decimal_num = int(num,16)
        binary_num = bin(decimal_num)
        octal_num = oct(decimal_num)
        print(f"decimal_num = {decimal_num} , binary_num = {binary_num}, octal_num = {octal_num}")


while True :
    print('''Choose type of calculator :
                 1- Scientific Cal
                 2- programming cal
                 ''')

    cal = int(input("Enter type of calculator :"))

    if cal == 1 :
        print('''Enter type of operation 
                 1- sum
                 2- subtraction
                 3- multiply
                 4- division 
                 5- Module
                 6- exponent
                 ''')
        op = int(input("Enter number of operation :"))
        num1 = float(input("Enter num1"))
        num2 = float(input("Enter num2"))
        Seintific(op ,num1 , num2)

    elif cal == 2 :
        print('''Enter type of the  input
                1- decimal
                2- binary
                3- octal 
                4- Hexdecimal
                ''')
        op = int(input("Enter input type :"))
        num = int(input("Enter number"))
        programming(op , num)