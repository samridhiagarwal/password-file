passwordFile = open('name.txt')
secretPassword = passwordFile.read()
secretPassword = secretPassword.strip()
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
elif typedPassword == 'abcdefg':
    print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
