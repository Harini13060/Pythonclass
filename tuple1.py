#write a program to take a user input and add it to a tuple
a=input("Enter the items:")
b=tuple(a)
print(b)
change=list(b)
print(change)
change.append(6)
print(tuple(change))