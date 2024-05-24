import socket
import subprocess
import ipaddress
import threading
import reportlab
from reportlab.pdfgen import canvas

# Obtenir l'adresse IP locale de l'hôte
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Obtenir le nom de la machine à partir de l'adresse IP
def get_host_name(ip_address):
    try:
        host_name = socket.gethostbyaddr(ip_address)[0]
        return host_name
    except Exception:
        return None

# Fonction pour scanner une seule adresse IP
def scan_ip(ip, active_hosts):
    result = subprocess.run(['ping', '-n', '1', '-w', '200', str(ip)], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        host_name = get_host_name(str(ip))
        if host_name:
            active_hosts.append((str(ip), host_name))
        else:
            active_hosts.append((str(ip), 'Nom inconnu'))

# Créer un fichier PDF avec les résultats
def create_pdf(hosts):
    c = canvas.Canvas('resultats_reseaux.pdf')
    c.drawString(100, 750, 'Résultats du Scan Réseau')
    c.drawString(80, 730, 'Adresse IP - Nom de la machine')
    y = 710
    for ip, host_name in hosts:
        c.drawString(80, y, f'{ip} - {host_name}')
        y -= 20
    c.save()

# Scanner le réseau pour les hôtes actifs
def scan_network(local_ip):
    network = '.'.join(local_ip.split('.')[:3]) + '.0/24'
    net = ipaddress.ip_network(network, strict=False)
    active_hosts = []
    threads = []

    for ip in net.hosts():
        thread = threading.Thread(target=scan_ip, args=(ip, active_hosts))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return active_hosts

# Exécuter le script
if __name__ == '__main__':
    local_ip = get_local_ip()
    print(f"Adresse IP locale: {local_ip}")
    print("Scan du réseau en cours...")
    hosts = scan_network(local_ip)
    print("Hôtes actifs trouvés :")
    for ip, host_name in hosts:
        print(f"{ip} ({host_name})")
    create_pdf(hosts)
    print("Les résultats du scan ont été sauvegardés dans 'resultats_reseau.pdf'")
