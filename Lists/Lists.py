# using list constructor
items = list()

# using list literally
items = []

print(len(items))

#Elements in the list can be changed

items.append("milk")
items.append("eggs")
items.append("bread")

print(items)

item2 = ["rice","butter"]

print(item2[1])

#index error occurs when index we are trying to access doesn't exsist

print(items[:])