#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,
# months,days TODAY.
# from datetime import datetime

DOB = (input('My date of birth is (dd-mm-yyy): ').split('-'))
mydobnew = []
for i in DOB:
    mydobnew.append(int(i))

DOB = mydobnew

if len(DOB)!=3 or DOB[0] > 31 or DOB[0] < 1  or DOB[1] < 1 or DOB[1]<1 or DOB[1]>12 or DOB[2]>2023 \
or len(str(DOB[2])) != 4 or (DOB[1] == 2 and DOB[0] > 29)\
or (DOB[1]==2 and DOB[0] > 28 and DOB[2] % 4 !=0 ) or (DOB[1] % 2 == 0 and DOB[0] > 30 and DOB[1] < 8)\
or (DOB[1] % 2 != 0 and DOB[0] > 30 and DOB[1] > 7):
    print('invalid date')
else:
    print(DOB)



