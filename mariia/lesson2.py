health = int(input("What is the hero's health?"))
if health > 0:
    print("True")
else:
    print("False")

number = int(input("Enter the nubmer:"))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

year = int(input("Enter the year:"))
if year % 4 == 0 and year % 400 == 0:
    print("The year", year, "is a leap year.")
elif year % 100 == 0:
    print("The year", year, "is NOT a leap year.")
else:
    print("The year", year, "is NOT a leap year")

text = input("Enter your text here:")
times = int(input("How many times should I print this text?"))
i = 1
while i <= times:
    i = i+1
    print(text)