# buats set bracket, constructor
myset = {'s','e','t',1}
# myset2 = set{'s','e','t',2}

#unordered urutan tidak sama
print('data;',myset)
# print('data:',myset2)
# print('============')

#unduplicatable unique
# myset1 = {'s','e','t',1,1}
# myset2 = set{'s','e','t',2,2}
# print('data;',myset1)
# print('data:',myset2)
# print('============')

#unidexed tidak memiliki index
# myIndex = myset.index(1)
# print('index angka 1:',myIndex)
# print('===========')

#unchangeable tidal dapat dirubah
# myset[3] = 9
# print('hasil edit:',myset)
# print('===========')

#tambah data add
# myset.add(5)
# print('hasil eadd:',myset)
# print('===========')

#hapus data
#pop: random, remove: specific
# myset.pop()
# print('hasil pop:',myset)
# print('===========')

# hapus 's' dari myset
myset.remove('s')
print('hasil remove:',myset)
print('===========')