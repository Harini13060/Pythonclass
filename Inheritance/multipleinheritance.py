class family1:
  def name1(self):
    print("parent name 1")
    print("children name 1")
class family2:
  def name2(self):
    print("parent name 2")
    print("children name 2")
class family3(family1,family2):
  def name3(self):
    print("parent name 3")
    print("children name 3")
amma=family3()
amma.name1()
amma.name2()
amma.name3()