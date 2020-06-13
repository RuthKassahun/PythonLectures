# variables are identifies that holds values of diffrent data types

age = 10            # Age holds the int value 10
name = "Abebe"      # name holds the string value abebe
mark = 88.5         # mark holds the float value 88.5

'''
Naming Conventions
don't use keywords as a name of a variable like print,float,int,new
don't start a variable name with digits, varibale name can start with letter or underscore
'''
'''
Example of Invlaid variable name
1age = 5
print(lage)
'''

age = 10
age = 15

print(age)

age = 15
newage = age

print(newage)

#Python is dynamically typed language

name = "Abebe"
name = 12

print(name)

#swapping

name = "Abebe"
newname = "Abeba"

name, newname = newname, name

print(name)
print (newname)

me ="apple"
friend = "money"

print("you have"+ me)
print("Your friend have"+ friend)

me, friend = friend, me

print("now you have "+me)
print("now your friend have"+friend)