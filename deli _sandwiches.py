# List of sandwich orders
sandwich_orders = ["BLT", "Philly Cheese Stake", "Ham and Cheese", 
                   "Shrimp Po Boy", "Grilled Cheese"]

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    # First sandwich order
    current_sandwich = sandwich_orders.pop(0)  
    print(f"I made your {current_sandwich} sandwich.")
    # Add the finished sandwich to the list
    finished_sandwiches.append(current_sandwich)  

# Finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)