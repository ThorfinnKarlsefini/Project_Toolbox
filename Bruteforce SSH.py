import tkinter as tk
from tkinter import filedialog, messagebox
import paramiko
import threading

class SSHBruteForceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SSH Connection Test")

        # Mode selection
        self.mode_var = tk.StringVar(root)
        self.mode_var.set("single")  # default value
        self.mode_menu = tk.OptionMenu(root, self.mode_var, "single", "multi", command=self.toggle_mode)
        self.mode_menu.pack()

        # IP address field
        self.label_ip = tk.Label(root, text="Enter IP address:")
        self.label_ip.pack()
        self.entry_ip = tk.Entry(root)
        self.entry_ip.pack()

        # Username and Password fields for single mode
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.entry_password = tk.Entry(root, show="*")  # Added the show="*" to hide the password
        self.entry_password.pack()

        # Username and Password file fields for multi mode
        self.username_file_label = tk.Label(root, text="Username File:")
        self.username_file_button = tk.Button(root, text="Browse", command=self.choose_username_file)
        self.entry_username_file = tk.Entry(root)

        self.password_file_label = tk.Label(root, text="Password File:")
        self.password_file_button = tk.Button(root, text="Browse", command=self.choose_password_file)
        self.entry_password_file = tk.Entry(root)

        # Default state
        self.toggle_mode()

        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.on_submit)
        self.submit_button.pack()

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def format_path(self, path):
        return path.replace("\\", "/")

    def choose_username_file(self):
        file_path = filedialog.askopenfilename(title="Select Username File", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.entry_username_file.delete(0, tk.END)
            self.entry_username_file.insert(0, file_path)

    def choose_password_file(self):
        file_path = filedialog.askopenfilename(title="Select Password File", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.entry_password_file.delete(0, tk.END)
            self.entry_password_file.insert(0, file_path)

    def toggle_mode(self, *args):
        mode = self.mode_var.get()
        if mode == "single":
            self.username_label.pack()
            self.entry_username.pack()
            self.password_label.pack()
            self.entry_password.pack()
            self.username_file_label.pack_forget()
            self.username_file_button.pack_forget()
            self.entry_username_file.pack_forget()
            self.password_file_label.pack_forget()
            self.password_file_button.pack_forget()
            self.entry_password_file.pack_forget()
        elif mode == "multi":
            self.username_label.pack_forget()
            self.entry_username.pack_forget()
            self.password_label.pack_forget()
            self.entry_password.pack_forget()
            self.username_file_label.pack()
            self.username_file_button.pack()
            self.entry_username_file.pack()
            self.password_file_label.pack()
            self.password_file_button.pack()
            self.entry_password_file.pack()

    def on_submit(self):
        mode = self.mode_var.get()
        ip_address = self.entry_ip.get()
        if mode == "single":
            username = self.entry_username.get()
            password = self.entry_password.get()
            self.start_single_scan(ip_address, username, password)
        elif mode == "multi":
            username_file = self.entry_username_file.get()
            password_file = self.entry_password_file.get()
            self.start_multi_scan(ip_address, username_file, password_file)

    def start_single_scan(self, ip_address, username, password):
        threading.Thread(target=self.single_scan, args=(ip_address, username, password)).start()

    def single_scan(self, ip_address, username, password):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip_address, username=username, password=password)
            self.update_result_label("Connection successful", "green")
            ssh.close()
        except paramiko.AuthenticationException:
            self.update_result_label("Connection failed: Invalid credentials", "red")
        except Exception as e:
            self.update_result_label(f"Connection failed: {str(e)}", "red")

    def start_multi_scan(self, ip_address, username_file, password_file):
        threading.Thread(target=self.multi_scan, args=(ip_address, username_file, password_file)).start()

    def multi_scan(self, ip_address, username_file, password_file):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            with open(username_file, 'r') as user_file, open(password_file, 'r') as pass_file:
                for user, passw in zip(user_file, pass_file):
                    try:
                        ssh.connect(ip_address, username=user.strip(), password=passw.strip())
                        self.update_result_label(f"Connection successful for {user.strip()}", "green")
                        ssh.close()
                    except paramiko.AuthenticationException:
                        self.update_result_label(f"Connection failed for {user.strip()}: Invalid credentials", "red")
                    except Exception as e:
                        self.update_result_label(f"Connection failed for {user.strip()}: {str(e)}", "red")
        except FileNotFoundError:
            self.update_result_label("File not found", "red")

    def update_result_label(self, message, color):
        self.result_label.config(text=message, fg=color)

def main():
    root = tk.Tk()
    app = SSHBruteForceApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
