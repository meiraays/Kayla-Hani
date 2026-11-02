sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami", 
    "cheese"
]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()} sandwich")