guest_list = ['Ayrton Senna', 'Pele', 'David Gilmour']
print(f"Hi {guest_list[0]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[1]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[2]}, I'd like to invite you to my next dinner event.")
print(f"\n Hello {guest_list[0]}, {guest_list[1]} and {guest_list[2]}, I'd like to inform that I found a bigger table and we'll be having more guests joining us.\n")

guest_list.insert(0, 'Jerry Seinfeld')
guest_list.insert(2, 'Scooby-Doo')
guest_list.append('Shaggy')
guest_list.sort()
print(guest_list)

print(f"\nHi {guest_list[0]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[1]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[2]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[3]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[4]}, I'd like to invite you to my next dinner event.")
print(f"\nHi {guest_list[5]}, I'd like to invite you to my next dinner event.")

print("\nThe first three items in the list are:")
for guests in guest_list[:3]:
  print(guests.title())

print("\nThree items from the middle of the list are:")
for guests in guest_list[1:4]:
  print(guests.title())

print("\nThe last three items in the list are:")
for guests in guest_list[-3:]:
  print(guests.title())
