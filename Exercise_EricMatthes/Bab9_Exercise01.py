# Membuat class Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Menampilkan informasi restoran
    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print (f"Jenis masakan: {self.cuisine_type}")

    # Menampilkan informasi bahwa restoran buka
    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

# Membuat objek dari class Restaurant
restaurant = Restaurant ("Pizza Hut", "Italian")

# Menampilkan atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil kedua method
restaurant.describe_restaurant()
restaurant.open_restaurant()