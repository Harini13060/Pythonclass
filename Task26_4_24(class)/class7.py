class dresses():
  def __init__(self,name,quality):
    self.name1=name
    self.fabric=quality
    print("Dress Name",self.name1)
    print("Dress Quality",self.fabric)
class shirts(dresses):
  def kurtis(self):
    print("kurtis")
leggins=shirts("Cotton kurti","good")
leggins.kurtis()