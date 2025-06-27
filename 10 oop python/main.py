# class dan object
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        return f"Mobil {self.merk} berwarna {self.warna}"
    
#membuat object dari class
Mobil1 = Mobil("TOYOTA", "Merah")
Mobil2 = Mobil("HONDA", "Gray")

# mengakses atribute dan method
print(Mobil1.info())
print(Mobil2.info())

# encapsulation (enkapsulasi)
class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, jumlah):
        if jumlah < 0:
            print("Saldo tidak boleh negatif!")
        else:
            self.__saldo = jumlah

# Contoh
akun = AkunBank("Budi", 100000)
print(akun.get_saldo())
akun.set_saldo(200000)
print(akun.get_saldo())

# inheritance (pewarisan)
print("========INHERITANCE=============")
class Kendaraan: #parent class
    def __init__(self, jenis):
        self.jenis = jenis

    def info_kendaraan(self):
        return f"Jenis: {self.jenis}"
    
class Mobil(Kendaraan): # class child(anak)
    def __init__(self, jenis, merek):
        super().__init__(jenis) 
        self.merek =merek

    def info_mobil(self):
        return f"{self.info_kendaraan()}, Merek: {self.merek}"
        
mobil1 = Mobil ("Sedan", "TOYOTA")
print(mobil1.info_mobil())

# polymorphism (polimorfisme)
print("========POLYMORPHISM=============")
class Kucing:
    def suara(self):
        return "Moew"
    
class Anjing:
    def suara(self):
        return "Woof!!"

# fungsi polymorphism
def cetak_suara(hewan):
    print(hewan.suara())

kucing = Kucing()
anjing = Anjing()

cetak_suara(kucing)
cetak_suara(anjing)

# abstraction 
# menyembunyikan kompleksitas dan menampilkan fitur esensial
print("============ABSTRAKSI==============")
from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2
    
persegi = Persegi(5)
print(persegi.luas())