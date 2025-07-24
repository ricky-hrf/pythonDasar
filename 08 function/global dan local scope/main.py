nama = "Utomo" # variable global
def aksesNama():
  print(f"variable nama bisa diakses di dalam fungsi jika berada di global. ini hasilnya {nama}")
aksesNama()

# variable global juga bisa di akses jika dibuat sebelum pemanggilan fungsi 
def latihan():
  print(f"ini latihan global")
  print(ini)

ini = "isi untuk varible global"
latihan()

# variable lokal hanya bisa diakses di dalam fungsi
def latihan2():
  local = "ini local" # variable local
  print(local)

# merubah variable global
jumlah = 18
def ubah(nilaiBaru):
  global jumlah
  jumlah = nilaiBaru
  print(jumlah)
ubah(5)
