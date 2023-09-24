from PyPDF2 import PdfWriter,PdfReader
num=int(input("Enter page number you want to combine from multiple documents:"))
pdf1=open('C:\\Users\\HP\\Downloads\\wepik-the-kingfisher-beak-a-design-inspiration-for-high-speed-bullet-trains-20230830111725NSHb.pdf','rb')
pdf2=open('C:\\Users\\HP\\Downloads\\wepik-plant-burrs-natures-ingenious-hitchhikers-20230901085644wkR3.pdf','rb')

pdf_writer=PdfWriter()

pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num-1]
pdf_writer.add_page(page)

pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num-1]
pdf_writer.add_page(page)

with open('C:\\Users\\HP\\Desktop\\PROGRAMMING\\op.pdf','wb')as output:
    pdf_writer.write(output)

