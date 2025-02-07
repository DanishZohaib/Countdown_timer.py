# # my calculator

# user_num1 = int(input("Enter your 1st number: "))
# user_operator = input("Enter your operator i.e + - * / % : ")
# user_num2 = int(input("Enter your 2nd number: "))

# def calculate(num1, operator, num2):
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         elif operator == '%':
#             return num1 % num2
#         else:
#             return "Invalid operator"

# result = calculate(user_num1, user_operator, user_num2)
# print(f"The result of {user_num1} {user_operator} {user_num2} is: {result}")


num1=int(input("Enter your first number: "))
operator=input("Enter an operator i.e : + - * / % : ")
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
    elif operator=='%':
        return num1%num2

result=calculate(num1, operator, num2)
print(f"The result of {num1} {operator} {num2} is {result}")