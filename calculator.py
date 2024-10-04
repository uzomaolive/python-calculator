operator = input("Enter operator (+ - * /): ") # input() function is used to take input from the user
num1 = float(input("Enter 1st number: ")) # float() function is used to convert the input to float
num2 = float(input("Enter 2nd number: ")) 

if operator == '+': 
    result = num1 + num2 # + operator is used to add two numbers
    print(round(result, 3)) # round() function is used to round off the result to 3 decimal places
elif operator == '-':
    result = num1 - num2
    print(round(result, 3)) # round() function is used to round off the result to 3 decimal places
elif operator == '*':
    result = num1 * num2
    print(round(result, 3)) # round() function is used to round off the result to 3 decimal places
elif operator == '/':
    result = num1 / num2
    print(round(result, 3)) # round() function is used to round off the result to 3 decimal places
else: 
    print(f"{operator} is not a valid operator") # f-string is used to format the string