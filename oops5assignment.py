# # 1.Square Numbers and Return Their Sum
# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def sqSum(self):
#         return self.x**2 + self.y**2 + self.z**2
# point = Point(1, 3, 5)
# print(point.sqSum())
# # outout 35

# 2.Implement a CalculatorClass
# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def add(self):
#         return self.num1 + self.num2
#     def subtract(self):
#         return self.num2 - self.num1
#     def multiply(self):
#         return self.num1 * self.num2
#     def divide(self):
#         return self.num2 / self.num1
# calc = Calculator(10, 94)
# print(calc.add())  # Output: 104
# print(calc.subtract())  # Output: 84
# print(calc.multiply())  # Output: 940
# print(calc.divide())  # Output: 9.4

# 3.Implement the Complete Student Class
# class Student:
#     def __init__(self):
#         self._name = ""
#         self._rollNumber = ""
#     def setName(self, name):
#         self._name = name
#     def getName(self):
#         return self._name
#     def setRollNumber(self, rollNumber):
#         self._rollNumber = rollNumber
#     def getRollNumber(self):
#         return self._rollNumber
# student = Student()
# student.setName("John Doe")
# print(student.getName())  # Output: John Doe
# student.setRollNumber("12345")
# print(student.getRollNumber())  # Output: 12345

# 4.Implement a Banking Account
# class Account:
#     def __init__(self, title, balance):
#         self.title = title
#         self.balance = balance
# class SavingsAccount(Account):
#     def __init__(self, title, balance, interestRate):
#         super().__init__(title, balance)
#         self.interestRate = interestRate
# account = Account("Ashish", 5000)
# print(account.title)  # Output: Ashish
# print(account.balance)  # Output: 5000
# savingsAccount = SavingsAccount("Ashish", 5000, 5)
# print(savingsAccount.title)  # Output: Ashish
# print(savingsAccount.balance)  # Output: 5000
# print(savingsAccount.interestRate)  # Output: 5

# Handling a Bank Account
# class Account:
#     def __init__(self, title=None, balance=0):
#         self.title = title
#         self.balance = balance
#     def withdrawal(self, amount):
#         self.balance -= amount
#     def deposit(self, amount):
#         self.balance += amount
#     def getBalance(self):
#         return self.balance
# class SavingsAccount(Account):
#     def __init__(self, title=None, balance=0, interestRate=0):
#         super().__init__(title, balance)
#         self.interestRate = interestRate
#     def interestAmount(self):
#         return self.balance * self.interestRate / 100
# demo1 = SavingsAccount("Ashish", 2000, 5)
# demo1.deposit(500)
# print(demo1.getBalance())  # Output: 2500
# demo1.withdrawal(500)
# print(demo1.getBalance())  # Output: 2000
# print(demo1.interestAmount())  # Output: 100

