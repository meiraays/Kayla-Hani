# Membuat class Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # Menampilkan informasi restoran
    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    # Menampilkan informasi bahwa restoran buka
    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka!")

# Membuat tiga objek restoran
restaurant1 = Restaurant("Marugame Udon", "Japanese")
restaurant2 = Restaurant("Pizza Hut", "Italian")
restaurant3 = Restaurant("Kharisma Bahari", "Indonesian")

# Menampilkan informasi masing-masing restoran
restaurant1.describe_restaurant()
print()

restaurant2.describe_restaurant()
print()

restaurant3.describe_restaurant()