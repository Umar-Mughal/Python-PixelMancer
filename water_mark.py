import PyPDF2

template = PyPDF2.PdfReader(open('pdfs/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('pdfs/wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)