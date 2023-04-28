# working with a tuple
days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday")
print(days)
# 1. Find wednesday using an index
print(days[2])
print(len(days))
days=list(days)
days[3]="thur"
days=tuple(days)
print(days)

