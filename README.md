Qu'est-ce que ToolBox par Rachid ?
ToolBox par Rachid est un outil de cybersécurité polyvalent et puissant qui vous aide dans diverses tâches de sécurité. Il dispose d'une interface conviviale et offre une gamme de fonctionnalités telles que le scan de réseau, la gestion des mots de passe, les simulations d'attaques par force brute et la manipulation de fichiers PDF.

Que faut-il pour l'utiliser ?
Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre ordinateur :

Python 3.x : Le langage de programmation principal pour l'outil.
pip : Un gestionnaire de paquets pour installer des bibliothèques Python.
Pillow : Pour le traitement d'images.
nmap : Un outil pour le scan de réseau.
paramiko : Pour les connexions SSH.
reportlab : Pour créer des fichiers PDF.
PyPDF2 : Pour manipuler les fichiers PDF.
fitz (PyMuPDF) : Pour travailler avec des documents PDF.

Comment utiliser ToolBox par Rachid
Télécharger ou Cloner le Dépôt : Obtenez le code de ToolBox par Rachid sur votre machine locale.

Naviguer vers le Répertoire : Ouvrez votre terminal et allez dans le dossier où se trouvent les fichiers de ToolBox.

Lancer l'Application : Démarrez l'application en exécutant le script principal avec :

main.py

Interface Utilisateur
La fenêtre principale comporte des boutons pour chaque tâche et une zone pour afficher des images. Il y a également des champs de saisie et des contrôles pour des opérations détaillées.

Fonctionnalités Clés
Opérations Réseau
Scan de Réseaux : Trouvez des machine actifs sur votre réseau et obtenez un rapport PDF.
Comment : Cliquez sur "Scan Reseaux" pour voir les hôtes actifs et enregistrer les résultats en PDF.
Scan de Ports et Vulnérabilités : Vérifiez les ports ouverts et les vulnérabilités potentielles sur une adresse IP spécifique et genere un PDF.
Comment : Cliquez sur "Scan de Port et Vulnérabilité", entrez l'adresse IP et lancez le scan.
Gestion des Mots de Passe
Test de Solidité des Mots de Passe : Vérifiez la force et la complexité d'un mot de passe.
Comment : Cliquez sur "Test des solidité du mots de passe", entrez le mot de passe et voyez les résultats.
Chiffrement des Mots de Passe : Créez des hachages MD5, SHA-1 et SHA-256 pour les mots de passe.
Comment : Cliquez sur "Chiffrement Mot de passe", entrez le mot de passe et voyez les hachages générés.
Déchiffrement des Mots de Passe : Essayez de cracker des mots de passe hachés en utilisant une attaque par dictionnaire.
Comment : Cliquez sur "Dechiffrement de Mot de passe", fournissez le hachage et un fichier dictionnaire, et lancez le processus.
Attaques par Force Brute
Brute Force SSH : Simulez une attaque par force brute sur un serveur SSH.
Comment : Cliquez sur "Brute force SSH", entrez l'adresse IP, le nom d'utilisateur et la liste des mots de passe, et lancez l'attaque.
Brute Force RDP : Simulez une attaque par force brute sur un serveur Remote Desktop Protocol (RDP).
Comment : Cliquez sur "Brute force RDP", entrez l'adresse IP, le nom d'utilisateur et la liste des mots de passe, et initiez l'attaque.
Outils PDF
Fusion de PDF : Combinez plusieurs fichiers PDF en un seul document.
Comment : Cliquez sur "PDF fusion", sélectionnez les fichiers PDF et effectuez la fusion.
Chiffrement de PDF : Chiffrez un fichier PDF fusionné avec un mot de passe.
Comment : Cliquez sur "PDF chiffrement", sélectionnez les fichiers PDF, entrez le mot de passe et générez le PDF chiffré.
Comment Exécuter les Tâches
Exécuter le Script : Utilisez les boutons de l'interface graphique pour lancer des tâches spécifiques.
Charger les Fichiers : Pour les tâches nécessitant des fichiers d'entrée (comme des listes de mots de passe ou des fichiers PDF), utilisez la boîte de dialogue pour sélectionner les fichiers appropriés.
Voir les Résultats : Les résultats des scans, des tests de mots de passe et des attaques seront affichés dans l'interface graphique et/ou enregistrés dans des fichiers.
Fonctionnalités Supplémentaires
Journalisation en Temps Réel : L'outil journalise les tâches en temps réel dans l'interface graphique, vous aidant à suivre la progression et les résultats.
Multi-Threading : Il utilise le multi-threading pour exécuter les tâches plus rapidement et plus efficacement.
Rappels Importants
Utilisation Légale et Éthique : Assurez-vous d'obtenir l'autorisation appropriée avant de réaliser des tests de sécurité pour éviter tout problème légal.
Maintenance : Gardez l'outil et ses dépendances à jour pour assurer la compatibilité et la sécurité.
Crédits
Développé par Rachid.

What is ToolBox by Rachid?
ToolBox by Rachid is a versatile and powerful cybersecurity tool that helps you with various security tasks. It has a user-friendly interface and offers a range of features such as network scanning, password management, brute force attack simulations, and PDF manipulation.

What Do You Need to Use It?
Before you start, make sure you have these installed on your computer:

Python 3.x: The main programming language for the tool.
pip: A package manager for installing Python libraries.
Pillow: For image processing.
nmap: A tool for network scanning.
paramiko: For SSH connections.
reportlab: For creating PDFs.
PyPDF2: For handling PDF files.
fitz (PyMuPDF): For working with PDF documents.


How to Use ToolBox by Rachid
Download or Clone the Repository: Get the ToolBox by Rachid code on your local machine.

Navigate to the Directory: Open your terminal and go to the folder where you have the ToolBox files.

Run the Application: Start the application by running the main script with:


python main.py
User Interface
The main window has buttons for each task and an area to show images. There are also input fields and controls for detailed operations.

Key Features
Network Operations
Scan Networks: Find active devices on your network and get a PDF report.
How: Click "Scan Reseaux" to see active hosts and save results as a PDF.
Port and Vulnerability Scan: Check open ports and potential vulnerabilities on a specific IP address.
How: Click "Scan de Port et Vulnerabilité", enter the IP address, and start the scan.
Password Management
Password Strength Test: Check how strong and complex a password is.
How: Click "Test des solidité du mots de passe", enter the password, and see the results.
Password Encryption: Create MD5, SHA-1, and SHA-256 hashes for passwords.
How: Click "Chiffrement Mot de passe", enter the password, and view the hashes.
Password Decryption: Try to crack hashed passwords using a dictionary attack.
How: Click "Dechiffrement de Mot de passe", provide the hash and a dictionary file, and start the process.
Brute Force Attacks
SSH Brute Force: Simulate a brute force attack on an SSH server.
How: Click "Brute force SSH", enter the IP, username, and password list, and start the attack.
RDP Brute Force: Simulate a brute force attack on a Remote Desktop Protocol server.
How: Click "Brute force RDP", enter the IP, username, and password list, and initiate the attack.
PDF Tools
PDF Merge: Combine multiple PDF files into one.
How: Click "PDF fusion", select the PDF files, and merge them.
PDF Encryption: Encrypt a merged PDF with a password.
How: Click "PDF chiffrement", select the PDFs, enter the password, and generate the encrypted PDF.
How to Execute Tasks
Run Script: Use the GUI buttons to run specific tasks.
Load Files: For tasks needing file inputs (like password lists or PDFs), use the file dialog to select files.
View Results: Results from scans, password tests, and attacks will show in the GUI and/or be saved to files.
Extra Features
Real-Time Logging: The tool logs tasks in real-time within the GUI, helping you monitor progress and results.
Multi-Threading: It uses multi-threading to make tasks run faster and more efficiently.
Important Reminders
Legal and Ethical Use: Always get proper authorization before running security tests to avoid legal issues.
Maintenance: Keep the tool and its dependencies updated for compatibility and security.
Credits
Developed by Rachid.