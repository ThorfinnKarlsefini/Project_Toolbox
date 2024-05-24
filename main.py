import tkinter as tk
from subprocess import call
from PIL import Image, ImageTk  # Importez les modules nécessaires pour les images
import threading

def run_script(script_name):
    call(["python", script_name])

def run_script1():
    threading.Thread(target=run_script, args=("Scan reseau.py",)).start()

def run_script2():
    threading.Thread(target=run_script, args=("SCAN NMAP FINALE.py",)).start()

def run_script3():
    threading.Thread(target=run_script, args=("Password solidity.py",)).start()

def run_script4():
    threading.Thread(target=run_script, args=("Bruteforce SSH.py",)).start()

def run_script5():
    threading.Thread(target=run_script, args=("Bruteforce RDP.py",)).start()

def run_script6():
    threading.Thread(target=run_script, args=("Chiffrement MDP.py",)).start()

def run_script7():
    threading.Thread(target=run_script, args=("cracker de mdp.py",)).start()

def run_script8():
    threading.Thread(target=run_script, args=("pdf_merger.py",)).start()

def run_script9():
    threading.Thread(target=run_script, args=("pdf_toolbox.py",)).start()

# Créez la fenêtre principale
root = tk.Tk()
root.title("ToolBox by Rachid")

# Définissez la taille de la fenêtre
root.geometry("1000x900")  # Largeur x Hauteur

# Charger l'image (assurez-vous que le chemin est correct)
image_path = "cybersecurity2.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Créer un widget Label pour afficher l'image
label = tk.Label(root, image=photo)
label.image = photo  # Garder une référence de l'image
label.pack(pady=20)  # Ajustez l'espacement selon vos besoins

# Ajoutez un bouton pour chaque script
button1 = tk.Button(root, text="Scan Reseaux", command=run_script1)
button1.pack(pady=10)

button2 = tk.Button(root, text="Scan de Port et Vulnerabilité", command=run_script2)
button2.pack(pady=10)

button3 = tk.Button(root, text="Test des solidité du mots de passe", command=run_script3)
button3.pack(pady=10)

button4 = tk.Button(root, text="Brute force SSH", command=run_script4)
button4.pack(pady=10)

button5 = tk.Button(root, text="Brute force RDP", command=run_script5)
button5.pack(pady=10)

button6 = tk.Button(root, text="Chiffrement Mot de passe", command=run_script6)
button6.pack(pady=10)

button7 = tk.Button(root, text="Dechiffrement de Mot de passe", command=run_script7)
button7.pack(pady=10)

button8 = tk.Button(root, text="PDF fusion", command=run_script8)
button8.pack(pady=10)

button9 = tk.Button(root, text="PDF chiffrement", command=run_script9)
button9.pack(pady=10)

# Démarrer la boucle Tkinter
root.mainloop()
