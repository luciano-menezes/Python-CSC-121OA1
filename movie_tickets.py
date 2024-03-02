prompt = "\nEnter your age (or 'exit' to quit): "
active = True
while active:
    age_input = input(prompt)
    
    if age_input == 'exit':
        print("Goodbye!")
        active = False
    else:
        age = int(age_input)
        
        if age < 3:
            print("Your ticket is free.")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")