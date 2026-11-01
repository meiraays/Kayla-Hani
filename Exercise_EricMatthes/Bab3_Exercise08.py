#list places in the world
list_places = ['Edinburgh', 'Norway', 'Australia', 'Germany', 'Japan']
print("original list:")
print(list_places)

#urutan asli
print("\nUrutan alfabetis (menggunakan sorted()):")
print(sorted(list_places))

#urutan sorted tapi alfabetis tanpa mengubah list asli
print("\nUrutan asli setelah sorted():")
print(list_places)

#pakai sorted tapi urutan terbalik tanpa mengubah list asli
print("\nUrutan terbalik (menggunakan sorted(reverse=True)):")
print(sorted(list_places, reverse=True))

#list menunjukkan bahwa masih dalam urutan asli
print("\nUrutan asli sekali lagi:")
print(list_places)

#menggunakan reverse() untuk mengembalikan urutan list asli
list_places.reverse()
print("\nUrutan asli setelah reverse():")
print(list_places)

#menggunakan sort() agar list tersimpan dalam urutan alfabetis
list_places.sort()
print("\nUrutan alfabetis setelah sort():")
print(list_places)

#menggunakan sort() dengan reverse=True agar list tersimpan dalam urutan terbalik
list_places.sort(reverse=True)
print("\nUrutan terbalik setelah sort(reverse=True):")
print(list_places)