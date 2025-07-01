# # struktur dasar exception handling
# try:
#     # kode yang mungkin menyebabkan error
# except ExceptionType:
#     # kode yang dijalankan jika terjadi error
# else:
#     # kode yang dijalankan jika tidak terjadi error
# finally:
#     # kode yang selalu dijalankan, baik terjadi error atau tidak

try:
    # kode yang mungkin menyebabkan error
    x = int(input("Masukkan bilangan bulat: "))
except ValueError:
    # kode yang dijalankan jika terjadi error
    print("Input tidak valid. Silakan masukkan bilangan bulat.")
else:
    # kode yang dijalankan jika tidak terjadi error
    print("Bilangan bulat yang dimasukkan:", x)
finally:
    # kode yang selalu dijalankan, baik terjadi error atau tidak
    print("Terima kasih telah mencoba.")