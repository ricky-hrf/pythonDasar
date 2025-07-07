class Manusia:

  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def berbicara(self, target):
    print(f"{self.nama} sedang berbicara dengan {target.nama}")

class Guru(Manusia):
  def mengajar(self):
    print(f"{self.nama} sedang mengajar")

class Dokter(Manusia):
  def mengobati(self):
    print(f"{self.nama} sedang mengobati pasien")

g = Guru("Heru", 35)
g.mengajar()

d = Dokter("Siti", 40)
d.mengobati()

g.berbicara(d)