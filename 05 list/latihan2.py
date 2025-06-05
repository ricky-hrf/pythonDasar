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