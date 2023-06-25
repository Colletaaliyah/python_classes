# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!

num=int(input('Enter a number: '))
num2=int(input('Enter a num2: '))
num3=int(input('Enter a num3: '))
# if num > num2 and num3 :
#     print('largest number is: ',num)
# elif num2 > num3 and num:
#     print('largest number is: ',num2)
# elif num3 > num and num2:
#     print('largest number is: ',num3)
max_value=max(num,num2,num3)
print(max_value)
