#This code to convert pdf to binary numbers


import os
import base64
import pyperclip

pdf_path=os.path.join(os.getcwd(),"Sale report-1.pdf")

with open(pdf_path,"rb") as pdf_file:
    pdf_data=pdf_file.read()

base64_pdf=base64.b64encode(pdf_data)
base64_str=base64_pdf.decode("utf-8")

pyperclip.copy(base64_str)


