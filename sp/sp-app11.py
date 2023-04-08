import pandas as pd
from fpdf import FPDF


df = pd.read_csv('articles.csv')

class Article:
    def __init__(self, article_id) -> None:
        self.article_id = article_id
        self.name = df.loc[df['id'] == self.article_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.article_id, 'price'].squeeze()
        self.instock = df.loc[df['id'] == self.article_id, 'in stock'].squeeze()
        
    def buy(self):
        instock = self.instock - 1
        df.loc[df['id'] == self.article_id, 'in stock'] = instock
        df.to_csv('articles.csv', index=False)

class Receipt:
    def __init__(self, article) -> None:
        self.article = article

    def generate_receipt(self):
        pdf = FPDF(orientation='P', unit='mm', format='A5')
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.article_id}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name.title()}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)
        pdf.output("receipt.pdf")


if __name__ == '__main__':
    print(df)
    article_id = int(input('Choose an article to buy: '))
    article = Article(article_id)
    article.buy()
    receipt = Receipt(article)
    receipt.generate_receipt()
