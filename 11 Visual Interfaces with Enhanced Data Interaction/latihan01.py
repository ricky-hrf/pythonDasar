from tkinter import *
from PIL import Image, ImageTk # impor modul Pillow

window = Tk()

try:
    image = Image.open("../person.jpg") # buka file JPG menggunakan Pillow
    resized_image = image.resize((200, 200), Image.LANCZOS) # ubah ukuran gambar
    photo = ImageTk.PhotoImage(resized_image) # konversi ke PhotoImage

    label = Label(
        window,
        text="Bro, do you even code?",
        font=("Arial", 16),
        fg="#00FF00",
        bg="black",
        padx=20,
        pady=20,
        relief=RAISED,
        bd=10,
        image=photo,
        compound="bottom",
    )
    label.image = photo  # simpan referensi gambar
    label.pack()

except Exception as e:
    print(f"Error: {e}")
    label = Label(window, text="Gambar tidak dapat dimuat")
    label.pack()

window.mainloop()