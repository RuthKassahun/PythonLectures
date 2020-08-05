message = 'Hello world'
# firstchar = message[0]
# lastchar = message[-1]
# slicing_msg = message[:-6]
# slicing_msg2 = message[6:]
# print(firstchar)
# print(lastchar)
# print(slicing_msg)
# print(slicing_msg2)

# Error might occur if we access indexes that are not in range

slicing_msg3 = message[15:]
print(slicing_msg3)

# This has no error even though the index doesn't exist
slicing_msg3 = message[:15]
print(slicing_msg3)

slicing_msg4 = message[:-1]
print(slicing_msg4)

slicing_msg5 = message[-1:]
print(slicing_msg5)


