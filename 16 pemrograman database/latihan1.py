import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Membuat tabel barang jika belum ada
cursor.execute( "CREATE TABLE IF NOT EXISTS barang (id INTEGER PRIMARY KEY, nama TEXT, harga REAL) ")

while True:
    print("===== MENU =====")
    print("1. Tambah Barang")
    print("2. Update Barang")
    print("3. Hapus Barang")
    print("4. Tampilkan Barang")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        nama = input("Masukkan nama barang: ")
        harga = float(input("Masukkan harga barang: "))
        cursor.execute("INSERT INTO barang (nama, harga) VALUES (?, ?)", (nama, harga))
        conn.commit()

    elif pilihan == "2":
        id_barang = input("Masukkan ID barang yang ingin diupdate: ")
        nama = input("Masukkan nama barang baru: ")
        harga = float(input("Masukkan harga barang baru: "))
        cursor.execute("UPDATE barang SET nama = ?, harga = ? WHERE id = ?", (nama, harga, id_barang))
        conn.commit()
        print("Barang berhasil diupdate.")

    elif pilihan == "3":
        id_barang = input("Masukkan ID barang yang ingin dihapus: ")
        cursor.execute("DELETE FROM barang WHERE id = ?", (id_barang,))
        conn.commit()
        print("Barang berhasil dihapus.")

    elif pilihan == "4":
        cursor.execute("SELECT * FROM barang")
        rows = cursor.fetchall()
        if rows:
            print("Daftar Barang:")
            for row in rows:
                print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}")
        else:
            print("Tidak ada barang yang tersedia.")
            
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# membuat tabel transaksi jika belum ada
cursor.execute("CREATE TABLE IF NOT EXISTS transaksi (id INTEGER PRIMARY KEY, barang_id INTEGER, jumlah INTEGER, total_harga REAL, FOREIGN KEY (barang_id) REFERENCES barang(id))")
# Menambahkan transaksi
while True:
    print("===== MENU TRANSAKSI =====")
    print("1. Tambah Transaksi")
    print("2. Tampilkan Transaksi")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        id_barang = input("Masukkan ID barang: ")
        jumlah = int(input("Masukkan jumlah: "))
        cursor.execute("SELECT harga FROM barang WHERE id = ?", (id_barang,))
        row = cursor.fetchone()
        if row:
            total_harga = row[0] * jumlah
            cursor.execute("INSERT INTO transaksi (barang_id, jumlah, total_harga) VALUES (?, ?, ?)", (id_barang, jumlah, total_harga))
            conn.commit()
            print("Transaksi berhasil ditambahkan.")
        else:
            print("Barang tidak ditemukan.")

    elif pilihan == "2":
        cursor.execute("SELECT * FROM transaksi")
        rows = cursor.fetchall()
        if rows:
            print("Daftar Transaksi:")
            for row in rows:
                print(f"ID: {row[0]}, Barang ID: {row[1]}, Jumlah: {row[2]}, Total Harga: {row[3]}")
        else:
            print("Tidak ada transaksi yang tersedia.")

    elif pilihan == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    # menambah tabel laporan jika belum ada
cursor.execute("CREATE TABLE IF NOT EXISTS laporan (id INTEGER PRIMARY KEY, transaksi_id INTEGER, total_penjualan REAL, FOREIGN KEY (transaksi_id) REFERENCES transaksi(id))")
# Menambahkan laporan
cursor.execute("SELECT SUM(total_harga) FROM transaksi")
total_penjualan = cursor.fetchone()[0] or 0.0
cursor.execute("INSERT INTO laporan (transaksi_id, total_penjualan) VALUES (?, ?)", (1, total_penjualan))
conn.commit()
# Menampilkan laporan
cursor.execute("SELECT * FROM laporan")
rows = cursor.fetchall()
if rows:
    print("Daftar Laporan:")
    for row in rows:
        print(f"ID: {row[0]}, Transaksi ID: {row[1]}, Total Penjualan: {row[2]}")
else:
    print("Tidak ada laporan yang tersedia.")

# Menampilkan pesan keluar
print("Terima kasih telah menggunakan program ini!")

# Menutup koneksi
cursor.close()
conn.close()
print("Koneksi ke database ditutup.")