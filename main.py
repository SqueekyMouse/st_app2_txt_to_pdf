import glob
from pathlib import Path
from fpdf import FPDF
## commit: multiline cell and code refactor Sec26

pdf=FPDF(orientation='P',unit='mm',format='A4')

# get file list
filepaths=glob.glob('data/*.txt')
# print(filepaths)

for filename in filepaths:
    # topic=Path(filename).stem.capitalize() #this dense and not recommeneded by zen of Py!!
    fname=Path(filename).stem # not dense, recomended by zen of Py!!
    topic=fname.capitalize() # not dense, recomended by zen of Py!!
    # print(topic)

    # add page
    pdf.add_page()

    # add heading
    pdf.set_font(family='Times',size=22,style='B')
    pdf.cell(w=0,h=22,txt=topic,ln=1)

    # get content of each file
    with open(filename,'r') as file:
        content=file.read()
    
    # add content to pdf body
    pdf.set_font(family='Times',size=14)
    pdf.multi_cell(w=0,h=6,txt=content)

# save pdf file
pdf.output(f'pdfs/doc.pdf')
