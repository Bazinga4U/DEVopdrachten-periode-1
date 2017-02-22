def abs_1():
    value = int(input("Please enter a value: "))
    if value <= 0:
        value = value * -1
    else:
        value = value * 1
    print(value)

abs_1()
