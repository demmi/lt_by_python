#2.1

# health = int(input("Enter current health:"))
# if health <= 0:
#     print(False)
# else:
#     print(True)
#

#2.2

# number = int(input("Enter number for testing:"))
#
# if number%2 == 0:
#     print('even')
# else:
#     print('Uneven')

#2.3
# year = int(input("Enter year:"))
#
# if year%4 ==0 and year%100 != 0 or year%400 == 0:
#     print(True)
# else:
#     print(False)

#2.4
# text = input("Enter text to be repeated:")
# number = int(input("Enter quantity of repeating:"))
# i = 1
# while i <= number:
#     print(text)
#     i += 1


text = input("Enter text to be repeated:")
number = int(input("Enter quantity of repeating:"))

for i in range(1, number+1):
    print(i, text)
