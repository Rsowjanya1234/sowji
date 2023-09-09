addition_result = None
subtraction_result = None
multiplication_result = None
division_result = None
while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' to display all outputs")
    print("Enter '6' to quit")
    choice = input("Enter your choice: ")
    if choice == '6':
        break
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        if choice == '1':
            addition_result = a + b
            print("Result:", addition_result)
        elif choice == '2':
            subtraction_result = a - b
            print("Result:", subtraction_result)
        elif choice == '3':
            multiplication_result = a * b
            print("Result:", multiplication_result)
        elif choice == '4':
            if b != 0:
                division_result = a / b
                print("Result:", division_result)
            else:

                print("Cannot divide by zero")
    elif choice == '5':
        print("Addition Result:", addition_result)
        print("Subtraction Result:", subtraction_result)
        print("Multiplication Result:", multiplication_result)
        if subtraction_result is not None:
            if b != 0:
                print("Division Result:", division_result)
            else:
                print("Division: Cannot divide by zero")
else:
    print("Invalid input. Please enter a valid option.")
 
