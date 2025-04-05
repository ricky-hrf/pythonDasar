import tkinter as tk
from tkinter import messagebox

def show_all():
    gender = var_gender.get()
    hobbies = [h for h, v in hobbies_vars.items() if v.get()]
    print(f"Gender: {gender}, Hobbies: {hobbies}")

root = tk.Tk()

var_gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=var_gender, value="male").pack()
tk.Radiobutton(root, text="Female", variable=var_gender, value="female").pack()

hobbies_vars = {
    "music": tk.BooleanVar(),
    "sports": tk.BooleanVar()
}
for hobby, var in hobbies_vars.items():
    tk.Checkbutton(root, text=hobby.capitalize(), variable=var).pack()

tk.Button(root, text="Submit", command=show_all).pack()

root.mainloop()