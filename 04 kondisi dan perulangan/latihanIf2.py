# print("=========Latihan Login Sederhana==========")
# username = input("Masukkan Username: ")
# password = input("Masukkan Password: ")

# if username == "admin" and password =="123":
#   print("======oi========")
#   print("Login Berhasil boss")
# else:
#   print("======oi========")
#   print("Username/password salah")

# print("=========Mengecek Apakah bisa dibuat segitiga==========")
# a = int(input("Masukkan panjang 1: "))
# b = int(input("Masukkan panjang 2: "))
# c = int(input("Masukkan panjang 3: "))

# if a+b > c and b+c > a and a+c > b:
#   print("Segitiga valid")
# else:
#   print("Segitiga tidak valid")

print("==========APLIKASI KASIR==========")
beras = int(input("Masukkan Harga beras: "))
telur = int(input("Masukkan Harga telur: "))
minyak = int(input("Masukkan Harga minyak: "))
labubu = int(input("Masukkan Harga labubu: "))
totalBelanja = beras + telur + minyak + labubu
if(totalBelanja >= 10000):
  diskon = totalBelanja * (15/100)
elif (totalBelanja >= 50):
  diskon = totalBelanja * (5/100)
else:
  diskon = 0
  
totalBayar = totalBelanja-diskon
print("Total belanja Anda:", totalBelanja)
print("Diskon :", int(diskon))
print("Total Bayar", int(totalBayar))