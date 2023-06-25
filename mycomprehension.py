students=[{'name':'john','marks':50},
          {'name':'mary','marks':60},
           {'name':'james','marks':70},
            {'name':'peter','marks':65},
             {'name':'simon','marks':80},
              {'name':'ann','marks':40} ]
#create an empty list of students above 50#
# new=[]
# for i in students:
#     if i['marks']>50:
#         new.append(i['name'])
# print(new)

new=[i['name'] for i in students if i['marks']>50]
print(new)