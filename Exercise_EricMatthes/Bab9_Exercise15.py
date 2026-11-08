from random import choice

def generate_ticket(possibilities):
    """Menghasilkan kombinasi tiket acak berupa 4 karakter/angka."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


def check_ticket(my_ticket, winning_ticket):
    """Memeriksa apakah tiket pemain sama dengan tiket pemenang."""
    for element in my_ticket:
        if element not in winning_ticket:
            return False
    return True


# List berisi 10 angka dan 5 huruf
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Tiket pilihan kamu
my_ticket = [3, 7, 'A', 'E']

winning_ticket = []
plays = 0
won = False

# Perulangan sampai tiket kamu menang
while not won:
    winning_ticket = generate_ticket(possibilities)
    plays += 1
    won = check_ticket(my_ticket, winning_ticket)

# Menampilkan hasil
print(f"Tiket kamu: {my_ticket}")
print(f"Tiket pemenang: {winning_ticket}")
print(f"Dibutuhkan {plays:,} kali percobaan perulangan untuk menang!")