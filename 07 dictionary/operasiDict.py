print("====== OPERASI DICTIONARY ======")

data_dictionary = {
  "py":"Pemrograman Python",
  "jv":"Pemrograman Java",
  "js":"Pemrograman JavaScript",
  "c++":"Pemrograman C++"
}
print(data_dictionary)
# mengetahui panjang dictionary
LENDICT = len(data_dictionary)
print(f"Panjang Dictionary: {LENDICT}")

# mengecek key ada atau tidak
KEY = input("Masukkan key yang ingin kamu cari: ")
check = KEY in data_dictionary
if check == True:
  print(f"{KEY} ada di dalam dataDictionary")
else:
  print(f"{KEY} tidak ada di dalam dataDictionary")

for value in data_dictionary.values():
  print(value)

# copy dictionary
