import fitz
import os

class PDFMerger:
    def __init__(self, cover_pdf):
        self.cover_pdf = cover_pdf  # Page de couverture constante

    def merge_pdfs(self, pdfs):
        result = fitz.open()
        pdfs_to_merge = [self.cover_pdf] + pdfs

        for pdf in pdfs_to_merge:
            with fitz.open(pdf) as mfile:
                result.insert_pdf(mfile)

        result.save('Resultat_Finaux.pdf')

        for pdf in pdfs:
            if pdf != self.cover_pdf:
                os.remove(pdf)

        print("Fusion terminée et fichiers d'origine supprimés, sauf la page de couverture.")

def main():
    pdfs = ['resultats_reseaux.pdf', 'scan_result.pdf']  # List of PDFs to merge excluding cover page
    cover_pdf = 'Page de couverture.pdf'
    merger = PDFMerger(cover_pdf)
    merger.merge_pdfs(pdfs)

if __name__ == '__main__':
    main()
