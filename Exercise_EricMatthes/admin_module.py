class User:
    """Class untuk memodelkan profil pengguna."""
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\nNama: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Menampilkan salam personal kepada pengguna."""
        print(f"Selamat datang kembali, {self.username}!")


class Privileges:
    """Class khusus untuk mengelola hak akses/privilese."""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak akses yang dimiliki admin."""
        print("\nHak akses Administrator:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- Pengguna ini tidak memiliki hak akses khusus.")


class Admin(User):
    """Class khusus untuk administrator, turunan dari User."""
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        # Menggunakan instance dari Privileges sebagai atribut
        self.privileges = Privileges()