from random import choice

# 1. Membuat list berisi 10 angka dan 5 huruf
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 2. Memilih 4 elemen secara acak
winning_ticket = []

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    
    # Memastikan tidak ada karakter/angka yang terambil ganda
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

# 3. Menampilkan pesan pemenang
print(f"Tiket yang cocok dengan kombinasi {winning_ticket} memenangkan hadiah utama!")