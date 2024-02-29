#3,write a program to create mini calculator
num1=int(input("Enter the number :"))
num2=int(input("Enter the other number :"))

print("""
press 1 for add
press 2 for sub
press 3 for mul
press 4 for div
""")
choice= int(input("Enter your choice"))

if choice == 1:
  print("add: ",num1+num2)
elif choice ==2:
  print("sub:",num1-num2)
elif choice ==3:
  print("mul:",num1*num2)
elif choice ==4:
  print("div:",num1/num2)
else:
  print("enter correct choice")