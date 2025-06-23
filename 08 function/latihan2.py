biodata = {}
def fungsi_biodata(data):
    while True:
        key = input("Masukkan key (ketik 1 untuk berhenti): ")
        if key == "1":
            break
        type_value = input(f"Apakah value untuk {key} bertipe dictionary (yes/no)?: ").lower()
        if type_value == "yes":
            value={}
            while True:
                key2 = input("Masukkan key (ketik 3 untuk berhenti): ")
                if key2 == "3":
                    break
                value2 = input(f"Masukkan value untuk key {key2} : ")
                value[key2] = value2
        elif type_value == "no":
            value = input(f"Masukkan value untuk {key}")
        else:
            print("Jawab yes/no saja!!")
        data[key]=value
    return data

while True:
    print(f"Pilih Menu")
    print(f"1. Tambah data")
    print(f"2. Tampilkan data")
    print(f"3. keluar dari aplikasi")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        fungsi_biodata(biodata)
    elif pilihan == "2":
        for key, value in biodata.items():
            print(f"{key} adalah {value}")
        break
    elif pilihan == "3":
        break
    else:
        print("pilihan tidak valid\n")