#str(input("Please put in an sentence you want to reverse: "))
#a = ord("a")
#print(chr(a))
#print(ord("a"))
#print(chr(ord("b")))

x = str(input("Please put in an sentence you want to reverse: "))
output = ""
for i in range(len(x)-1,-1,-1):
    output += x[i]

print(output)
