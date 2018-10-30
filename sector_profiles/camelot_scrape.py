# module imports
import camelot
from os import listdir

curr_dir = "."
pdf_suffix = ".pdf"
csv_suffix = ".csv"
sheets_dir = "../camelot_scrape/"
pages_to_pull = "1"

# get the pdf file names
pdfs = [f for f in listdir(curr_dir) if f.endswith(pdf_suffix)]

for pdf in pdfs:
    # print pdf # # debug
    # read in the sheet
    tables = camelot.read_pdf(pdf, pages=pages_to_pull, flavor='stream')
    # export sheets
    tables.export(sheets_dir + pdf.rstrip(pdf_suffix) + csv_suffix, f="csv")

print "done"
