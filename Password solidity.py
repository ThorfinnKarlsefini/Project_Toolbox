import tkinter as tk
import threading
from zxcvbn import zxcvbn
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import hashlib

class PasswordAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Analyzer Tool")
        
        # Set the window size
        self.root.geometry("400x300")  # Width x Height

        tk.Label(root, text="Veuillez entrer votre mot de passe:").grid(row=0)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1)

        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.grid(row=2)

        self.result_text = tk.StringVar()
        result_label = tk.Label(root, textvariable=self.result_text)
        result_label.grid(row=4)

        self.canvas = None

    def check_pwned(self, password):
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        head, tail = sha1password[:5], sha1password[5:]
        response = requests.get(f'https://api.pwnedpasswords.com/range/{head}')
        hashes = (line.split(':') for line in response.text.splitlines())
        count = next((int(count) for t, count in hashes if t == tail), 0)
        return count

    def analyse_password(self, password):
        analysis = zxcvbn(password)
        return analysis

    def submit(self):
        password = self.password_entry.get()
        threading.Thread(target=self.process_password, args=(password,)).start()

    def process_password(self, password):
        analysis = self.analyse_password(password)
        pwned_count = self.check_pwned(password)

        # Mise à jour de l'interface utilisateur doit se faire dans le thread principal
        self.root.after(0, self.update_ui, analysis, pwned_count)

    def update_ui(self, analysis, pwned_count):
        self.result_text.set(f"Score : {analysis['score']}\nSuggestions : {', '.join(analysis['feedback']['suggestions'])}\nCe mot de passe a été exposé {pwned_count} fois dans des violations de données.")

        # Création d'un graphique de barres pour visualiser la force du mot de passe
        fig = plt.figure(figsize=(3, 2))
        plt.bar(['Score'], [analysis['score']], color=['green' if analysis['score'] > 2 else 'red'])
        plt.ylim(0, 4)
        plt.ylabel('Score')
        plt.title('Force du mot de passe')

        # Affichage du graphique dans l'interface tkinter
        if self.canvas:
            self.canvas.get_tk_widget().grid_forget()
        
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column=0)

def main():
    root = tk.Tk()
    app = PasswordAnalyzer(root)
    root.mainloop()

if __name__ == '__main__':
    main()
