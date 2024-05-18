def calculator(x, y, v):
    try:
        if (isinstance(x, int) or isinstance(x, float)or isinstance(y, int) or isinstance(y, float) or isinstance(v, float) or isinstance(v, float)):
            pass
            if v == "A":
                print(f"The addition of {x} and {y} is: {x + y}")
            elif v == "S":
                print(f"The Subtraction of {x} and {y} is: {x - y}")
            elif v == "D":
                if y == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"The Division of {x} and {y} is: {x / y}")
            elif v == "M":
                print(f"The Multiply of {x} and {y} is: {x * y}")
            else:
                print(f'"{v}" is not an option for an Operator')
    except ValueError:
        return ('Your value is invalid')
calculator(int(input("Enter your first value:\n")), int(input("Enter your second value:\n")), input("Enter your operator to calculate:\n").upper())

while True:
    print('''Use this calculator to Add, Subtract, Divide and Multiply:
            Choose "A" to Add,
                    "S" to Subtract,
                    "D" to Divide,
                    "M" to Multiply,
            your two values''')
    break
    # except ValueError:
    #     return ('Your value is invalid')

    
    
   
