# my calculator

num1=int(input("Enter your first number: "))
operator=input("Enter an operator i.e : + - * / : ")
# print(type(operator))
num2=int(input("Enter your second number: "))
def calculate (num1, operator, num2):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        return "Invalid operator"

result=calculate(num1, operator, num2)
print(f"The result of {num1} {operator} {num2} is {result}")