class Calculator:
    def __init__(self, current=0.0):
        self.current = current

    def add(self, second):
        self.current += second

    def multiply(self, second):
        self.current *= second

    def decrease(self, second):
        self.current -= second

    def divide(self, second):
        self.current /= second


calc = Calculator(1.0)
calc.add(5)
print(calc.current)
calc.decrease(3)
print(calc.current)
calc.multiply(5)
print(calc.current)
calc.divide(2)
print(calc.current)
