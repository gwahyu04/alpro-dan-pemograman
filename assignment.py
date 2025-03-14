
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

total_nilai = 0

for i in range(1, jumlah_siswa + 1):
    nilai = float(input(f"Masukkan nilai tugas siswa ke-{i}: "))
    total_nilai += nilai
    
    if nilai >= 80:
        print("Lulus dengan Baik")
    elif nilai >= 60:
        print("Lulus")
    else:
        print("Tidak Lulus")

rata_rata = total_nilai / jumlah_siswa
print(f"Rata-rata nilai tugas: {rata_rata:.2f}")
