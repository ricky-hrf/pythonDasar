# aplikasi kamus mini sederhana
kamus = {
    "apel": "buah berwarna merah atau hijau",
    "pisang": "buah berwarna kuning",
    "jeruk": "buah berwarna oranye"
}

while True:
    kata = input("Masukkan kata (atau 'keluar' untuk mengakhiri): ")
    if kata == "keluar":
        break
    arti = kamus.get(kata)
    if arti:
        print(f"Arti '{kata}': {arti}")
    else:
        print(f"Kata '{kata}' tidak ditemukan dalam kamus.")

# Aplikasi kamus mini inggris-indonesia sederhana
kamus_inggris_indonesia = {
    "apple": "apel",
    "banana": "pisang",
    "orange": "jeruk"
}

while True:
    kata = input("Masukkan kata dalam bahasa Inggris (atau 'keluar' untuk mengakhiri): ")
    if kata == "keluar":
        break
    arti = kamus_inggris_indonesia.get(kata)
    if arti:
        print(f"Arti '{kata}': {arti}")
    else:
        print(f"Kata '{kata}' tidak ditemukan dalam kamus.")
