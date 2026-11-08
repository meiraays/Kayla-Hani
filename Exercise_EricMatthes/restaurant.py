class Restaurant:
    """Class untuk memodelkan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan informasi restoran."""
        print(f"{self.restaurant_name} menyajikan makanan khas {self.cuisine_type}.")

    def open_restaurant(self):
        """Menampilkan pesan restoran sedang buka."""
        print(f"{self.restaurant_name} sekarang sedang buka!")