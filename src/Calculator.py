from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

    def subtract(self, a, b):
        self.result = a - b
        return subtraction(a, b)

    def multiply(self, a, b):
        self.result = a * b
        return multiplication(a, b)

    def divide(self, a, b):
        self.result = a / b
        return division(a, b)