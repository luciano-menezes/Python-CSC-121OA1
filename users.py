class User:
    def __init__(self, first_name, last_name, age, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Information:")
        print(f"First Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! You are all set.")

# Creating instances of User
user1 = User('felicia', 'castro', 47, 'feli@example.com')
user2 = User('arli', 'sobrinho', 30, 'arli@example.com')
user3 = User('uira', 'menezes', 28, 'uira@example.com')

# Calling methods for each user
user1.describe_user()
user1.greet_user()
print("\n")

user2.describe_user()
user2.greet_user()
print("\n")

user3.describe_user()
user3.greet_user()
