class mobil:
  
  def __init__(self,nama,warna,jumlah):
    self.nama = nama
    self.warna = warna
    self.jumlah = jumlah

  def __repr__(self):
    return f"Mobil: {self.nama} dengan warna {self.warna} biasanya digunakan untuk debugging"

  def __str__(self):
    return f"Mobil: {self.nama} dengan warna {self.warna} biasanya digunakan untuk production"
  
  def __add__(self,objek):
    return self.jumlah + objek.jumlah


object1 = mobil("avanza","silver",2)
object2 = mobil("hrv","gray",1)
print(object1)
print(object2)
print(object1 + object2)