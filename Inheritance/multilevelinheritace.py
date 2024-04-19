class family1:
  def name1(self):
    print("parent name1")
    print("children name1")
class family2(family1):
  def name2(self):
    print("parent name2")
    print("children name2")
class family3(family2):
  def name3(self):
    print("parent name3")
    print("children name3")
amma=family3()
amma.name1()
amma.name2()
appa=family2()
appa.name1()
amma.name3()