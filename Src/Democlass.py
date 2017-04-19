class1={'Ankur', 'Sethi', 'Pune'}

class2={'Pune', 'Max', 'Paul'}

print(class1.union(class2))
print(class1.intersection(class2))
print(class1.difference(class2))

print(class1.intersection(class2).issubset(class2))
print(class2.issuperset(class1.intersection(class2)))

print(class1.isdisjoint(class2))
