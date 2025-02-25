print("RINCIAN UANG KEMBALIAN")
print(("-") * 30)

# input
totalBayar = int(input("Total yang harus dibayar : Rp. "))
besarBayar = int(input("Besar bayar: Rp.  "))

print(("-") * 30)

# perhitungan
kembalian = besarBayar - totalBayar
print(f"Kembalian : Rp. {kembalian}")

# rincian kembalian
print(f"Rincian kembalian: ")
limaPuluh = kembalian // 50000
kembalian %= 50000
print(f"Rp. 50.000 : {limaPuluh} lembar")

duaPuluh = kembalian // 20000
kembalian %= 20000
print(f"Rp. 20.000 : {duaPuluh} lembar")

sepuluh = kembalian // 10000
kembalian %= 10000
print(f"Rp. 10.000 : {sepuluh} lembar")

lima = kembalian // 5000
kembalian %= 5000
print(f"Rp. 5.000 : {lima} lembar")

dua = kembalian // 2000
kembalian %= 2000
print(f"Rp. 2.000 : {dua} lembar")

satu = kembalian // 1000
kembalian %= 1000
print(f"Rp. 1.000 : {satu} lembar")










