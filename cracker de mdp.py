import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def crack_md5(hash_to_crack, passwords):
    for password in passwords:
        if hashlib.md5(password.encode()).hexdigest() == hash_to_crack:
            return password
    return None

def crack_sha1(hash_to_crack, passwords):
    for password in passwords:
        if hashlib.sha1(password.encode()).hexdigest() == hash_to_crack:
            return password
    return None

def crack_sha256(hash_to_crack, passwords):
    for password in passwords:
        if hashlib.sha256(password.encode()).hexdigest() == hash_to_crack:
            return password
    return None

def crack_hash():
    hash_to_crack = hash_entry.get().strip()
    hash_type = hash_type_var.get()
    password_file = password_file_path.get()

    if not hash_to_crack or not hash_type or not password_file:
        messagebox.showerror("Error", "All fields are required")
        return

    passwords = load_passwords(password_file)

    if hash_type == 'md5':
        result = crack_md5(hash_to_crack, passwords)
    elif hash_type == 'sha1':
        result = crack_sha1(hash_to_crack, passwords)
    elif hash_type == 'sha256':
        result = crack_sha256(hash_to_crack, passwords)
    else:
        messagebox.showerror("Error", "Unsupported hash type")
        return

    if result:
        messagebox.showinfo("Success", f"Password found: {result}")
    else:
        messagebox.showinfo("Failure", "Password not found")

def select_password_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        password_file_path.set(file_path)

# GUI Setup
root = tk.Tk()
root.title("Hash Cracker")

tk.Label(root, text="Enter the hash to crack:").grid(row=0, column=0, padx=10, pady=5)
hash_entry = tk.Entry(root, width=50)
hash_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select hash type:").grid(row=1, column=0, padx=10, pady=5)
hash_type_var = tk.StringVar(value="md5")
hash_type_menu = tk.OptionMenu(root, hash_type_var, "md5", "sha1", "sha256")
hash_type_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select password file:").grid(row=2, column=0, padx=10, pady=5)
password_file_path = tk.StringVar()
password_file_entry = tk.Entry(root, textvariable=password_file_path, width=50)
password_file_entry.grid(row=2, column=1, padx=10, pady=5)
password_file_button = tk.Button(root, text="Browse", command=select_password_file)
password_file_button.grid(row=2, column=2, padx=10, pady=5)

crack_button = tk.Button(root, text="Crack Hash", command=crack_hash)
crack_button.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
