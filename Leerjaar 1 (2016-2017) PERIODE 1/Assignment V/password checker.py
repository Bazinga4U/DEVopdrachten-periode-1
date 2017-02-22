import re

def password():
    return(input('password: '))

def check_strength():
    strength_ammount()
    hoofdletters_ammount(hoofdletters)
    special_chars_ammount(special_chars)
    password_length_ammount(pass_length)

def strength_ammount():
    if strength < 5:
        print ('password is weak')
    elif strength > 5 and strength < 8:
        print ('password is medium')
    else:
        print ('password is strong')


def hoofdletters_ammount(hoofdletters_count):
    if hoofdletters_count < 6:
        strength = strength + 1
    elif hoofdletters_count < 10 and hoofdletters_count > 6:
        strength = strength + 2
    else:
        strength = strength + 3

def special_chars_ammount(special_chars_count):
    if special_chars_count < 4:
        strength = strength + 1
    elif special_chars_count < 10 and special_chars_count > 4:
        strength = strength + 2
    else:
        strength = strength + 3

def password_length_ammount(password_length):
    if password_length < 6:
        strength = strength + 1
    elif password_length < 10 and password_length > 6:
        strength = strength + 2
    else:
        strength = strength + 3


strength = 0
hoofdletters = 0
special_chars = 0
wachtwoord = password()
for letter in wachtwoord:
    if letter.isupper():
        hoofdletters = hoofdletters + 1
    elif re.match("\W", letter):
        special_chars = special_chars + 1
pass_length = len(wachtwoord)

check_strength()
