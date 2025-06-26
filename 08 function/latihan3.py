data_negara = []
def insert_data(data):
    while True:
        confirm = input("Tambah Data ke List:\n1. Tambah data type string\n2. Tambah data type int\n3. Back\npilihan anda: ").upper()
        if confirm == "3":
            print("bye bye ....")
            break
        if confirm == "1":
            value = input("\nMasukkan data dengan tipe string: ").upper()
            data.append(value)
            print(f"\nBerhasil menambah {value} ke dalam list")
            print(f"Makasih ya..\n")
        elif confirm == "2":
            value = input("Masukkan data number: ").upper()
            if value.isdigit():
                value_baru = int(value)
                data.append(value_baru)
                print(f"Berhasil menambah {value_baru} ke dalam list\n")
                print(f"Makasih ya..\n")
            else:
                print(f"\nhanya boleh input NUMBER ketua!!\n{value} bukan number\n")  
        else:
            print(f"\npilihan (1,2,3).\nAda-ada aja kau tulis {confirm}!!!\nSilahkan coba lagi!!!\n")
            
def tampil_data(data):
    for i in data:
        print(f"-{i}", end=" ")
        
while True:
    cek = input("\nPilihan:\n1. Tambah Data\n2. Tampilkan Data\n3. Stop Program\nPilihan Anda: ")
    if cek == "1":
        insert_data(data_negara)
    elif cek == "2":
        tampil_data(data_negara)
    else:
        print("pilihan tidak valid")
    if cek == "3":
        break