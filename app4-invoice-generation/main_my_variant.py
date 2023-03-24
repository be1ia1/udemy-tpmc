import glob
# import os
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    # rename headers
    df = df.rename(columns={'product_id': 'Product ID', 'product_name': 'Product Name',
                            'amount_purchased': 'Amount', 'price_per_unit': 'Price per Unit',
                            'total_price': 'Total Price'})
    # get invoice number and date
    ## invoice_number = (os.path.basename(filepath)).split('-')[0]
    filename = Path(filepath).stem
    invoice_number, invoice_date = filename.split('-')
    ## invoice_date = (os.path.basename(filepath)).split('-')[1][:-5]
    # add row with calculated total price 
    empty_cells = df.shape[1] - 1
    total_row = ['' for x in range(empty_cells)]
    total_row.append(df['Total Price'].sum())
    df.loc[len(df.index)] = total_row
    # start creating pdf document
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='b')
    pdf.cell(w=50, h=8, ln=1, txt=f'Invoice nr. {invoice_number}')
    pdf.cell(w=50, h=8, ln=1, txt=f'Date {invoice_date}')
    pdf.ln()

    top = pdf.y
    offset = pdf.x 

    # Table Header
    pdf.set_font('Arial', 'B', 12)
    for header in df:
        cell_w = 70 if header == 'Product Name' else 30
        pdf.multi_cell(w=cell_w, h=10, txt=header, border=1, align='L')
        pdf.y = top
        offset += cell_w
        pdf.x = offset
    # Table content
    data_count = len([x for x in df.values if x[0]])
    # print(data_count)
    pdf.set_font('Arial', '', 10)
    for row in df.values[:data_count]:
        pdf.y += 10 
        pdf.x = 10
        top = pdf.y
        offset = pdf.x 
        for item in row:
            cell_w = 70 if len(str(item)) >= 8 else 30
            pdf.multi_cell(w=cell_w, h=10, txt=str(item), border=1, align='L')
            pdf.y = top
            offset += cell_w
            pdf.x = offset
    # Table footer
    pdf.y += 10 
    pdf.x = 10
    top = pdf.y
    offset = pdf.x 
    for index, row in enumerate(df.values[data_count]):
        cell_w = 70 if index == 1 else 30
        pdf.multi_cell(w=cell_w, h=10, txt=str(row), border=1, align='L')
        pdf.y = top
        offset += cell_w
        pdf.x = offset
    pdf.ln(20)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(w=190, h=10, ln=1, txt=f'The total due amount is {df["Total Price"].sum()} Euros.')
    pdf.cell(w=190, h=10, ln=1, txt=f'PythonHow')
    pdf.output(f'{invoice_number}-{invoice_date}.pdf')