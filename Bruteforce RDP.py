import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import socket
import threading
import time
import queue

# Configuration par défaut
DEFAULT_RDP_PORT = 3389
DEFAULT_DELAY = 1  # Délai par défaut entre les tentatives en secondes
DEFAULT_THREADS = 10  # Nombre de threads par défaut

usernames = []  # Définir la liste des noms d'utilisateur en dehors de la fonction
passwords = []  # Définir la liste des mots de passe en dehors de la fonction

def check_rdp(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=5) as sock:
            return f"Serveur RDP trouvé à {ip}:{port}\n"
    except (socket.timeout, ConnectionRefusedError, socket.gaierror) as e:
        return f"Impossible de se connecter à {ip}:{port} - {e}\n"

def brute_force(ip, username, password, delay, result_queue):
    # Simulation de la vérification des identifiants
    # Cette partie ne fera pas de vérification réelle
    result_queue.put(f"Test Username: {username}, Password: {password}, IP: {ip}\n")
    time.sleep(delay)  # Ajouter un délai entre les tentatives
    if username == "Rachid" and password == "Rootroot1234.":
        result_queue.put(f"Success! Username: {username}, Password: {password}, IP: {ip}\n")
        result_queue.put(("SUCCESS", username, password, ip))
    else:
        result_queue.put(f"Failed! Username: {username}, Password: {password}, IP: {ip}\n")

def start_brute_force(ip_address, usernames, passwords, threads, delay, result_queue):
    result = check_rdp(ip_address, DEFAULT_RDP_PORT)
    result_queue.put(result)
    if "Serveur RDP trouvé" in result:
        result_queue.put("Le processus de brute force a commencé.\n")
        thread_list = []
        for username in usernames:
            for password in passwords:
                while threading.active_count() > threads:
                    time.sleep(0.1)  # Attendre qu'un thread soit disponible
                t = threading.Thread(target=brute_force, args=(ip_address, username, password, delay, result_queue))
                t.start()
                thread_list.append(t)
        for t in thread_list:
            t.join()

def load_file(entry, target_list, label):
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(tk.END, filename)  # Afficher le nom du fichier dans l'entrée
        label.config(text=f"Fichier chargé : {filename}")  # Afficher le nom du fichier dans l'étiquette
        target_list.clear()
        with open(filename, 'r') as file:
            target_list.extend([line.strip() for line in file if line.strip()])  # Charger les données dans la liste cible

def on_start_button_click(ip_entry, usernames_entry, passwords_entry, threads_entry, delay_entry, result_queue):
    ip_address = ip_entry.get()
    usernames_list = usernames if usernames else usernames_entry.get().split(',')
    passwords_list = passwords if passwords else passwords_entry.get().split(',')
    threads = int(threads_entry.get())
    delay = float(delay_entry.get())

    # Clear the output text box before starting
    result_queue.put(None)  # Signal to clear the output box

    # Start brute force in a separate thread
    t = threading.Thread(target=start_brute_force, args=(ip_address, usernames_list, passwords_list, threads, delay, result_queue))
    t.start()

def process_result_queue(output_text, result_queue):
    try:
        while True:
            result = result_queue.get_nowait()
            if result is None:
                output_text.delete(1.0, tk.END)
            elif isinstance(result, tuple) and result[0] == "SUCCESS":
                messagebox.showinfo("Succès", f"Les identifiants corrects ont été trouvés!\nUsername: {result[1]}, Password: {result[2]}, IP: {result[3]}")
            else:
                output_text.insert(tk.END, result)
            output_text.see(tk.END)  # Scroll to the end of the text box
    except queue.Empty:
        pass
    root.after(100, process_result_queue, output_text, result_queue)

# Créer la fenêtre principale
root = tk.Tk()
root.title("RDP Brute Force Tool")

# Ajouter les champs pour entrer l'adresse IP, les identifiants et les mots de passe
tk.Label(root, text="Adresse IP:").grid(row=0, column=0)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

tk.Label(root, text="Identifiants (séparés par des virgules ou charger un fichier):").grid(row=1, column=0)
usernames_entry = tk.Entry(root)
usernames_entry.grid(row=1, column=1)
usernames_label = tk.Label(root, text="")
usernames_label.grid(row=1, column=3)
usernames_button = tk.Button(root, text="Charger", command=lambda: load_file(usernames_entry, usernames, usernames_label))
usernames_button.grid(row=1, column=2)

tk.Label(root, text="Mots de passe (séparés par des virgules ou charger un fichier):").grid(row=2, column=0)
passwords_entry = tk.Entry(root)
passwords_entry.grid(row=2, column=1)
passwords_label = tk.Label(root, text="")
passwords_label.grid(row=2, column=3)
passwords_button = tk.Button(root, text="Charger", command=lambda: load_file(passwords_entry, passwords, passwords_label))
passwords_button.grid(row=2, column=2)

tk.Label(root, text="Nombre de threads:").grid(row=3, column=0)
threads_entry = tk.Entry(root)
threads_entry.grid(row=3, column=1)
threads_entry.insert(0, str(DEFAULT_THREADS))

tk.Label(root, text="Délai entre les tentatives (en secondes):").grid(row=4, column=0)
delay_entry = tk.Entry(root)
delay_entry.grid(row=4, column=1)
delay_entry.insert(0, str(DEFAULT_DELAY))

# Ajouter un bouton pour lancer le processus de brute force
start_button = tk.Button(root, text="Démarrer", command=lambda: on_start_button_click(ip_entry, usernames_entry, passwords_entry, threads_entry, delay_entry, result_queue))
start_button.grid(row=5, column=0, columnspan=3)

# Ajouter une boîte de texte défilante pour afficher les résultats
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
output_text.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

# Créer une queue pour les résultats
result_queue = queue.Queue()

# Lancer la boucle principale de la fenêtre et le traitement de la queue
root.after(100, process_result_queue, output_text, result_queue)
root.mainloop()
