class maths():
    def add(self,num1,num2,num3):
        self.no1=num1
        self.no2=num2
        self.no3=num3
        print("Addition", self.no1 + self.no2 + self.no3)
    def sub(self,number1,number2):
        self.int1=number1
        self.int2=number2
        print("Subtraction",self.int1 - self.int2)
class multiply(maths):
    def mul(self):
        print("Multiplication")
class division(multiply):
    def divide(self, integer1, integer2):
        self.number1=integer1
        self.number2=integer2
        print("Division",self.number1 / self.number2)
math=division()
math.divide(6, 2)
math.mul()
math.add(6, 13, 0)
math.sub(19, 6)