# Program Penentuan Diskon Pembelian

# Input status keanggotaan
member = input("Apakah Anda anggota? (ya/tidak): ").strip().lower()

# Input total belanja
total_belanja = float(input("Masukkan total belanja Anda: "))

# Inisialisasi diskon
diskon = 0

# Cek status keanggotaan
if member == "ya":
    if total_belanja >= 1000000:
        diskon = 50
    elif total_belanja >= 500000:
        diskon = 20
    else:
        diskon = 5
else:
    if total_belanja >= 500000:
        diskon = 30
    elif total_belanja >= 300000:
        diskon = 10
    else:
        diskon = 0

jumlah_diskon = (diskon / 100) * total_belanja
total_bayar = total_belanja - jumlah_diskon

print(f"Diskon Anda: {diskon}%")
print(f"Total yang harus dibayar: Rp {total_bayar:.2f}")
