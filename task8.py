#Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driv20er one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”.

speed = int(input('Enter speed: '))
if speed <= 70:
    print('Ok!')

demerit_points=0
#     print(len(list(range(70,speed,5))))
# demerit_points=0
if speed <76 and speed > 71:
    print ('The demerit points are ',((speed-71)/5))
for i in range (71,speed,5):
    demerit_points = demerit_points + 1
    if (speed-71)/5 != 0:
        print('The points are',((speed -71)/5))
print ("Points:",demerit_points)
if demerit_points > 12:
    print ('License Suspended')


