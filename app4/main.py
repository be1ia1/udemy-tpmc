import glob
from pathlib import Path
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
filepaths = glob.glob('txt/*.txt')
for filepath in filepaths:
    filename = Path(filepath).stem.capitalize()
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=50, h=8, txt=f'{filename}', ln=1)
    pdf.set_font(family='Times', size=14)
    with open(filepath) as fo:
        text = fo.read()
    pdf.multi_cell(w=190, h=8, txt=text)
pdf.output('output.pdf')