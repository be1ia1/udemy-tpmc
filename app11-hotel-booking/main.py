import pandas as pd


df = pd.read_csv('hotels.csv')
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)

class Hotel:
    def __init__(self, hotel_id) -> None:
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()
    
    def view(self):
        pass
    
    def available(self):
        availability =  df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        return availability == 'yes'

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

class Spa(Hotel):
    pass

class ReservationSpa:
    def __init__(self, name, hotel) -> None:
        self.name = name
        self.hotel = hotel

    def generate(self):
        content = f"""
Thank you for your SPA reservation!
Here are you SPA booking data:
Name: {self.name}
Hotel ID: {self.hotel.hotel_id}
Hotel name: {self.hotel.hotel_name}
"""
        return content

class ReservationTicket:
    def __init__(self, name, hotel) -> None:
        self.name = name
        self.hotel = hotel

    def generate(self):
        content = f"""
Thank you for your reservation!
Here are you booking data:
Name: {self.name}
Hotel ID: {self.hotel.hotel_id}
Hotel name: {self.hotel.hotel_name}
"""
        return content

class CreditCard:
    def __init__(self, number) -> None:
        self.number = number
    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number,
                     'expiration': expiration,
                     'holder': holder,
                     'cvc': cvc}
        return card_data in df_cards

class SecureCreditCard(CreditCard):
    def authenticate(self, user_password):
        password = df_cards_security.loc[df_cards_security['number'] == self.number, 'password'].squeeze()
        return password == user_password


if __name__ == "__main__":
    print(df)
    hotel_id = int(input('Enter the id of the hotel: '))
    hotel = Hotel(hotel_id)
    print(hotel.available())
    if hotel.available():
        credit_card = SecureCreditCard(number = '1234567890123456')
        if credit_card.validate(expiration='12/26',
                                holder='JOHN SMITH',
                                cvc='123'):
            if credit_card.authenticate(user_password='mypass'):
                hotel.book()
                name = input('Enter your name: ')
                reservation_ticket = ReservationTicket(name, hotel)
                print(reservation_ticket.generate())
                spa_answer = 'yes'
                if spa_answer == 'yes':
                    spa = Spa(hotel_id)
                    spa_ticket = ReservationSpa(name, hotel)
                    print(spa_ticket.generate())


    else:
        print('Hotel is not free..')