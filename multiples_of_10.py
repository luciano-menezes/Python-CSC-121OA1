# Ask the user for a number
number = (input("Enter a number: "))
number = int(number)

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(number, "is a multiple of 10.")
else:
    print(number, "is not a multiple of 10.")