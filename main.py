import glob
from pathlib import Path
from fpdf import FPDF
## commit: get files, and create pdf with heading and content Sec25

pdf=FPDF(orientation='P',unit='mm',format='A4')

# get file list
filepaths=glob.glob('data/*.txt')
# print(filepaths)

for filename in filepaths:
    topic=Path(filename).stem.capitalize()
    # print(topic)
    with open(filename,'r') as file:
        content=file.read()
    # add page
    pdf.add_page()
    # add heading
    pdf.set_font(family='Times',size=22,style='B')
    pdf.cell(w=0,h=22,txt=topic,ln=1)
    # add body
    # pdf.set_font(family='Times',size=14,style='B')
    pdf.set_font(family='Times',size=14)
    pdf.multi_cell(w=0,h=7,txt=content)

pdf.output(f'pdfs/doc.pdf')
