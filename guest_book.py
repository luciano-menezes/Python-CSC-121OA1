from pathlib import Path

path = Path("guest_book.txt")

# Loop until the user enters 'quit'
while True:
    name = input("Please enter your name (enter 'quit' to exit): ")
    if name.lower() == 'quit':
        break
    print("Hello, " + name + "! Welcome!")
    
    # Read existing content if file exists
    if path.is_file():
        content = path.read_text()
    else:
        content = ""
    
    # Append the user's name to the content
    content += name + '\n'
    
    # Write the updated content back to the file
    path.write_text(content)