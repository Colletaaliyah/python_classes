# week=['Monday', 'Tuesday', 'wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# new_week=week[0:] #the whole string is printed
# print(new_week)
# second_week=week[1:] #monday is eliminated
# print(second_week)
# third_week=week[0:2] #monday and tuesday is printed
# print(third_week)
# fourth_week=week[1:5] #tuesday to friday prints out
# print(fourth_week)
# fifth_week=week[0:-1] #sunday is eliminated
# print(fifth_week)
# sixth_week=week[0:-3]
# print(sixth_week)

trainees = ["John", [2, ["James","Mary"]]]
print('original list',trainees)

print(trainees[1][0])
print(trainees[1][1][0])
trainees.append(56)
print(trainees)

trainees[1][1].insert(1,'mike')
print(trainees)

trainees[1][0]=8
print(trainees)

trainees.remove('John')
print(trainees)

trainees[0][1].remove('Mary')
print(trainees)

print(len(trainees))
print('original list',trainees)
