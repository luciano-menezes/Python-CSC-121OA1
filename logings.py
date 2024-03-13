class User:
    def __init__(self, first_name, last_name, age, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0  # Adding login_attempts attribute

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

# Instance of User
user = User('felicia', 'castro', 47, 'feli@example.com')

# Calling increment_login_attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts to ensure proper incrementing
print(f"Login Attempts: {user.login_attempts}")

# Calling reset_login_attempts
user.reset_login_attempts()

# Print login_attempts to ensure it was reset to 0
print(f"After resetting, Login Attempts: {user.login_attempts}")