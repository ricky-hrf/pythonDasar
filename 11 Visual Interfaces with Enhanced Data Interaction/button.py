import tkinter as tk
from tkinter import messagebox # import modul messagebox untuk menampilkan pesan

def tekan_tombol():
  messagebox.showinfo("pesan", "Tombol ditekan!") # menampilkan pesan saat tombol ditekan
  label_status.config(text="Status:Tombol ditekan!") # mengubah teks label status saat tombol ditekan

window = tk.Tk() # buat jendela utama/window aplikasi
window.title("PyhtonApp") # membuat judul jendela/window aplikasi
window.geometry("300x200") # mengatur ukuran jendela/window aplikasi

# button 1
tombol_1 = tk.Button(
  window,
  text="Tombol 1",
  command=tekan_tombol, # menghubungkan tombol dengan fungsi tekan_tombol
)
tombol_1.pack(pady=10) # menampilkan tombol di jendela aplikasi

# button 2
tombol_2 = tk.Button(
  window,
  text="Tombol 2",
  bg="green",
  fg="white",
  font=("Arial", 12, "bold"),
  width=15,
  height=1,
  activebackground="darkgreen",
  command=window.destroy # menutup aplikasi saat tombol ditekan
)
tombol_2.pack(pady=15) # menampilkan tombol di jendela aplikasi

# tombol 3
from PIL import Image, ImageTk # import modul PIL untuk memproses gambar

gambar = Image.open("../person.jpg").resize((20, 20)) # memuat gambar dari file
gambar_tk =ImageTk.PhotoImage(gambar) # mengonversi gambar menjadi format yang dapat digunakan tkinter

tombol_gambar = tk.Button(
  window,
  image=gambar_tk, # menggunakan gambar sebagai ikon tombol
  text="Tombol Gambar",
  compound="left", # menempatkan teks di sebelah kiri gambar
  padx=10,
)
tombol_gambar.image= gambar_tk # menyimpan referensi gambar agar tidak dihapus oleh garbage collector
tombol_gambar.pack(pady=10) # menampilkan tombol di jendela aplikasi

# Label untuk menampilkan status
label_status = tk.Label(window, text="Status: Menunggu input")
label_status.pack(pady=10)
window.mainloop() # menjalankan aplikasi tkinter