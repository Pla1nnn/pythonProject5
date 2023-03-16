def prog1(a):
    while True:
        if (a % 3 == 0):
            print("Делится")
            break
        else:
            print("Error")
            break
prog1(6)

def prog2(a):
    b = float()
    try:
        b = 100 / float(a)

    except ValueError:
        print("Error")
    except ZeroDivisionError:
        print("Error")
    else:
        print (100 / float(a))


    return b
prog2(0)
def prog3(a:str):
    try:
        a = a.split(".")
        if int(a[0]) * int(a[1]) == int(a[2]):
            print("True")
        else:
            print("False")
    except:
        print("Error")
prog3("03.11.22")
def prog4(a:str):
    b = sum([int(i) for i in a[:int(len(a)/ 2)]])
    c = sum([int(i) for i in a[int(len(a) / 2):]])
    if (b == c):
        print(True)
    else:
        print(False)
prog4("123123")

