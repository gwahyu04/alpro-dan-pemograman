# # Program untuk demonstrasi operator logika (Logical Operators)

# # Memasukkan dua nilai boolean dari pengguna
# nilai1 = input("Masukkan nilai pertama (True/False): ").strip().capitalize() == "True"
# nilai2 = input("Masukkan nilai kedua (True/False): ").strip().capitalize() == "True"

# # Melakukan operasi logika dan menampilkan hasil
# print(f"{nilai1} and {nilai2}: {nilai1 and nilai2}")  # Operator AND
# print(f"{nilai1} or {nilai2}: {nilai1 or nilai2}")    # Operator OR
# print(f"not {nilai1}: {not nilai1}")                  # Operator NOT
# print(f"not {nilai2}: {not nilai2}")

print('operator and')
print('semua statement benar :', (5>3) and (7>5))
print('semua statement salah :', (5<3) and (7>5))
print('------------------------------------------')


print('operator or')
print('semua statement benar :', (5<3) or (7<5))
print('semua statement salah :', (5<3) or (7>5))
print('------------------------------------------')


print('operator not')
print('semua statement benar :',not(5>3))
print('semua statement salah :',not (7<5))
print('------------------------------------------')