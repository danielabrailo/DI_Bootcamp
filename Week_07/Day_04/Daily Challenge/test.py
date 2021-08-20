# Daily challenge

def calc():
    try:
        5/0
    except ZeroDivisionError:
        print("Can't divide by zero")

