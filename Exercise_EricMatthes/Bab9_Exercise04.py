class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Menambah number_served default 0
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    # Method mengubah nilai number_served
    def set_number_served(self, number):
        self.number_served = number

    # Method untuk menambahkan jumlah pelanggan yang dilayani
    def increment_number_served(self, additional_number):
        self.number_served += additional_number

# Uji Coba

# 1. Buat restaurant
restaurant = Restaurant("Sederhana", "Padang")

# Cetak nilai awal
print (f"Jumlah pelanggan dilayani (awal): {restaurant.number_served}")

# Ubah nilai langsung dan cetak
restaurant.number_served = 15
print(f"Jumlah pelanggan dilayani: {restaurant.number_served}")

# 2. Menggunakan method set_number_served()
restaurant.set_number_served(30)
print(f"Jumlah pelanggan dilayani: {restaurant.number_served}")

# 3. Menggunalan method increment_number_served()
restaurant.increment_number_served(20)
print(f"Jumlah pelanggan dilayani: {restaurant.number_served}")