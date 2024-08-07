#Extracting initial from first and last Name using map function
 
names = ["ranjith selva","Vana sakthi","Kairaa Ranjith","Akil krishnamoorthi","Arun sakthi"]

"""initials =list(map(lambda name:name.split()[0][0]+name.split()[1][0],names))

print(initials)
"""
#alternatively

initial_for = list(map(lambda name: "".join([i[0] for i in name.split()]),names))
print(initial_for)