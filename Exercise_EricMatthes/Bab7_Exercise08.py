sandwich_orders = ["tuna", "chicken", "beef", "cheese"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")

for finished_sandwich in finished_sandwiches:

    print(f"- {finished_sandwich.title()} sandwich")