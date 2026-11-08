from admin_module import Admin
admin_user = Admin("Hihu", "Titut", "hihu_admin", "hihu@gmail.com")

admin_user.privileges.privileges = [
    "menambah postingan",
    "menghapus postingan",
    "ban pengguna"
]

admin_user.privileges.show_privileges()