import time
def down():
    for i in range(6):
        print(' ' * 9 , '*')
    for i in range(9):
        print(' ' * i  ,'*' * (9-i) * 2  )

def up():
    for i in range(9) :
        print(' ' * (9-i) ,'*' * i *2 )

    for i in range(6):
        print(' '*9 + '*')

def right():
    for i in range (8):
        print(' ' * 9 +  '*' * i)

    print('*'*18)

    for i in range (8):
        print(' ' * 9 +  '*' * (7-i))


def left():
    for i in range(6):
        print(' '*(6-i) + '*'*i)

    print('*'*18)

    for i in range(6):
        print(' '*(i) + '*'*(6-i))


while True :
    up()
    time.sleep(1) #3s Delay!
    right()
    time.sleep(1) #3s Delay!
    down()
    time.sleep(1) #3s Delay!
    left()
    time.sleep(1) #3s Delay!