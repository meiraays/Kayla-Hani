# 1. Class User (Parent Class)
class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nProfil User:")
        print(f"- Nama Lengkap : {self.first_name} {self.last_name}")
        print(f"- Username     : {self.username}")
        print(f"- Email        : {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")


# 2. Class Privileges (Terpisah untuk mengelola daftar hak akses)
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "dapat menambahkan postingan",
                "dapat menghapus postingan",
                "dapat ban user",
                "dapat edit izin user"
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nHak Akses (Privileges):")
        for privilege in self.privileges:
            print(f"- {privilege}")


# 3. Class Admin (Menggunakan Privileges sebagai atribut/komposisi)
class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        # Membuat instance Privileges sebagai atribut milik Admin
        self.privileges = Privileges()

# Uji Coba Kode

# Membuat objek Admin
admin_baru = Admin("Kayla", "Hani", "kayla_admin", "admin@website.com")

# Menampilkan informasi dasar user
admin_baru.describe_user()

# Memanggil method show_privileges() melalui self.privileges milik Admin
admin_baru.privileges.show_privileges()