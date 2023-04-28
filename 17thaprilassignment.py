taskList = [23, 'Jane', ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John"),'Jane']
# 1. Determining class of taskList using an inbuilt function
print(type(taskList))
# 2. Print KES
print(taskList[2][2]["currency"])
# 3. Print 560
print(taskList[2][1])
# 4. Use a function to determine the length of taskList
print(len(taskList))
# 5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.

taskList[3]=int(str(taskList[3])[::-1])
print(taskList)
# For number 5 above we can research the solution online

# 6. Change the name “John” to “Jane” . 
taskList[4]=list(taskList[4])
taskList[4][1]='Jane'
taskList[4]=tuple(taskList[4])
print(taskList)
# 7. In the dictionary with the key currency, add another key “amount” with value 90
taskList[2][2]['amount']=90
print(taskList)

del taskList('Jane')
print(taskList)
