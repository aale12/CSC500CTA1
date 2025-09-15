def AddAndSubtract(a, b):
    return "a + b = " + str(a + b) + ", a - b = " + str(a - b)

def MultiplyAndDivide(a, b):
    if b == 0:  # Error handling for division by zero
        return "Division by zero is undefined"
    return "a * b = " + str(a * b) + ", a / b = " + str(a / b)

def main(): 
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    print(AddAndSubtract(a, b))
    print(MultiplyAndDivide(a, b))  

if __name__ == "__main__":
    main()

