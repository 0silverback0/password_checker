import re

is_8_chars = False
has_caps = False
has_digit = False

caps = re.compile(r"[A-Z]")
digit = re.compile(r'\d')

def passwordcheck():
    password = input('Enter a password: ')

    if len(password) < 8:
        print('Password must be 8 or more characters long')
        passwordcheck()

    elif len(password) >= 8:
        is_8_chars = True

        if hasCaps(password) == True and hasDigit(password) == True:
            print("STrong password")
        elif hasCaps(password) == False:
            print('Must have a capital character')
            passwordcheck()
        elif hasDigit(password) == False:
            print('Must have a digit')
            passwordcheck()
    else:
        print("Password must have 8 chars, a cap, and a digit")
        passwordcheck()

def hasCaps(pwd):
    check = caps.search(pwd)
    try:
        if check.group():
            has_caps = True
            return True
    except AttributeError:
        has_caps = False
        return False

def hasDigit(password):
    check = digit.search(password)
    try:
        if check.group():
            has_digit = True
            return True
    except AttributeError:
        has_digit = False
        return False

passwordcheck()
