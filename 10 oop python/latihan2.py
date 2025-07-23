# latihan oop menghitung biaya sewa kendaraan
class Kendaraan:
    def __init__(self, jenis, harga_sewa):
        self.jenis = jenis
        self.harga_sewa = harga_sewa

    def hitung_biaya(self, jumlah_hari):
        return self.harga_sewa * jumlah_hari

# Membuat objek Kendaraan
motor = Kendaraan("Motor", 50000)
print(motor.__dict__)