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