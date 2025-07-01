# program menemukan istilah dalam dictionary
dictionary = {
    "Python": "Bahasa pemrograman tingkat tinggi",
    "Java": "Bahasa pemrograman yang banyak digunakan",
    "JavaScript": "Bahasa pemrograman untuk pengembangan web",
}
input_kata = input("Masukkan kata yang ingin dicari: ")
if input_kata in dictionary:
    print(f"{input_kata}: {dictionary[input_kata]}")
else:
    print(f"{input_kata} tidak ditemukan dalam dictionary.")