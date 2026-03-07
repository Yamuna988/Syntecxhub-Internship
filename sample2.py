def add(a, b):
    return a + b  
def subtract(a, b):
    return a - b  
def multiply(a, b):
    return a * b  
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"  
    return a / b  
def calculator():
    while True:  
        print("\n--- Simple Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Clear")
        print("6. Exit")
        choice = input("Choose an option: ")  
        if choice == '6':  
            print("Exiting calculator...")
            break
        if choice == '5':  
            print("Calculator cleared!")
            continue
        if choice in ['1','2','3','4']:
            try:
                a = float(input("Enter first number: "))  
                b = float(input("Enter second number: "))  
            except ValueError:
                print("Invalid input! Please enter numbers.")  
                continue
            if choice == '1':
                result = add(a, b)
            elif choice == '2':
                result = subtract(a, b)
            elif choice == '3':
                result = multiply(a, b)
            elif choice == '4':
                result = divide(a, b)
            print("Result:", result)  
        else:
            print("Invalid choice. Try again.")  
calculator()