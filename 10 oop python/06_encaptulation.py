# # encapsulation
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.__speed = 0  # private attribute

#     def accelerate(self, amount):
#         self.__speed += amount
#         print(f"Accelerating: {self.__speed} km/h")

#     def brake(self, amount):
#         self.__speed -= amount
#         if self.__speed < 0:
#             self.__speed = 0
#         print(f"Braking: {self.__speed} km/h")

#     def get_speed(self):
#         return self.__speed

# # Example usage
# my_car = Car("Toyota", "Corolla", 2020)
# my_car.accelerate(50)
# my_car.brake(20)

# class murid:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur
#         self.__nilai = 0  # private attribute

#     def set_nilai(self, nilai):
#         if 0 <= nilai <= 100:
#             self.__nilai = nilai
#         else:
#             print("Nilai harus antara 0 dan 100")

#     def get_nilai(self):
#         return self.__nilai
# # Example usage
# m1 = murid("Budi", 20)
# m1.set_nilai(85)
# print(m1.get_nilai())

# contoh 3:
class Bank:
    def __init__(self,namaPengguna,nomorRekening,saldoPengguna,admin):
        self.namaPengguna = namaPengguna
        self.__nomorRekening = nomorRekening
        self.__saldoPengguna = saldoPengguna
        self.__admin = admin
    
    def getNomorRekening(self):
        return self.__nomorRekening
    
    def getSaldoPengguna(self):
        return self.__saldoPengguna
    
    def setorUang(self):
        setoran = int(input("setor uang: "))
        self.__saldoPengguna += setoran
        return self.__saldoPengguna,setoran
    
    def tarikUang(self):
        JumlahTarik = int(input("Masukkan jumlah tarik: "))
        self.__saldoPengguna -= JumlahTarik
        return JumlahTarik, self.__saldoPengguna
    
class BankBCA(Bank):
    def __init__(self, namaPengguna, nomorRekening, saldoPengguna, cicilan, admin):
        super().__init__(namaPengguna, nomorRekening, saldoPengguna,cicilan,5000)
        self.cicilan = cicilan

    def showInfo(self):
        print(f"Nama : {self.namaPengguna}")
        print(f"Norek: {self.getNomorRekening()}")
        print(f"Saldo: {self.getSaldoPengguna()}")
        print(f"Cicilan : {self.cicilan}")
class BankBRI(Bank):
    def __init__(self, namaPengguna, nomorRekening, saldoPengguna, pinjaman,admin):
        super().__init__(namaPengguna, nomorRekening, saldoPengguna, 5000)
        self.pinjaman = pinjaman

nasabah1 = BankBCA("Budi", 12345,100000,10000)
nasabah2 = BankBRI("Wati", 54321,150000,80000)
while True:
    pilihan = input("\npilihan:\n1. ShowInfo\n2. SetorTunai\n3. Exit\nPilihan Anda: ").lower()
    if pilihan == "3":
        break
    elif pilihan == "2":
        saldo,setoran = nasabah1.setorUang()
        print(f"Setor Uang Rp {setoran} berhasil")
    elif pilihan == "1":
        nasabah1.showInfo()
    else:
        print("Pilihan Tidak Valid...!!!")
