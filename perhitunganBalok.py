print("PERHITUNGAN BALOK")
print(("-") * 30)
# input
panjang = int(input("Panjang : "))
lebar = int(input("Lebar : "))
tinggi = int(input("Tinggi : "))

print(("-") * 30)

# proses
luasSelimut = (2 * panjang * lebar) + (2 * lebar * tinggi) + (2 * panjang * tinggi)
volume = panjang * lebar * tinggi

#output
print(f"Luas selimut balok : {luasSelimut}")
print(f"Volume Balok : {volume}")
print(f"Dimensi Balok : {panjang} x {lebar} x {tinggi}")