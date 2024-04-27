class saree():
  def __init__(self):
    super().__init__()
    print("Saree")
  def traditional(self):
    print("Traditional")
class cotton_saree():
  def __init__(self):
    print("Cotton saree")
class silk_saree(saree,cotton_saree):
  def __init__(self):
    super().__init__()
    print("Silk Saree")
saree_collection=silk_saree()
saree_collection.traditional()