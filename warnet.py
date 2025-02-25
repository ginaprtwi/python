print(f"WARNET 31")
print(("-") * 30)

# input
jamMasuk = int(input("Jam masuk : "))
menitMasuk = int(input("Menit masuk : "))
jamKeluar = int(input("Jam keluar : "))
menitKeluar = int(input("Menit Keluar: "))

print(("-") * 30)

# proses
totalMasuk = (jamMasuk * 60) + menitMasuk
totalKeluar = (jamKeluar * 60) + menitKeluar

lamaRental = totalKeluar - totalMasuk
jam = lamaRental // 60
menit = lamaRental %  60
biayaRental = (lamaRental / 60) * 5000

# output
print(f"Lama Rental: {lamaRental} menit ({jam} jam {menit} menit)")
print(f"Biaya rental: Rp. {biayaRental}")