import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected = combo.get()
    label_result.config(text=f"Anda memilih: {selected}")

root = tk.Tk()
root.title("Contoh Combobox")
root.geometry("300x200")

combo = ttk.Combobox(
    root,
    values=["Pilih Kota", "Jakarta", "Bandung", "Surabaya", "Yogyakarta"], 
    state="readonly"  
)
combo.current(0)  
combo.pack(pady=20)

combo.bind("<<ComboboxSelected>>", on_select)

label_result = tk.Label(root, text="", font=("Arial", 10))
label_result.pack()

root.mainloop()