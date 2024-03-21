from PyPDF2 import PdfWriter, PdfReader
n = int(input("Enter page number you want combine from multiple documents "))
p1 = open('BFE MODULE 4.pdf', 'rb')
p2 = open('BFE MODULE 5.pdf', 'rb')
pw = PdfWriter()
pr1 = PdfReader(p1)
p = pr1.pages[n-1]
pw.add_page(p)
pr2 = PdfReader(p2)
p = pr2.pages[n-1]
pw.add_page(p)
with open('op.pdf', 'wb') as o:
    pw.write(o)