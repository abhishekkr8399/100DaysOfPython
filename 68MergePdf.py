#|----------------------------------------------------------------|
#|Description    :    Merge PDF Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
from PyPDF2 import PdfWriter
import os
files=[file for file in os.listdir() if file.endswith(".pdf")]

merger=PdfWriter()
for pdf in files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
