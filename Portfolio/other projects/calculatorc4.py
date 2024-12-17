import tkinter as tk

def button_click(char):
    if entry.get() != "ERROR!":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + char)

def evaluate():
    try:
        result = str(eval(entry.get()))  
        entry.delete(0, tk.END)
        entry.insert(tk.END, result) 
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR!")
        entry.config(state=tk.DISABLED)

def clear():
    entry.delete(0, tk.END)
    entry.config(state=tk.NORMAL) 

root = tk.Tk()
root.title("C4 Bomb Calculator")
root.geometry("700x700+700+200")  
root.config(bg="black") 

bomb_casing = tk.Frame(root, bg="#333", bd=10, relief="solid")
bomb_casing.pack(padx=50, pady=50)

entry = tk.Entry(bomb_casing, width=16, font=('Courier New', 24, 'bold'), borderwidth=6, relief="sunken", 
                 justify='center', fg="lime", bg="black")
entry.grid(row=0, column=0, columnspan=5, pady=20)

button_layout = [
    ['7', '8', '9', '/', '//'],['4', '5', '6', '*', '**'],['1', '2', '3', '-', '+'],['0', '.', '=', 'C', '']
]

def create_button(text, row, col, bg, fg, command=None):
    button = tk.Button(bomb_casing, text=text, width=6, height=3, font=('Courier New', 18, 'bold'), 
                       bg=bg, fg=fg, relief="raised", bd=4, command=command)
    button.grid(row=row, column=col, padx=5, pady=5)

for r, row in enumerate(button_layout, start=1):
    for c, button in enumerate(row):
        if button == '=':
            create_button(button, r, c, bg="red", fg="white", command=evaluate)  
        elif button == 'C':
            create_button(button, r, c, bg="green", fg="white", command=clear)  
        else:
            create_button(button, r, c, bg="#666", fg="white", command=lambda t=button: button_click(t))

root.mainloop()
