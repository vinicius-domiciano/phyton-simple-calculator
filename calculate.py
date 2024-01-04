class Calculate:

    result = 0;

    def __init__(self, numberA: int, numberB: int) -> None:
        self.numberA = numberA
        self.numberB = numberB;

    def add(self):
        Calculate.result = self.numberA + self.numberB;

    def sub(self):
        Calculate.result = self.numberA - self.numberB;

    def multply(self):
        Calculate.result = self.numberA * self.numberB;

    def divide(self):
        Calculate.result = self.numberA / self.numberB;

class ExpressionResult:

    def __init__(self) -> None:
        pass

    def caucule(self, expression: int, numberA, numberB) -> int :
        calculate = Calculate(numberA, numberB)

        match expression:
            case 1:
                calculate.add();
            case 2:
                calculate.sub();
            case 3:
                calculate.multply();
            case 4:
                calculate.divide();
            case _:
                return -1;
    
        return calculate.result;

try:
    a = int(input("Please enter an number: "));
    b = int(input("Please enter another number: "));

    print("\nSelect an expression to your account")
    expression = int(input("1 - some\n2 - subtract\n3 - multiply\n4 - divide\n"))

    if expression < 1 or expression > 4:
        print("Sorry, but expression: " + str(expression) + " is invalid");
    else:
        result = ExpressionResult()
        print("The result is:", result.caucule(expression, a, b));
except:
    print("\nSorry, an error occurred!")
    