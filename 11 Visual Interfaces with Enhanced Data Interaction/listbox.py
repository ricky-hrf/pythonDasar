import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("500x500")

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

# menambahkan item 
for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

# fungsi untuk menampilkan item terpilih
def pilihan():
    selected_items = listbox.curselection()
    selected_text = ", ".join([listbox.get(i) for i in selected_items])
    print("Item terpilih:", selected_text)

tk.Button(root, text="Tampilkan item terpilih", command=pilihan).pack()

root.mainloop()