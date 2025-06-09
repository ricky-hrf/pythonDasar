#contoh penulisan tuple
tuple1 = ('fisika', 'kimia', 123, 432)
tuple2 = (1, False, 7, 4, 5, )
tuple3 = "a", "d", "f", "b"

print(tuple1[0])
print(tuple2[1])
print(tuple3[2:5])

print("========== METHOD DALAM TUPLE ==========")
# length untuk menghitung jumlah elemen dalam tuple
print("Jumlah elemen dalam tuple1:", len(tuple1))
# max untuk mencari nilai maksimum dalam tuple
print("Nilai maksimum dalam tuple2:", max(tuple2))
# min untuk mencari nilai minimum dalam tuple
print("Nilai minimum dalam tuple2:", min(tuple2))
# sorted untuk mengurutkan elemen dalam tuple
print("Tuple3 setelah diurutkan:", sorted(tuple3))
# sum untuk menjumlahkan elemen numerik dalam tuple
print("Jumlah elemen numerik dalam tuple2:", sum(tuple2))