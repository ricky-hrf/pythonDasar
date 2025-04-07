import tkinter as tk

window = tk.Tk()
window.title("Canvas")
window = tk.Canvas(
  window, width=400, height=300, bg="white"
)
window.pack()

# shape
window.create_rectangle(50, 50, 150, 150, fill="blue")
window.create_oval(200, 100, 300, 290, fill="red")
window.create_line(10, 10, 390, 400, width=3)

window.mainloop()