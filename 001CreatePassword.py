import string,random

while True:
    length = int(input('Plaese enter your preferred password length : '))

    chars = string.ascii_letters + string.digits + '!~@#$%&-+*'

    password = ''.join([random.choice(chars) for i in range(length)])

    print('Your password : {}'.format(password))

    while True:
        answer = input('do you want another password (Y/n) : ').lower()

        if answer =='n' or answer =='y' :
            break

    if answer == 'n' :
        break
    