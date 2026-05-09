class Expression:
    
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def solve(self):
        
        if self.operator == '+':
            return self.num1 + self.num2

        elif self.operator == '-':
            return self.num1 - self.num2

        elif self.operator == '*':
            return self.num1 * self.num2

        elif self.operator == '/':
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Division by zero not possible"

        else:
            return "Invalid Operator"

    def display(self):
        result = self.solve()
        print("Expression:", self.num1, self.operator, self.num2)
        print("Result =", result)


n1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
n2 = float(input("Enter second number: "))

obj = Expression(n1, n2, op)

obj.display()