logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1, n2):
    """This function is use to add two numbers"""
    return n1 + n2
def subtract(n1, n2):
    """This function is use to subtract two numbers"""
    return n1 - n2
def multiply(n1, n2):
    """This function is use to multiply two numbers"""
    return n1 * n2
def divide(n1, n2):
    """This function is use to divide two numbers"""
    if n2 == 0:
        return 
    else:
        return n1 / n2
calculate={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}
value=True
while value:
    num1=float(input("Enter the first number: "))
    print("Operations are: ")
    for key, func in calculate.items():
        print(f" {key} -> {func.__name__}")
    operation=input("Enter the operation you want to perform: ")
    if operation in calculate:
        num2=float(input("Enter the second number: "))
        result=calculate[operation](num1,num2)
        if result == None:
            print("Result is: UNDEFINED")
        else:
            print(f"Result is: {result:.2f}")
    else:
        print("Invalid operation entered!")
    repeat=input("Type 'yes' to continue or 'no' to exit: ").lower()
    if repeat == 'yes':
        value=True
        print('\n'*3)
    elif repeat == 'no':
        value=False
        print("Thank You!")
    else:
        value=False
        print("Invalid Input!")