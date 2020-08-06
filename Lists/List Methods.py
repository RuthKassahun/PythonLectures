# pop() remove an element starting from the last element of the list (index =-1)

items = ["milk","bread","orange"]

items.pop()
deleted_item = items.pop()
print(deleted_item)
print(items)

items.append("tea")
print(items)

items.pop(1)
print(items)

#remove() remove element from the list but unlike to pop it doesn't return deleted value

items2 = ["pencil","pen","eraser","sharpner"]
#results None
deleted_item2 = items2.remove("pencil")
print(deleted_item2)

#Why does pop return a value and remove doesn’t? Well, when we are calling remove, we already know the value that we want to remove.

# index() - to find the index position of a value

print(items2.index("pen"))

#insert()- takes two paramenters, an indext to insert in and a value to insert

print(items2)
items2.insert(0,"pencil")
print(items2)
# clear() - removes the entire list

items2.clear()
print(items2)

#count() - count the number of times a value exsists

items3 = ["pencil","pen","eraser","pen"]
print(items3.count("pen"))
print(items3.count("eraser"))

#reverse() - reverse the order of the list
print(items3)
print(items3.reverse())
print(items3)

#sort() - compare values and put it in order

num_lst = [1, 0.5, 3.6, 17, 121, 12.1]
print(num_lst)

num_lst.sort()
print(num_lst)

