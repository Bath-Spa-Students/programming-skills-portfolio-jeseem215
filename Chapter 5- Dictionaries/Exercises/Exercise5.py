# Create a list of dictionaries representing different pets
my_pets = [
    {"kind": "Dog", "owner": "tate"},
    {"kind": "Cat", "owner": "garfield"},
    {"kind": "Parrot", "owner": "Antony"},
    {"kind": "Fish", "owner": "bellingham"},
]

# Loop through the list and print information about each pet
for pet in my_pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}\n")