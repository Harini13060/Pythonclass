class school():
  def students(self,student,teacher):
    self.student1=student
    self.teacher1=teacher
    print("Student",self.student1)
    print("Teacher",self.teacher1)
class college(school):
  def professor(self):
    print("Professor")
class elementary_school(college):
  def children(self):
    print("Children")
books=elementary_school()
books.children()
books.professor()
books.students("Harini","Sri")