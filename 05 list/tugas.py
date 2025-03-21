# print("=====PROGRAM MENAMPILKAN DATA SUATU LIST MELALUI INPUTAN USER=====")
# inputan_list = []
# print("masukkan elemen (ketik done untuk selesai):")
# while True:
#   elemen = input("-")
#   if elemen.lower() =="done":
#     break
#   inputan_list.append(elemen)
# print("List yang anda masukan ", inputan_list)

# print("MENENTUKAN NILAI TERBESAR DAN TERKECIL DI ANTARA LIST")
# bilangan = [6,3, 22, 7, 8]
# maximal = max(bilangan)
# minimal = min(bilangan)
# print("nilai maximal dari list [6,3, 22, 7, 8] adalah ", maximal)
# print("nilai minimal dari list [6,3, 22, 7, 8] adalah ", minimal)

print("MENGHITUNG BERAPA KALI KEMUNCULAN SUATU ANGKA DALAM LIST")
bil = input("masukkan bilangan pisahkan dengan spasi : ")
list_bilangan = [int(x) for x in bil.split()]

#membuat inputan untuk target angka
target = int(input("Angka berapa yang ingin dihitung? : "))

#hitung kemunculan
kemunculan = list_bilangan.count(target)

print(f"Angka {target} muncul sebanyak {kemunculan} kali.")
