# Creat a a table using user_input and error handling

try:
    table_of = int(input("Enter your digit to create table: "))
    for i in range(1, 6):  
        print(f"{table_of} x {i} = {table_of * i}")
except ValueError:
    print("Oops! That's not a valid number. Please enter an integer.")
