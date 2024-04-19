class family1:
  def name1(self):
    print("parent name 1")
    print("children name 1")
class family2(family1):
  def name2(self):
    print("parent name 2")
    print("children name 2")
appa=family2()
appa.name1()
appa.name2()