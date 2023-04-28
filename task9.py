# Write a program called stars.py. 
# It should prompt the user for a number, and it should print the number of stars till the number entered.
# number = int(input('Enter a number: '))
# for i in range (number):
#         for j in range (i+1):
#           print('*',end='')
#           print()
      

number = int(input('Enter a number: '))
for i in range (number):
  print('*'*(i+1))