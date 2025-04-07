import tkinter as tk

def save_note():
  text_content = text_box.get("1.0", tk.END) # mengambil teks dari text widget
  with open("catatan.txt", "w") as file:
    file.write(text_content)
    label_status.config(text="Catatan disimpan!") # mengubah teks label status saat catatan disimpan

root = tk.Tk() # buat jendela utama/window aplikasi
root.title("Notepad Sederhana") # membuat judul jendela/window aplikasi

text_frame = tk.Frame(root) # membuat frame untuk text widget
text_frame.pack(padx=10, pady=10) # menampilkan frame di jendela aplikasi

scrollbar = tk.Scrollbar(text_frame) # membuat scrollbar untuk text widget
scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # menampilkan scrollbar di sebelah kanan text widget

text_box = tk.Text(
  text_frame,
  width=50,
  height=15,
  yscrollcommand=scrollbar.set,
  wrap=tk.WORD
) # membuat text widget untuk menampilkan dan mengedit teks

text_box.pack(side=tk.LEFT)

scrollbar.config(command=text_box.yview)

# Tombol simpan
btn_save = tk.Button(
    root,
    text="Simpan Catatan",
    command=save_note,
    bg="#2196F3",
    fg="white"
)
btn_save.pack(pady=5)

# Label status
label_status = tk.Label(root, text="", fg="green")
label_status.pack()

root.mainloop() # menjalankan aplikasi tkinter