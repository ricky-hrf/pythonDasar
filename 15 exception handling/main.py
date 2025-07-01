# contoh 1
# keep_asking = True
# while keep_asking:
#   try:
#     x = int(input("Masukkan bilangan bulat: "))
#   except ValueError:
#     print("Input tidak valid. Silakan masukkan bilangan bulat.")
#   else:
#     print("Bilangan bulat yang dimasukkan:", x)
#     break

# contoh 2
# keep_asking = True
# while keep_asking:
#   try:
#     x = int(input("Masukkan bilangan bulat: "))
#   finally:
#     print("Terima kasih telah mencoba.")

# contoh penggunaan IOError
try:
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
except IOError:
    print("Error: Gagal membuka file.")
# contoh penggunaan ZeroDivisionError
try:
    result = 10 / 0  # Akan menyebabkan ZeroDivisionError
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan!")
