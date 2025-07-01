def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    return umur

try:
    age = int(input("Masukkan umur Anda: "))
    print(cek_umur(age))
except ValueError as error:
    print(f"Error: {error}")