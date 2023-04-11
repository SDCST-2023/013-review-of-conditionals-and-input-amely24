"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

hypotenuse = input("Is one of the numbers the hypotenuse of a right triangle? (yes/no): ").lower()

if hypotenuse == "yes":
    side = (abs(a**2 - b**2))**0.5
    s = round(side, 1)
    print("The length of the missing side is:", s)
elif hypotenuse == "no":
    side = (abs(a**2 + b**2))**0.5
    s = round(side, 1)
    print("The length of the missing side is:", s)
else:
    print("Invalid input")

