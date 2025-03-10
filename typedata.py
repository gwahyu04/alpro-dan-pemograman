
mahasiswa = {
    "nama": "gus wahyu",
    "nim": 1264984672,  # Integer
    "ipk": 3.75,  # Float
    "mata_kuliah": ["Algoritma", "Struktur Data", "Basis Data"],  # List
    "temp1": ('a','b','c'), #Tuple
    "temp2": {'a','b','c'}, #Set
    "temp3": {'data': 'dt'} #Dictionary
}

# Menampilkan data mahasiswa
print("Data Mahasiswa:")
print(f"Nama         : {mahasiswa['nama']} ({type(mahasiswa['nama'])})")
print(f"NIM          : {mahasiswa['nim']} ({type(mahasiswa['nim'])})")
print(f"IPK          : {mahasiswa['ipk']} ({type(mahasiswa['ipk'])})")
print(f"temp1        : {mahasiswa['temp1']} ({type(mahasiswa['temp1'])})")
print(f"temp2        : {mahasiswa['temp2']} ({type(mahasiswa['temp2'])})")
print(f"temp3        : {mahasiswa['temp3']} ({type(mahasiswa['temp3'])})")

# Menampilkan jumlah mata kuliah yang diambil
print(f"\nJumlah mata kuliah yang diambil: {len(mahasiswa['mata_kuliah'])}")

