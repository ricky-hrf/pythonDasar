print("========== APLIKASI MEMINTA INPUTAN DARI USER KE DALAM LIST ==========")
data = []
while True:
    input_data = input("Masukkan data (tekan enter untuk berhenti): ")
    if input_data == "":
        break
    data.append(input_data)
print("Data yang dimasukkan:")
for item in data:
    print("-", item)


print("========== MENGHITUNG TOTAL DATA DALAM LIST ==========")
himpunan = [7, 23, 5, 8]
count = len(himpunan)
print("Jumlah Eleman dalam list:", count)

print("========== MENGHITUNG ELEMEN TERTENTU DENGAN COUNT DALAM LIST ==========")

list = [1, 2, 2, 3, 4, 6]
count = list.count(5)
print("Jumlah elemen 2 dalam list: ", count)