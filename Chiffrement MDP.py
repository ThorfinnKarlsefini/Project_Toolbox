import tkinter as tk
from tkinter import messagebox
import hashlib

def calculate_hashes():
    password = password_entry.get().strip()

    if not password:
        messagebox.showerror("Error", "Password field cannot be empty")
        return

    md5_hash = hashlib.md5(password.encode()).hexdigest()
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()

    md5_hash_entry.delete(0, tk.END)
    md5_hash_entry.insert(0, md5_hash)
    sha1_hash_entry.delete(0, tk.END)
    sha1_hash_entry.insert(0, sha1_hash)
    sha256_hash_entry.delete(0, tk.END)
    sha256_hash_entry.insert(0, sha256_hash)

# GUI Setup
root = tk.Tk()
root.title("Hash Generator")

tk.Label(root, text="Enter password:").grid(row=0, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, width=50)
password_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Hashes", command=calculate_hashes)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text="MD5: ").grid(row=2, column=0, padx=10, pady=5)
md5_hash_entry = tk.Entry(root, width=64)
md5_hash_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="SHA-1: ").grid(row=3, column=0, padx=10, pady=5)
sha1_hash_entry = tk.Entry(root, width=64)
sha1_hash_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="SHA-256: ").grid(row=4, column=0, padx=10, pady=5)
sha256_hash_entry = tk.Entry(root, width=64)
sha256_hash_entry.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()
