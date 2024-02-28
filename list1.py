#1,write a program to swap first and last element of list
num=[1,2,3,4,5,6]
print("unchanged list",num)
temp = num[0]
num[0] = num[-1]
num[-1]=temp
print("changed list",num)