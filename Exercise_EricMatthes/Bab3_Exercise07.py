#nambah tamu
guest = ['Kayla', 'Hani', 'Dewi']
print ("Kita akan mengundang tamu lebih banyak")

guest.insert(0, 'Rizki')

#nambah tamu kedua
guest.insert(2, 'Dian')

#nambah tamu akhir
guest.append('Rani')

#maaf, kita hanya bisa mengundang 2 orang
print("Maaf, kita hanya bisa mengundang 2 orang")

#hapus tamu
popped_guest = guest.pop()
print(f"Maaf {popped_guest}, kamu tidak bisa datang ke acara makan malam")

popped_guest = guest.pop()
print(f"Maaf {popped_guest}, kamu tidak bisa datang ke acara makan malam")

popped_guest = guest.pop()
print(f"Maaf {popped_guest}, kamu tidak bisa datang ke acara makan malam")

popped_guest = guest.pop()
print(f"Maaf {popped_guest}, kamu tidak bisa datang ke acara makan malam")

#message 2 tamu yang diundang
print(f"halo {guest[0]}, kamu diundang ke acara makan malam")
print(f"halo {guest[1]}, apakah kamu mau datang ke acara makan malam") 

del guest[0]
del guest[0]

print("daftar tamu sekarang:", guest)
