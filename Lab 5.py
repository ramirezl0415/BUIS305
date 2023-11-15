number1 = int(input('Enter a number: '))
if number1 % 3 == 0 and number1 % 5 == 0:
    print(number1, 'Tic Tac')
elif number1 % 3 == 0:
    print(number1, 'Tic')
elif number1 % 5 == 0:
    print(number1, 'Tac')
i = 1
while i <= 20:
    if number1 % 3 == 0 and number1 % 5 == 0:
        print(i, 'Tic Tac')
    elif number1 % 3 == 0:
        print(i, 'Tic')
    elif number1 % 5 == 0:
        print(i, 'Tac')
    i += 1

user_number = 0
count = 0

while count < 5:
    user_number = int(input('Enter Value:'))
    if user_number > 0:
        print('Greater than 0')
        break
    else:
        count += 1
        if count < 5:
            print('Try Again')
        else:
            print('Max Attempts')
            break

import random
random_number = random.randint(1,1000)
print('Random Number:',random_number)
print('User Number:',user_number)
if user_number == random_number:
    print('Match')
else:
    print('Not A Match')
