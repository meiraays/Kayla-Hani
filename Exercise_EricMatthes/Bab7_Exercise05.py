while True:
    age = input ("\nENter your age (or 'quit' to stop): ")

    if age.lower() == "quit":
        break

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")