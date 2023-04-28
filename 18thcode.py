ls1=["Mombasa", ["Kitale", ("Eldoret", "Fill"),("Nakuru")]]
#replace fill with machakos
ls1[1][1]=list(ls1[1][1])

ls1[1][1][1]=('machakos')
ls1[1][1]=tuple(ls1[1][1])

print(ls1)