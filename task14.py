#Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only or otherwise display an error “invalid character
#  entered” and take the user to re-enter the inputs .
# while True:
#     try:
#         num = float(input('Enter a number: '))
#         num2 = float(input('Enter a number: '))
#         total = num + num2
#         print(total)
#         break
#     except ValueError:
#         print('Error: Invalid character entered')


for i in range(0,100):
    try:
        num = float(input('Enter a number: '))
        num2 = float(input('Enter a number: '))
        total = num + num2
        print(total)
        break
    except ValueError:
        print('Error: Invalid character entered')
