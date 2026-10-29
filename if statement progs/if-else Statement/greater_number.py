# Write a program to find the greater of two numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number > second_number:
    print(f"{first_number} is greater.")
elif second_number > first_number:
    print(f"{second_number} is greater.")
else:
    print("Both numbers are equal.")