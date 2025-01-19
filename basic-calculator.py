while True:
    print("Simple Calculator Using Python!")
    print("Choose an operation\n"
          "1. Add (+)\n"
          "2. Subtract (-)\n"
          "3. Multiply (*)\n"
          "4. Divide (/)")
    select = int(input("Select the operations from 1-4 : "))
  
    # Define x + y as the number
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
  
    # Condition
    if select == 1:
        print("Result:", x, "+", y, "=", x + y)
    elif select == 2:
        print("Result:", x, "-", y, "=", x - y)
    elif select == 3:
        print("Result:", x, "*", y, "=", x * y)
    elif select == 4:
        print("Result:", x, "/", y, "=", x / y)
    else:
        print("Invalid input, please select a valid number!")
      
    # Condition for Next Calculation
    calculation = input("Do you want to do another calculation? (yes/no): ")
    if calculation == "yes":
        print("====================\n")
    elif calculation == "no":
        print("Goodbye, thanks for using this calculator!")
        break
