try:
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    result = int(first_number) + int(second_number)
    
    print("The sum is:", result)

except ValueError:
    print("Error: Please enter valid numbers.")