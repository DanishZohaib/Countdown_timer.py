# # # Creating table of 2 using for loop 
# # print("Table of 2 using for loop")
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for num in numbers:
# #     print(f"2 x {num} = {2*num}")

# # num = 1
# # while num <= 10:
# #     print(f"2 x {num} = {2*num}")
# #     num += 1



# # print("\nTable of 2 using while loop")
# # Creating table of 2 using while loop
# # num = 1
# # while num <= 10:
# #     print(f"2 x {num} = {2*num}")
# #     num += 1
    
    
# # obtained_marks=450
# # total_marks=500
# # percentage=(obtained_marks/total_marks)*100
# # print(f"Percentage is {percentage}%")
# # if percentage>=90:
# #     print("Grade A+")
# # elif percentage>=80:
# #     print("Grade A")
# # elif percentage>=70:
# #     print("Grade B")
# # elif percentage>=60:
# #     print("Grade C")
# # elif percentage>=50:
# #     print("Grade D")
# # else:
# #     print("Fail")


# for i in range(1,11):
#     print(f'3 x {i} = {3*i}')

    

# for i in range(1,11):
#     print(f"2 x {i} = {i*2}")


obtained_marks: int = 400
total_marks: int = 500
percentage = (obtained_marks/total_marks)*100
print(f'{percentage:.1f}' "%")
if percentage >=90:
    print("A+ Grade")
elif percentage >=80:
    print("A Grade")
elif percentage >=70:
    print("B Grade")
elif percentage >=60:
    print("C Grade")
elif percentage >=50:
    print("D Grade")
elif percentage >=40:
    print("E Grade")
else:
     print("Fail")