prompt="\nEnter 'quit' when you wish to stop:"
while True:
    besttopping=input(prompt)
    if besttopping!='quit':
        print("I will add" + besttopping + "to your pizza.")
    else:
        break