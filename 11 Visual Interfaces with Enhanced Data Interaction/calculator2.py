import tkinter as tk
from tkinter import ttk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Calculator")
        self.current_theme = "light"
        self.memory = 0
        self.history = []
        
        # Setup UI
        self.create_widgets()
        self.setup_keyboard()
        self.apply_theme()

    def create_widgets(self):
        # Entry Field
        self.entry = tk.Entry(self.root, font=('Arial', 18), width=25, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Memory Display
        self.memory_label = tk.Label(self.root, text="Memory: 0", font=('Arial', 10))
        self.memory_label.grid(row=1, column=0, columnspan=5, sticky='w', padx=10)

        # History Frame
        history_frame = ttk.Frame(self.root)
        history_frame.grid(row=0, column=5, rowspan=6, padx=10, pady=10, sticky='ns')
        
        self.history_list = tk.Listbox(history_frame, width=30, height=15)
        self.history_list.pack(side=tk.LEFT, fill=tk.BOTH)
        
        scrollbar = ttk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.history_list.yview)

        # Number Buttons
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3), ('⌫', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('^', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3), ('π', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3), ('e', 5, 4)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Scientific Buttons
        sci_buttons = [
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2),
            ('log', 6, 3), ('ln', 6, 4), ('√', 7, 0),
            ('!', 7, 1), ('±', 7, 2), ('MC', 7, 3),
            ('MR', 7, 4), ('M+', 8, 3), ('M-', 8, 4)
        ]

        for (text, row, col) in sci_buttons:
            self.create_button(text, row, col, is_scientific=True)

        # Control Buttons
        self.create_button('C', 8, 0, columnspan=2)
        self.create_button('Theme', 8, 2)

    def create_button(self, text, row, col, columnspan=1, is_scientific=False):
        btn = tk.Button(self.root, text=text, padx=20, pady=10, command=lambda t=text: self.on_button_click(t),
                      font=('Arial', 12, 'bold' if is_scientific else 'normal'))
        btn.grid(row=row, column=col, columnspan=columnspan, sticky='nsew')
        return btn

    def on_button_click(self, value):
        current = self.entry.get()
        
        if value == '=':
            self.calculate()
        elif value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '⌫':
            self.entry.delete(len(current)-1)
        elif value == '±':
            self.entry.insert(0, '-' if not current.startswith('-') else '')
        elif value == 'Theme':
            self.toggle_theme()
        elif value == 'π':
            self.entry.insert(tk.END, str(math.pi))
        elif value == 'e':
            self.entry.insert(tk.END, str(math.e))
        elif value in ['MC', 'MR', 'M+', 'M-']:
            self.memory_operation(value)
        elif value in ['sin', 'cos', 'tan', 'log', 'ln', '√', '!', '^']:
            self.handle_scientific(value)
        else:
            self.entry.insert(tk.END, value)

    def handle_scientific(self, func):
        try:
            num = float(self.entry.get())
            result = {
                'sin': math.sin(math.radians(num)),
                'cos': math.cos(math.radians(num)),
                'tan': math.tan(math.radians(num)),
                'log': math.log10(num),
                'ln': math.log(num),
                '√': math.sqrt(num),
                '!': math.factorial(int(num)),
                '^': lambda: num ** 2
            }[func]()
            
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            self.add_history(f"{func}({num}) = {result}")
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def memory_operation(self, op):
        try:
            current = float(self.entry.get())
            if op == 'M+':
                self.memory += current
            elif op == 'M-':
                self.memory -= current
            elif op == 'MC':
                self.memory = 0
            elif op == 'MR':
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(self.memory))
            
            self.memory_label.config(text=f"Memory: {self.memory:.2f}")
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
            self.add_history(f"{expression} = {result}")
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def add_history(self, entry):
        self.history.append(entry)
        self.history_list.insert(tk.END, entry)
        if len(self.history) > 10:
            self.history_list.delete(0)
            self.history.pop(0)

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        colors = {
            "light": {'bg': '#ffffff', 'fg': '#000000', 'btn_bg': '#e0e0e0'},
            "dark": {'bg': '#2d2d2d', 'fg': '#ffffff', 'btn_bg': '#4d4d4d'}
        }
        theme = colors[self.current_theme]
        
        self.root.config(bg=theme['bg'])
        self.entry.config(bg=theme['btn_bg'], fg=theme['fg'])
        self.memory_label.config(bg=theme['bg'], fg=theme['fg'])
        
        for child in self.root.winfo_children():
            if isinstance(child, tk.Button):
                child.config(bg=theme['btn_bg'], fg=theme['fg'])

    def setup_keyboard(self):
        key_bindings = {
            '<Return>': lambda e: self.calculate(),
            '<BackSpace>': lambda e: self.entry.delete(len(self.entry.get())-1),
            'c': lambda e: self.entry.delete(0, tk.END),
            's': lambda e: self.handle_scientific('sin'),
            'o': lambda e: self.handle_scientific('cos'),
            't': lambda e: self.handle_scientific('tan'),
            'l': lambda e: self.handle_scientific('log'),
            'n': lambda e: self.handle_scientific('ln'),
            'r': lambda e: self.handle_scientific('√'),
            '!': lambda e: self.handle_scientific('!')
        }
        
        for key, func in key_bindings.items():
            self.root.bind(key, func)
        
        for num in range(10):
            self.root.bind(str(num), lambda e, n=num: self.entry.insert(tk.END, str(n)))

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    
    # Configure grid weights
    for i in range(9):
        root.grid_rowconfigure(i, weight=1)
    for i in range(5):
        root.grid_columnconfigure(i, weight=1)
    
    root.mainloop()