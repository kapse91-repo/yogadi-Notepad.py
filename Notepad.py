import tkinter as tk
from tkinter import messagebox,filedialog

def new_file():
    text.delete(1.0, tk.END)
    
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
            
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("Info", "File saved Successfully!")
            
root = tk.Tk()
root.title("Write NOTES")
root.geometry("600x400")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New Tab", command=new_file)
file_menu.add_command(label="New Window", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Recent", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=new_file)
file_menu.add_command(label="Save all", command=new_file)

file_menu.add_separator()
file_menu.add_command(label="Close Tab", command=root.quit)
file_menu.add_command(label="Close Window", command=root.quit)

menu.add_cascade(label="Edit", menu=file_menu)

file_menu.add_command(label="Cut", command=save_file)
file_menu.add_command(label="Copy", command=new_file)
file_menu.add_command(label="Past", command=new_file)
file_menu.add_command(label="Delete", command=new_file)

file_menu.add_separator()
file_menu.add_command(label="Select all", command=root.quit)
file_menu.add_command(label="Time/Date", command=root.quit)

menu.add_cascade(label="View", menu=file_menu)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
text = tk.Text(root,wrap=tk.WORD, font=("Arial", 12), fg="black", bg="white")
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()
