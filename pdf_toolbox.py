import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

def generate_pdf(output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawString(100, 750, "Ceci est un PDF sécurisé.")
    c.save()

def encrypt_pdf(input_filename, output_filename, password):
    with open(input_filename, "rb") as infile:
        reader = PdfReader(infile)
        writer = PdfWriter()

        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

        writer.encrypt(password)

        with open(output_filename, "wb") as outfile:
            writer.write(outfile)

def merge_pdfs(pdf_files, output_filename):
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])

    with open(output_filename, "wb") as outfile:
        writer.write(outfile)

def select_files():
    filetypes = [("PDF files", "*.pdf")]
    filenames = filedialog.askopenfilenames(title="Sélectionnez des fichiers PDF", filetypes=filetypes)
    if filenames:
        selected_files.extend(filenames)
        files_label.config(text="\n".join(selected_files))

def generate_merge_and_encrypt_pdf():
    if not selected_files:
        output_label.config(text="Aucun fichier sélectionné.")
        return

    merged_filename = "fusionne_temp.pdf"
    password = password_entry.get()

    # Merge the selected PDF files
    merge_pdfs(selected_files, merged_filename)

    # Ask the user where to save the final encrypted PDF
    output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_filename:
        # Encrypt the merged PDF
        encrypt_pdf(merged_filename, output_filename, password)
        output_label.config(text="PDF fusionné et chiffré généré avec succès.")

# Interface utilisateur Tkinter
root = tk.Tk()
root.title("Générateur de PDF Chiffré et Fusionné")

selected_files = []

select_files_button = tk.Button(root, text="Sélectionner des fichiers PDF", command=select_files)
select_files_button.pack()

files_label = tk.Label(root, text="Aucun fichier sélectionné.")
files_label.pack()

password_label = tk.Label(root, text="Mot de passe de chiffrement :")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

generate_button = tk.Button(root, text="Fusionner et chiffrer PDF", command=generate_merge_and_encrypt_pdf)
generate_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
