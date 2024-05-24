import tkinter as tk
from tkinter import scrolledtext
import nmap
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import threading

def scan_os_mac_ports_vulnerabilities(target_ip, aggressive=False):
    scanner = nmap.PortScanner()

    # Construction des arguments du scan
    arguments = '-sS -O'  # Arguments de base pour le scan d'OS et d'adresse MAC
    if aggressive:
        arguments += ' -T4'  # Ajout de l'option agressive -T4

    # Scan d'OS et d'adresse MAC
    result = f"Scanning OS and MAC for {target_ip}...\n"
    scanner.scan(target_ip, arguments=arguments)

    for host in scanner.all_hosts():
        if 'osmatch' in scanner[host]:
            result += f"Adresse IP : {host}\n"
            result += "Système(s) d'exploitation détecté(s) :\n"
            for os_match in scanner[host]['osmatch']:
                result += f"- Nom : {os_match['name']}, Précision : {os_match['accuracy']}%\n"
        else:
            result += f"Aucun système d'exploitation détecté pour {host}\n"

        if 'addresses' in scanner[host]:
            result += f"Adresse MAC : {scanner[host]['addresses'].get('mac', 'Non trouvée')}\n"
        else:
            result += f"Aucune adresse MAC trouvée pour {host}\n"

    # Scan de ports et de vulnérabilités
    result += f"\nScanning ports and vulnerabilities for {target_ip}...\n"
    arguments = '-p 1-4025'  # Arguments de base pour le scan de ports et de vulnérabilités
    if aggressive:
        arguments += ' -T4'  # Ajout de l'option agressive -T4
    scanner.scan(target_ip, arguments=arguments)

    open_ports = []
    for host in scanner.all_hosts():
        for port in scanner[host].get('tcp', {}):
            if scanner[host]['tcp'][port]['state'] == 'open':
                service_name = scanner[host]['tcp'][port]['name']
                result += f"Port {port} ({service_name}) ouvert sur {host}\n"
                open_ports.append(port)
    
    # Scan de vulnérabilités pour les ports ouverts
    if open_ports:
        ports_str = ','.join(str(port) for port in open_ports)
        arguments = f'-p {ports_str} --script vulners'  # Arguments de base pour le scan de vulnérabilités
        if aggressive:
            arguments += ' -T4'  # Ajout de l'option agressive -T4
        scanner.scan(target_ip, arguments=arguments)
        result += "\nRésultats du scan de vulnérabilités :\n"
        for host in scanner.all_hosts():
            for port in scanner[host].get('tcp', {}):
                if 'script' in scanner[host]['tcp'][port] and 'vulners' in scanner[host]['tcp'][port]['script']:
                    result += f"Port {port} vulnérabilités :\n"
                    vulns = scanner[host]['tcp'][port]['script']['vulners']
                    vulns_dict = json.loads(vulns)
                    for vuln_id, vuln_info in vulns_dict.items():
                        result += f"  {vuln_id}: {vuln_info['title']}\n"
                else:
                    result += f"Port {port} pas de vulnérabilité trouvée.\n"
    else:
        result += "Aucun port ouvert trouvé. Aucun scan de vulnérabilité effectué.\n"

    return result

def start_scan():
    def scan_thread():
        target_ip = ip_entry.get()
        aggressive_scan = aggressive_var.get()
        scan_result = scan_os_mac_ports_vulnerabilities(target_ip, aggressive_scan)
        output_text.configure(state='normal')
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, scan_result)
        output_text.configure(state='disabled')
    
    # Démarrer le scan dans un thread séparé
    scan_thread = threading.Thread(target=scan_thread)
    scan_thread.start()

def generate_pdf():
    def pdf_thread():
        target_ip = ip_entry.get()
        aggressive_scan = aggressive_var.get()
        scan_result = scan_os_mac_ports_vulnerabilities(target_ip, aggressive_scan)

        # Générer le PDF
        pdf_filename = "scan_result.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "Résultat scan de ports et de vulnérabilités")
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 730, "Résultats scan de ports et de Vulnérabilités")
        c.setFont("Helvetica", 12)
        y = 710
        for line in scan_result.split('\n'):
            if line.strip():  # Ignorer les lignes vides
                c.drawString(100, y, line)
                y -= 20
        c.save()
        output_text.insert(tk.END, f"\nRendu PDF généré : {pdf_filename}\n")
    
    # Générer le PDF dans un thread séparé
    pdf_thread = threading.Thread(target=pdf_thread)
    pdf_thread.start()

def create_gui():
    global ip_entry, aggressive_var, output_text
    
    # Créer une fenêtre
    window = tk.Tk()
    window.title("Nmap Scan")

    # Ajouter une zone de texte pour l'adresse IP
    ip_label = tk.Label(window, text="Adresse IP:")
    ip_label.grid(row=0, column=0)
    ip_entry = tk.Entry(window)
    ip_entry.grid(row=0, column=1)

    # Ajouter une case à cocher pour spécifier l'agressivité du scan
    aggressive_var = tk.BooleanVar()
    aggressive_checkbox = tk.Checkbutton(window, text="Scan agressif (-T4)", variable=aggressive_var)
    aggressive_checkbox.grid(row=0, column=2)

    # Ajouter un bouton pour lancer le scan
    scan_button = tk.Button(window, text="Lancer le scan", command=start_scan)
    scan_button.grid(row=0, column=3)

    # Ajouter un bouton pour générer le PDF
    pdf_button = tk.Button(window, text="Générer PDF", command=generate_pdf)
    pdf_button.grid(row=0, column=4)

    # Ajouter une zone de texte pour afficher les résultats
    output_text = scrolledtext.ScrolledText(window, width=60, height=20, state='disabled')
    output_text.grid(row=1, column=0, columnspan=5)

    # Exécute la boucle principale de l'interface graphique
    window.mainloop()

if __name__ == "__main__":
    create_gui()
