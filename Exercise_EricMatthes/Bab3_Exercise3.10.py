kota = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]

#menampilkan list awal
print(kota)

#menambahkan kota di akhir
kota.append("Bali")
print(kota)

#menambahkan kota di posisi pertama
kota.insert(0, "Semarang")
print(kota) 

#menghapus kota berdasarkan nama
kota.remove("Bandung")
print(kota)

#menghapus kota terakhir
kota.pop()
print(kota)

#menghapus kota berdasarkan index
del kota[1]     
print(kota)

#mengurutkan sementara
print(sorted(kota)) 

#mengurutkan secara permanen
kota.sort()
print(kota) 

#membalik  urutan list
kota.reverse()
print(kota)

#menghitung jumlah kota dalam list
print(len(kota))
