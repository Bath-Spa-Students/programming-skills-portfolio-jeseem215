# Assign an age value (you can change this value as needed).
age = 30

# Check the age of the person and print a corresponding message based on age ranges.
if age < 2:
    # If the age is less than 2, the person is considered a baby.
    print("The person is a baby.")
elif age >= 2 and age < 4:
    # If the age is between 2 and 4 (inclusive), the person is considered a toddler.
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    # If the age is between 4 and 13 (inclusive), the person is considered a kid.
    print("The person is a kid.")
elif age >= 13 and age < 20:
    # If the age is between 13 and 20 (inclusive), the person is considered a teenager.
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    # If the age is between 20 and 65 (inclusive), the person is considered an adult.
    print("The person is an adult.")
else:
    # If none of the above conditions are met, the person is considered an elder.
    print("The person is an elder.")