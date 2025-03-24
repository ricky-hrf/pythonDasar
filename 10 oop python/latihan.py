class Buku:
  def __init__(self, judul, penulis, kategori):
    self.judul = judul
    self.penulis = penulis
    self.kategori = kategori
    self.status = "Tersedia"
    self.peminjam = None
    self.riwayat_peminjam = []

  def pinjam(self, nama_peminjam):
    if self.status == "Tersedia":
      self.status = "Dipinjam"
      self.peminjam = nama_peminjam
      self.riwayat_peminjam.append(nama_peminjam)
      return f"Buku '{self.judul}' berhasil dipinjam oleh {nama_peminjam}"
    else:
      return f"Buku '{self.judul}' sedang tidak tersedia!"
    
  def kembalikan(self):
    if self.status == "Dipinjam":
      peminjam_sebelumnya = self.peminjam
      self.status = "Tersedia"
      self.peminjam = None
      return f"Buku '{self.judul}' sudah tersedia!"
    
  def __str__(self):
    status_peminjam = f"(Dipinjam oleh {self.peminjam})" if self.peminjam else ""
    return f"{self.judul} oleh {self.penulis} - {self.status}{status_peminjam}"
  
class Perpustakaan:
  def __init__(self):
    self.koleksi = []
    self.pengguna_terdaftar = {}
    self.pengguna_login = None

  def daftar_pengguna(self, username, password):
    if username in self.pengguna_terdaftar:
      return f"Username '{username}' sudah digunakan."
    self.pengguna_terdaftar[username] = password
    return f"Pengguna '{username}' berhasil didaftarkan."
  
  def login(self, username, password):
    if username in self.pengguna_terdaftar and self.pengguna_terdaftar[username] == password:
      self.pengguna_login = username
      return f"Login berhasil! Selamat datang, {username}."
    return "Username atau password salah"
  
  def logout(self):
    if self.pengguna_login:
      nama = self.pengguna_login
      self.pengguna_login = None
      return f"{nama} telah logout."
    return "Tidak ada pengguna yang sedang login"
  
  def tambah_buku(self, judul, penulis, kategori):
    buku_baru = Buku(judul, penulis, kategori)
    self.koleksi.append(buku_baru)
    return f"Buku '{judul}' telah ditambahkan ke perpustakaan"
      
  def hapus_buku(self, judul):
    for buku in self.koleksi:
      if buku.judul.lower() == judul.lower():
        self.koleksi.remove(buku)
        return f"Buku '{judul}' telah dihapus dari perpustakaan"
      return f"Buku '{judul}' tidak ditemukan"
    
  def tampilkan_buku(self):
    if not self.koleksi:
      return "Tidak ada buku di perpustakaan"
    return "\n".join(str(buku) for buku in self.koleksi)
  
  def pinjam_buku(self, judul):
        if not self.pengguna_login:
            return "Silakan login terlebih dahulu untuk meminjam buku."
        for buku in self.koleksi:
            if buku.judul.lower() == judul.lower():
                return buku.pinjam(self.pengguna_login)
        return f"Buku '{judul}' tidak ditemukan."
  
  def kembalikan_buku(self, judul):
    if not self.pengguna_login:
      return "silakan login terlebih dahulu untuk mengembalikan buku!"
    for buku in self.koleksi:
      if buku.judul.lower() == judul.lower() and buku.peminjam == self.pengguna_login:
        return buku.kembalikan()
    return f"Buku '{judul}' tidak ditemukan atau bukan milik peminjam saat ini"
  
  def daftar_peminjam(self):
    peminjam_list = [buku for buku in self.koleksi if buku.peminjam is not None]
    if peminjam_list:
      return "\n".join(f"{buku.peminjam} meminjam '{buku.judul}'" for buku in peminjam_list)
    return "Tidak ada buku yang sedang dipinjam"
  
  def riwayat_peminjaman(self, judul):
    for buku in self.koleksi:
      if buku.judul.lower() == judul.lower():
        if buku.riwayat_peminjam:
          return f"Riwayat peminjam '{judul}' :  "+", ".join(buku.riwayat_peminjam)
        return f"Tidak ada riwayat peminjam untuk buku '{judul}'"
      return f"Buku '{judul}' tidak ditemukan"
    
# ======= Simulasi Penggunaan =======
perpus = Perpustakaan()

# Registrasi dan Login
print(perpus.daftar_pengguna("ali", "password123"))
print(perpus.daftar_pengguna("budi", "pass456"))

print(perpus.login("ali", "password123"))

# Menambahkan buku
print(perpus.tambah_buku("Python untuk Pemula", "John Doe", "Pemrograman"))
print(perpus.tambah_buku("Sejarah Dunia", "Michael Hart", "Sejarah"))

# Menampilkan daftar buku
print("\n Daftar Buku di Perpustakaan:")
print(perpus.tampilkan_buku())

# Meminjam buku oleh Ali
print("\n Ali Meminjam Buku:")
print(perpus.pinjam_buku("Python untuk Pemula"))

# Logout Ali, Login Budi, lalu meminjam buku
print(perpus.logout())
print(perpus.login("budi", "pass456"))

print("\n Budi Meminjam Buku:")
print(perpus.pinjam_buku("Sejarah Dunia"))

# Menampilkan daftar peminjam
print("\n Daftar Peminjam:")
print(perpus.daftar_peminjam())

# Mengembalikan buku
print("\n Budi Mengembalikan Buku:")
print(perpus.kembalikan_buku("Sejarah Dunia"))

# Menampilkan daftar peminjam setelah pengembalian
print("\n Daftar Peminjam Setelah Pengembalian:")
print(perpus.daftar_peminjam())

# Menampilkan riwayat peminjaman
print("\n Riwayat Peminjaman 'Python untuk Pemula':")
print(perpus.riwayat_peminjaman("Python untuk Pemula"))

print("\n Riwayat Peminjaman 'Sejarah Dunia':")
print(perpus.riwayat_peminjaman("Sejarah Dunia"))