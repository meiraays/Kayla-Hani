# List pizza
pizzas = ["Pepperoni", "Cheese", "Tuna"]

# Menyalin list pizza untuk teman
friend_pizzas = pizzas[:]

# Menambahkan pizza favorit saya
pizzas.append("Beef")

# Menambahkan pizza favorit teman
friend_pizzas.append("Chicken")

# Menampilkan pizza favorit saya
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Menampilkan pizza favorit teman
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)