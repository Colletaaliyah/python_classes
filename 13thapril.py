# Given two integer variables m and p, write expressions that use the assignment operator to perform the following operations:
# a. Add p to m and store the result in m.
# b. Subtract p from m and store the result in m.
# c. Multiply m by p and store the result in m.
# d. Divide m by p and store the result in m.
# e. Calculate the remainder of m divided by p and store the result in m.


temp=56.8926
print(int(round(temp)))
temp=56.8926
print(round(temp,1))
temp=56.8926
print(round(temp,3))
temp=56.8926
new_temp=str(temp)
first_temp=new_temp[3:4]
second_temp=new_temp[4:]
new_string=first_temp+'.'+second_temp
temp=float(new_string)
print(temp)
print(type(temp))