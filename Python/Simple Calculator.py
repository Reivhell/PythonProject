def calculator():

    class Calculator:
        def add(self, a, b):
            
            return a + b

        def subtract(self, a, b):
            return a - b

        def multiply(self, a, b):
            return a * b

        def divide(self, a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            return a / b    
        
    print("Welcome to the SimpleCalculator!")

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")        
    print("3. Multiply")
    print("4. Divide")
    operation = input("Enter choice (1/2/3/4): ")

    inputnum1 = float(input("Enter first number: "))
    inputnum2 = float(input("Enter second number: "))



    if operation in ['1', '2', '3', '4']:
        calc = Calculator()
        if operation == '1':
            print(f"{inputnum1} + {inputnum2} = {calc.add(inputnum1, inputnum2)}")
        elif operation == '2':
            print(f"{inputnum1} - {inputnum2} = {calc.subtract(inputnum1, inputnum2)}")
        elif operation == '3':
            print(f"{inputnum1} * {inputnum2} = {calc.multiply(inputnum1, inputnum2)}")
        elif operation == '4':
            try:
                print(f"{inputnum1} / {inputnum2} = {calc.divide(inputnum1, inputnum2)}")
            except ValueError as e:
                print(e)
    else:
        print("Invalid input")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == "y":
        calculator()
    else:
        print("Goodbye!")


calculator()