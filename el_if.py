
nilai = int(input("Masukkan nilai akhir mahasiswa : "))


if nilai < 0 or nilai > 100:
    print("Error: Nilai tidak valid. Harap masukkan angka antara 0 dan 100.")
elif nilai >= 85:
    print("peringkat: A")
elif nilai >= 75:
    print("peringkat: B")
elif nilai >= 65:
    print("peringkat: C")
elif nilai >= 50:
    print("peringkat: D")
else:
    print("peringkat: E (Tidak Lulus)")
