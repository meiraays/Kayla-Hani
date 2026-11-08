# Membuat class User
class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    # Menampilkan ringkasan informasi pengguna
    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Email: {self.email}")
        print(f"Kota: {self.city}")

    # Memberikan sapaan personal kepada pengguna
    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

# Membuat beberapa objek pengguna
user1 = User("Hihu", "Hehehe", 15, "hihu@gmail.com", "Bandung")
user2 = User("Kayla", "Hani", 18, "kayla@gmail.com", "Yogyakarta")
user3 = User("Solti", "Chikuro", 21, "solti@gmail.com", "Jakarta")

# Menampilkan informasi dan sapaan setiap pengguna
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()