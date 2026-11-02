def make_sandwich(*items):
    print("\nMaking a sandwich with:")

    for item in items:
        print(f"- {item}")

    print("Your sandwich is ready!")


make_sandwich("cheese")

make_sandwich("chicken", "lettuce")

make_sandwich("beef", "tomato", "cheese")