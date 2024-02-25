rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'mississippi River': 'USA'
}

# A sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

print("\n")

# The name of each river
print("Rivers:")
for river in rivers:
    print(river.title())

print("\n")

# The name of each country
print("Countries:")
for country in rivers.values():
    print(country)
