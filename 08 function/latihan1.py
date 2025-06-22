# Lesson 1: membuat Fungsi Sederhana
def menyapa():
    print("Halo, selamat datang di Python!")
    print("Ini adalah fungsi sederhana yang menyapa pengguna.")
    print("Fungsi ini dapat dipanggil berulang kali untuk menyapa pengguna.")
    print("Terima kasih telah menggunakan fungsi ini!")
    print("Apakah anda tertarik dengan fungsi di python?")
    print("====================================")

menyapa()

# Lesson 2: membuat Fungsi dengan Parameter/argumen/input
def menyapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang di Python!")
    print("Ini adalah fungsi sederhana yang menyapa pengguna dengan nama.")
    print("Fungsi ini dapat dipanggil berulang kali dengan nama yang berbeda.")
    print("Terima kasih telah menggunakan fungsi ini!")
    print("Apakah anda tertarik dengan fungsi di python?")
    print("====================================")
menyapa_nama("Budi")
menyapa_nama("Siti")
# jika nama menerima inputan dari pengguna
nama_pengguna = input("Masukkan nama Anda: ")
menyapa_nama(nama_pengguna)

def biodata(nama, umur, kota):
    print(f"Nama: {nama}")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")
    print("Terima kasih telah menggunakan fungsi ini!")
    print("====================================\n")

biodata("Budi", 25, "Jakarta")
biodata("Siti", 30, "Bandung")

# latihan jika parameter adalah list
def hewan_terfavorit(hewan):
    print("Hewan-hewan favorit Anda:")
    for h in hewan:
        print(f"- {h}")
    print("====================================\n")
hewan_favorit = ["Kucing", "Anjing", "Burung"]
hewan_terfavorit(hewan_favorit)
# latihan jika list menerima inputan dari pengguna
# cara pertama
def hewan_terfavorit_input():
    hewan = []
    while True:
        h = input("Masukkan hewan favorit (atau 'selesai' untuk mengakhiri): ").upper()
        if h == 'SELESAI':
            break
        hewan.append(h)
    print("Hewan-hewan favorit Anda:")
    for h in hewan:
        print(f"- {h}")
    print("====================================\n")
hewan_terfavorit_input()
# cara kedua
def hewan_terfavorit_input_cara_kedua():
    hewan = []
    while True:
        h = input("Masukkan hewan favorit (atau 'selesai' untuk mengakhiri): ").upper()
        if h == 'SELESAI':
            break
        hewan.append(h)
    hewan_terfavorit(hewan)
hewan_terfavorit_input_cara_kedua()
# cara ketiga
binatang = []
while True:
    hewan = input("Masukkan hewan favorit (atau 'selesai' untuk mengakhiri): ")
    if hewan.lower() == 'selesai':
        break
    binatang.append(hewan)
hewan_terfavorit(binatang)

# latihan jika parameter adalah dictionary
def biodata_dict(biodata):
    print("Biodata Anda:")
    for key, value in biodata.items():
        print(f"{key}: {value}")
    print("====================================\n")
biodata_saya = {
    "Nama": "Budi",
    "Umur": 25,
    "Kota": "Jakarta"
}
biodata_dict(biodata_saya)
# latihan jika dictionary menerima inputan dari pengguna
def biodata_dict_input():
    biodata = {}
    while True:
        key = input("Masukkan key (atau 'selesai' untuk mengakhiri): ")
        if key.lower() == 'selesai':
            break
        value = input(f"Masukkan value untuk {key}: ")
        biodata[key] = value
    biodata_dict(biodata)
biodata_dict_input()
# latihan jika dictionary di dalam dictionary
def biodata_dict_nested(biodata):
    print("Biodata Anda:")
    for key, value in biodata.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")
    print("====================================\n")
biodata_nested = {
    "Nama": "Budi",
    "Umur": 25,
    "Kota": "Jakarta",
    "Hobi": {
        "Hobi 1": "Membaca",
        "Hobi 2": "Bersepeda"
    }
}
biodata_dict_nested(biodata_nested)
