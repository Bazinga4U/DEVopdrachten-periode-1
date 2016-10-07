alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = input("Enter a message here ")
encryptedMessage =""
key = input("Please enter a key: ")
key = int(key)

for char in message:

    if char in alphabet:
        position = alphabet.find(char)
        newPosition = (position+key) %26
        encryptedMessage = encryptedMessage + alphabet [newPosition]
    else:
        encryptedMessage = encryptedMessage + char

print ("Your encrypted message is ", encryptedMessage)
