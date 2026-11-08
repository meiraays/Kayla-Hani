class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        # 1. login_attempts dengan nilai awal 0
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang kembali.")

    # 2. Method increment_login_attempts() untuk menambah login_attempts
    def increment_login_attempts(self):
        self.login_attempts += 1

    # 3. Method reset_login_attempts() untuk mengatur ulang login_attempts ke 0
    def reset_login_attempts(self):
        self.login_attempts = 0

# Uji Coba  

# Buat instance user
user = User("Kayla", "Hani", "kaylahani","kayla@gmail.com")

# Memanggil method increment_login_attempts() beberapa kali
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Menampilkan jumlah login_attempts
print(f"Jumlah login attempts saat ini: {user.login_attempts}")

# Reset nilai login_attempts
user.reset_login_attempts()

# Cetak nilai setelah reset
print(f"Jumlah login attempts setelah reset: {user.login_attempts}")