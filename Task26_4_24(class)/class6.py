class chair():
  def number(self,a,b):
    self.a1=a
    self.b1=b
    print(self.a1+self.b1)
class table(chair):
  def duster(self):
    print("Table")
class desk(table):
  def classroom(self):
    print("Classroom")
blackboard=desk()
blackboard.classroom()
chalk_peice=table()
chalk_peice.number(13,6)
chalk_peice.duster(