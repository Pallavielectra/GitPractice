
class Calculator:

    num = 100
    #Default Constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("i am called automatically when objects are created")
    def getData(self):
        print("I am executing as a method in class")

    def Summation(self):
        return self.firstNumber+self.secondNumber+Calculator.num

obj = Calculator(2,3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,10)
obj1.getData()
print(obj1.Summation())

