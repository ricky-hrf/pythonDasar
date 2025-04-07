import tkinter as tk

root = tk.Tk() # membuat jendela utama
root.title("Form Input") # memberi judul pada jendela
root.geometry("400x200") # mengatur ukuran jendela

label_petunjuk = tk.Label(
  root,
  text="Masukkan Nama Anda:",
  font=("Arial", 14),
  fg="blue",
)
label_petunjuk.pack(pady=10) # menampilkan label petunjuk di jendela

# entry widget untuk input teks
entry = tk.Entry(
  root,
  width=30,
  font=("Arial", 12),
  bg="white",
  fg="black",
)
entry.pack(pady=5)
entry.focus() # mengatur fokus pada entry saat aplikasi dibuka

# tombol submit
btn_submit = tk.Button(
  root,
  text="Submit",
  command=submit_data, # menghubungkan tombol dengan fungsi submit_data
  bg="#4CAF50",
  fg="white",
)
btn_submit.pack(pady=10) # menampilkan tombol di jendela

def submit_data():
  input_text = entry.get() # mengambil teks dari entry
  label_output.config(text=f"Anda mengetik: {input_text}") # menampilkan teks yang dimasukkan di label_output
  entry.delete(0, tk.END) # menghapus teks di entry setelah submit

label_output = tk.Label( root, text="", font=("Arial", 12)) # label untuk menampilkan output
label_output.pack() # menampilkan label output di jendela

root.mainloop() # menjalankan aplikasi tkinter