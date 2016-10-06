Celcius = float(input("Enter a value in Celcius: "))

x = (Celcius + 273.15)
output = round(x,2)
if output < 0:
    print ("Thats an invalid value you entered")
if output >= 0:
    print(("The given value is: "), output ,("Kelvin"))
    quit
