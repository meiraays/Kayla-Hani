# List username yang sudah terdaftar
current_users = ["admin", "kayla", "hani", "chikuro", "hihu"]

new_users = ["KAYLA", "budi", "HANI", "daffa", "aan"]

# Mengubah semua username lama menjadi huruf kecil
current_users_lower = [user.lower() for user in current_users]

# Mengecek username baru
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username {new_user} is already taken. Please choose another.")
    else:
        print(f"Username {new_user} is available.")