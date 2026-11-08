# 1. Parent Class

class User: 
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nProfil User: ")
        print(f"- Nama Lengkap : {self.first_name} {self.last_name}")
        print(f"- Username     : {self.username}")
        print(f"- Email        : {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


# 2. Class Admin (Child Class yang mewarisi dari User)
class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        # Memanggil __init__() milik class User (Parent)
        super().__init__(first_name, last_name, username, email)
        
        # Atribut khusus untuk Admin (menyimpan daftar hak akses)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify user permissions"
        ]

    # Method khusus Admin untuk menampilkan hak akses
    def show_privileges(self):
        print(f"\nHak Akses (Privileges) untuk Admin '{self.username}':")
        for privilege in self.privileges:
            print(f"- {privilege}")

# 3. Uji Coba Kode

# Membuat objek/instance dari class Admin
admin_utama = Admin("Kayla", "Hani", "kayla_admin", "admin@website.com")

# Memanggil method turunan dari class User
admin_utama.describe_user()
admin_utama.greet_user()

# Memanggil method khusus dari class Admin
admin_utama.show_privileges()