def hitung_tarif_parkir (kendaraan, jam_masuk, jam_keluar):
    #hitung durasi parkir dalam jam
    durasi = jam_keluar - jam_masuk
   
if Kendaraan == 1:
    jam_parkir = jam_keluar - jam_masuk
    tarif_per_jam = 3000 * jam_parkir
    tarif_maks = 24000
    if tarif_per_jam > tarif_maks:
        tarif = tarif_maks
    else:
        tarif = tarif_per_jam
    print ("Tarif Parkir Mobil: Rp.", tarif)

if Kendaraan == 2:
    jam_parkir = jam_keluar - jam_masuk
    tarif_per_jam = 1500 * jam_parkir
    tarif_maks = 12000
    if tarif_per_jam > tarif_maks:
        tarif = tarif_maks
    else:
        tarif = tarif_per_jam
    print ("Tarif Parkir Motor: Rp.", tarif)

else:
    return None