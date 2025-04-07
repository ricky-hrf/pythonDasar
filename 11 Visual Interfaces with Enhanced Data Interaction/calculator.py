import tkinter as tk

# Fungsi untuk operator ke entry
def tombol_klik(angka):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(angka))

def hitung():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

# Membuat window utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

# Entry untuk menampilkan input dan hasil
entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Daftar tombol
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Membuat tombol
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=hitung, bg="#4CAF50", fg="white")
    elif text in '+-*/':
        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: tombol_klik(t), bg="#2196F3", fg="white")
    else:
        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: tombol_klik(t), bg="#e0e0e0")
    btn.grid(row=row, column=col, sticky="nsew")

# Tombol Clear
clear_btn = tk.Button(root, text="C", padx=20, pady=10, command=clear, bg="#f44336", fg="white")
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Mengatur ukuran grid
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()