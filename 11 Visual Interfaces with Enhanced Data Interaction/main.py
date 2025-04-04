import tkinter as tk # import modul tkinter untuk GUI
from PIL import Image, ImageTk # import modul PIL untuk memproses gambar

zandela = tk.Tk() # buat jendela utama/window aplikasi
zandela.title("PyhtonApp") # membuat judul jendela/window aplikasi
zandela.geometry("400x300") # mengatur ukuran jendela/window aplikasi

label = tk.Label(
  zandela,
  text="Welcome to my app",
  font=("Arial", 16), # mengatur font label
  fg="blue", # mengatur warna teks label
  bg="white", # mengatur warna latar belakang label
  padx=10, # mengatur padding horizontal label
  pady=10, # mengatur padding vertikal label
  relief=tk.RAISED, # mengatur gaya bingkai label
  bd=2 # mengatur ketebalan bingkai label
  ) # membuat label dengan teks
label.pack() # menampilkan label di jendela aplikasi

img = Image.open("../person.jpg") # memuat gambar dari file
img = img.resize((100, 100), Image.LANCZOS) # mengubah ukuran gambar
img = ImageTk.PhotoImage(img) # mengonversi gambar menjadi format yang dapat digunakan tkinter
image_label = tk.Label(zandela, image=img) # membuat label untuk gambar
image_label.pack(pady=20) # menampilkan label gambar di jendela aplikasi

zandela.mainloop() # menjalankan aplikasi tkinter
