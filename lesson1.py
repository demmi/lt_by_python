user_name = input ("Enter your name:")
user_year = int(input ("Enter your year of birth:"))
user_age = 2022 - user_year
print (f'Hello, {user_name}. You are {user_age} years old')

password = input("Enter your password:")
password2 = input("Enter your password again:")
if password == password2:
    print("You have entered a valid password")
else:
    print("Your password is incorrect!")

number = int(input("Enter your number:"))
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")


