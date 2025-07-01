# program menentukan kategori umur
umur = int(input("Masukkan umur Anda: "))
if umur < 0:
    print("Umur tidak boleh negatif.")
elif umur < 5:
    print("Anda termasuk kategori balita.")
elif umur < 13:
    print("Anda termasuk kategori anak-anak.")
elif umur < 18:
    print("Anda termasuk kategori remaja.")
else:
    print("Anda termasuk kategori dewasa.")