import pandas as pd
from fpdf import FPDF

import glob
from pathlib import Path

filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split('-')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='b')
    pdf.cell(w=50, h=10, txt=f'Invoice nr. {invoice_nr}', ln=1)
    pdf.cell(w=50, h=10, txt=f'Date {invoice_date}', ln=1)

    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    df = df.rename(columns={'product_id': 'Product ID', 'product_name': 'Product Name',
                            'amount_purchased': 'Amount', 'price_per_unit': 'Price per Unit',
                            'total_price': 'Total Price'})
    
    # Add footer to df
    empty_cells = df.shape[1] - 1
    total_row = ['' for x in range(empty_cells)]
    total_price = df['Total Price'].sum()
    total_row.append(total_price)
    df.loc[len(df.index)] = total_row

    # Table header
    pdf.set_font(family='Times', style='b', size=14)
    columns = df.columns
    pdf.cell(w=30, h=10, txt=columns[0], border=1)
    pdf.cell(w=70, h=10, txt=columns[1], border=1)
    pdf.cell(w=30, h=10, txt=columns[2], border=1)
    pdf.cell(w=30, h=10, txt=columns[3], border=1)
    pdf.cell(w=30, h=10, txt=columns[4], ln=1, border=1)

    # Table content
    pdf.set_font(family='Times', size=12)
    for index, row in df.iterrows():
        
        pdf.cell(w=30, h=10, border=1, txt=str(row['Product ID']))
        pdf.cell(w=70, h=10, border=1, txt=str(row['Product Name']))
        pdf.cell(w=30, h=10, border=1, txt=str(row['Amount']))
        pdf.cell(w=30, h=10, border=1, txt=str(row['Price per Unit']))
        pdf.cell(w=30, h=10, border=1, txt=str(row['Total Price']), ln=1)

    pdf.set_font(family='Times', style='b', size=14)
    pdf.cell(w=30, h=8, txt=f'The total price is {total_price}', ln=1)
    pdf.cell(w=25, h=8, txt='PythonHow')
    pdf.image(w=10, name='pythonhow.png')
    pdf.output(f'{invoice_nr}-{invoice_date}.pdf')


# print(filepaths)

