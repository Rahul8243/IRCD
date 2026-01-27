# Input
a = int(input('enter first number:'))
b = int(input('enter second number:'))


while b != 0:
    a, b = b, a % b

if a == 1:
    print("The numbers are Co-Prime")
else:
    print("The numbers are Not Co-Prime")
