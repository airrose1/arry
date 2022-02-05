while True:
    print("Welcome to Faulty Calculator")
    print("First enter any two number and then the operator")
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    operator = str(input("Enter the operator (+,-,*,%,**,//,/) : "))
    answer = num1, operator, num2

    if num1 == 45 and num2 == 3 and operator == "*":
        print("555")
    elif num1 == 56 and num2 == 9 and operator == "+":
        print("77")
    elif num1 == 56 and num2 == 6 and operator == "/":
        print("4")
    elif operator == "+":
        print("The answer is", num1 + num2)
    elif operator == "-":
        print("The answer is", num1 - num2)
    elif operator == "*":
        print("The answer is", num1 * num2)
    elif operator == "/":
        print("The answer is", num1 / num2)
    elif operator == "**":
        print("The answer is", num1 ** num2)
    elif operator == "//":
        print("The answer is", num1 // num2)
    elif operator == "%":
        print("The answer is", num1 % num2)
    else:
        print("Please enter operator from the given choices only.")
