import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import os
import subprocess

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("C++ Text Editor Devloped By Mr.Sumit Gadwal")
        self.master.geometry("600x400")

        self.current_file = None

        self.create_widgets()

    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)

        # Text area
        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack(expand=True, fill="both")

        # Run button
        self.run_button = tk.Button(self.master, text="Run", command=self.run_code)
        self.run_button.pack()

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_file = None

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("C++ Files", "*.cpp"), ("All Files", "*.*")])
        if filename:
            with open(filename, "r") as file:
                code = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", code)
            self.current_file = filename

    def save_file(self):
        if self.current_file:
            code = self.text_area.get("1.0", tk.END)
            with open(self.current_file, "w") as file:
                file.write(code)
            messagebox.showinfo("Success", f"Changes saved to {self.current_file}")
        else:
            self.save_as()

    def save_as(self):
        code = self.text_area.get("1.0", tk.END)
        filename = filedialog.asksaveasfilename(defaultextension=".cpp", filetypes=[("C++ Files", "*.cpp"), ("All Files", "*.*")])
        if filename:
            with open(filename, "w") as file:
                file.write(code)
            self.current_file = filename
            messagebox.showinfo("Success", f"Code saved as {filename}")

    def run_code(self):
        if self.current_file:
            process = subprocess.Popen(["g++", self.current_file, "-o", "output.exe"])
            process.wait()
            if os.path.exists("output.exe"):
                subprocess.Popen(["output.exe"], shell=True)
            else:
                messagebox.showerror("Error", "Compilation failed!")
        else:
            messagebox.showerror("Error", "No file opened to run!")

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
