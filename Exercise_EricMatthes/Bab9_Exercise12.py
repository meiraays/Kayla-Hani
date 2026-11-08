from adminmodule import Admin

# Membuat instance dari class Admin
admin_user = Admin("Hihu", "Hohoho", "hihu_admin", "hihu@gmail.com")

# Menambahkan daftar hak akses
admin_user.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user"
]

# Memanggil method show_privileges() untuk memastikan semuanya berjalan lancar
admin_user.privileges.show_privileges()