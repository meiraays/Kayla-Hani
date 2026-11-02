# List makanan favorit saya
my_foods = ["Noodle", "Burger", "Chicken"]

# Menyalin list makanan untuk teman
friend_foods = my_foods[:]

# Menambahkan makanan favorit teman
friend_foods.append("Steak")

# Menampilkan makanan favorit saya
print("My favorite foods are:")
for food in my_foods:
    print(food)

# Menampilkan makanan favorit teman
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)