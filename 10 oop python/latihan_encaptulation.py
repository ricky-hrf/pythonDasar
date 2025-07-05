class Mahasiswa:
  def __init__(self, nama, nilai):
    self.nama = nama
    self.__nilai = nilai

  def tampilkan_nilai(self):
    return self.__nilai
  def set_nilai(self, nilai_baru):
    if 0 <= nilai_baru <= 100:
      self.__nilai = nilai_baru
    else:
      print("Nilai harus antara 0 dan 100")

# Contoh penggunaan
mhs = Mahasiswa("Budi", 85)
print(mhs.tampilkan_nilai())
mhs.set_nilai(90)
print(mhs.tampilkan_nilai())
mhs.set_nilai(110)