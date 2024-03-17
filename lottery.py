from random import choice

lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
lottery_numbers = [choice(lottery_list) for _ in range(4)] 
+ [choice(lottery_list)]

user_input = input("Enter your lottery number (4 numbers and 1 letter): ")

if user_input == lottery_numbers:
    print("Congratulations! You are a winner!")
else:
    print("Sorry, you are not a winner. The lottery number was:",
           lottery_numbers)