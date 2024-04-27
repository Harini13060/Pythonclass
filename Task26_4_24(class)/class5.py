class fruits():
  def __init__(self):
    print("Fruits")
class mango(fruits):
  def __init__(self):
    print("Mango")
    super().__init__()
Orange=mango()