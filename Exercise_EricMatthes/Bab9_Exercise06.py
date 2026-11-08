class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang buka!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Es krim"):
        # Memanggil __init__ () dari parent class (Restaurant)
        super().__init__(restaurant_name, cuisine_type)
        # Atribut khusus untuk menyimpan daftar rasa es krim
        self.flavors = []

    # Method untuk menampilkan daftar rasa
    def show_flavors(self):
        print(f"\nRasa es krim yang tersedia di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Uji Coba

# 1. Buat instance dari IceCreamStand
my_ice_cream_stand = IceCreamStand("Tianlala")

# 2. Tambahkan rasa eskrim
my_ice_cream_stand.flavors = ["Cokelat", "Vanilla", "Mangga", "Matcha"]

# 3. Panggil method parent class
my_ice_cream_stand.describe_restaurant()

# 4. Panggil method IceCreamSTand
my_ice_cream_stand.show_flavors()