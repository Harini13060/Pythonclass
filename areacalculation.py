while True:
  print("\n1.Area of Circle\n2.Area of Rectangle\n3.Area of Triangle\n")
  num = int(input("Enter Choice:"))

  if num == 1:
    r = float(input("Enter Radius:"))
    AC = 3.14 * r * r
    print("Area of Circle=", AC)
  elif num == 2:
    l = float(input("Enter the Length:"))
    b = float(input("Enter the Breadth:"))
    AR = l * b
    print("Area of Rectangle=", AR)
  elif num == 3:
    b = float(input("Enter the Base:"))
    h = float(input("Enter the Height:"))
    AT = 0.5 * b * h
    print("Area of Triangle=", AT)
  else:
    print("Invalid Input")

  choice = input("\nDo you want to calculate another area? (yes/no): ")
  if choice == 'no':
    break
