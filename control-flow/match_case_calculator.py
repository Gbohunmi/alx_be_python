num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /):"))
product = num1 * num2
addition = num1 + num2
difference = num1 - num2
division = num1 / num2

match operation:
    case "/":
        if num2 == 0:
            print( "Cannot divide by zero.")
        else:
            result = division

    case "+":
        result = addition

    case "-":
        result = difference
         
    case "*":
        result = product

print ( f"The result is {result}." )        