a = 120
b = 25
c = 5
hasil = int((a*b)/c)
print("(120", "x", "25)", "/5", "=", hasil)

#soal 2
soal2=(4*2)**2+10
print("(4 x 2)^2 + 10 = ",soal2)

#soal3
soal3a=(10 < 5)
soal3b=(3>1)
print("(10 > 5) adalah", soal3a, "dan", "(3 > 1) adalah", soal3b)

#soal 4
soal4=int((25/100) * (100 * (50+20)))
print("25 % dari 100 x (50+20)", soal4)

#soal 5
m=(9>2)
n=(10<4)
o=(30 == 15 * 2)
print(m, ",", n, ",", o)

print("\n===program menghitung luas balok===\n")
Panjang = int(input('Panjang : '))
Lebar = int(input('Lebar : '))
Tinggi = int(input('Tinggi Balik : '))
LuasBalok = int(2*((Panjang*Lebar) + (Panjang*Tinggi) * (Lebar * Tinggi)))
print(LuasBalok)
