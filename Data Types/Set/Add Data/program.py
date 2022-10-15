'''There are two method to add the element in the set'''
'''
1 - add():- It is used to add the single data as  one time  only .

2 - update():- It is used to add the multiple data in a single time .


'''


# example 1 :-  ADD

a = set()
name = "pushpendra"

age = 22

loc = "thane"

a.add(name)
a.add(age)
a.add(loc)
print(a)


#example 2 :-   Update
a = set()

data = {"pushpnedra","thane",22,"manpada"}

a.update(data)
print(a)