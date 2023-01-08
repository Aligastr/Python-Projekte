from PyPDF2 import PdfFileMerger
import os

source_dir = os.getcwd()
merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith("pdf"):
        merger.append(item)
merger.write("combined.pdf") #Pfad wo es geschrieben wird
merger.close()