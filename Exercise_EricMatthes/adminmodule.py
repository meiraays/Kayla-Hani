from user_module import User

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
        self.privileges = Privileges()