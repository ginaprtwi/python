print(f"SALDO TABUNGAN")
print(("-") * 30)

# input
saldoAwal = int(input("Saldo Awal : Rp. "))
bunga = int(input("Bunga (%): "))
jangkaWaktu = int(input("Jangka Waktu : "))
print(("-") * 30)

# proses
saldoAkhir = saldoAwal *  (1 + bunga/100)**jangkaWaktu

# output
print(f"Saldo Akhir : Rp. {saldoAkhir}")