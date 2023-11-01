#steps1-4
for count in range(0,10):
    print(count,end='')
print()
for count in range (1,10):
    print(count,end='')
print()
for count in range(1,10,2):
    print(count,end='')
print()
#steps5-6
import math
area=0.00
radius=float(input('Enter Radius'))
if(radius>0):
    print('Valid Input')
    area= math.pi*radius*radius
    print('Circle Area',area)
else:
    print('Invalid Input')
#steps7-11
area=0.00
length = float(input('Enter the length:'))
if(length>0):
    print('Valid Input')
else:
    print('Invalid Input')
breadth = float(input('Enter the breadth:'))
if(breadth>0):
    print('Valid Input')
else:
    print('Invalid Input')
if(length,breadth == 'Valid Input'):
    area = length * breadth
    print('Rectangle Area', area)
else:
    print('Invalid Input')