# aplikasi menghitung akar sebuah bilangan
print("======PROGRAM MENGHITUNG AKAR KUADRAT SEBUAH BILANGAN======")
def hitung_akar(bilangan):
    if bilangan < 0:
        raise ValueError("Bilangan tidak boleh negatif")
    return bilangan ** 0.5

bilangan = int(input("Masukkan bilangan: "))
print(f"Akar kuadrat dari {bilangan} adalah {hitung_akar(bilangan)}")

print("======PROGRAM MENGHITUNG AKAR PANGKAT N SEBUAH BILANGAN======")
def hitung_akar_pangkat_n(bilangan, n):
    if bilangan < 0 and n % 2 == 0:
        raise ValueError("Bilangan tidak boleh negatif untuk akar pangkat genap")
    return bilangan ** (1/n)

bilangan = int(input("Masukkan bilangan: "))
n = int(input("Masukkan pangkat n: "))
print(f"Akar pangkat {n} dari {bilangan} adalah {hitung_akar_pangkat_n(bilangan, n)}")

print("======PROGRAM MENGHITUNG AKAR PANGKAT 2 DENGAN PARAMETER TANPA FUNGSI RETURN======")

def hitung_akar_pangkat_2(bilangan):
    if bilangan < 0:
        raise ValueError("Bilangan tidak boleh negatif")
    akar = bilangan ** 0.5
    print(f"Akar pangkat 2 dari {bilangan} adalah {akar}")

bilangan = int(input("Masukkan bilangan: "))
hitung_akar_pangkat_2(bilangan)
