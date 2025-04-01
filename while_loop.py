# # Daftar antrian pelanggan
# antrian = ["Alice", "Bob", "Charlie", "David"]

# print("Memulai layanan kasir...\n")

# # Loop selama masih ada pelanggan di antrian
# while antrian:
#     pelanggan = antrian.pop(0)  # Mengambil pelanggan pertama
#     print(f"Melayani pelanggan: {pelanggan}")
    
#     # Simulasi proses pembayaran
#     input("Tekan Enter setelah pembayaran selesai...")  

# print("\nSemua pelanggan telah dilayani. Kasir ditutup.")

# Inisialisasi variabel
total_nilai = 0
jumlah_mahasiswa = 0

print("Masukkan nilai mahasiswa satu per satu.")
print("Ketik -1 jika sudah selesai.\n")

# Loop untuk menerima input nilai
while True:
    try:
        nilai = float(input("Masukkan nilai mahasiswa: "))
        
        if nilai == -1:  # Jika dosen selesai memasukkan nilai
            break
        elif nilai < 50 or nilai > 100:  # Validasi nilai harus dalam rentang 0-100
            print("Nilai harus antara 50 hingga 100.")
            continue
        
        total_nilai += nilai  # Menambahkan nilai ke total
        jumlah_mahasiswa += 1  # Menambah jumlah mahasiswa

    except ValueError:
        print("Harap masukkan angka yang valid.")

# Menghitung rata-rata jika ada nilai yang dimasukkan
if jumlah_mahasiswa > 0:
    rata_rata = total_nilai / jumlah_mahasiswa
    print(f"\nRata-rata nilai mahasiswa adalah: {rata_rata:.2f}")
else:
    print("\nTidak ada nilai yang dimasukkan.")

print("Terima kasih!")
