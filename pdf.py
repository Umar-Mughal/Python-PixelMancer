import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_lists):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_lists:
        print(pdf)
        merger.append(pdf)
    merger.write('pdfs/super.pdf')


pdf_combiner(inputs)

