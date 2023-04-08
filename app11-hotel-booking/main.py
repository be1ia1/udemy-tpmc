import pandas as pd


df = pd.read_csv('hotels.csv')


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

if __name__ == "__main__":
    print(df)
    hotel_id = int(input('Enter the id of the hotel: '))
    hotel = Hotel(hotel_id)
    print(hotel.available())
    if hotel.available:
        hotel.book()
        name = input('Enter your name: ')
        reservation_ticket = ReservationTicket(name, hotel)
        print(reservation_ticket.generate())
    else:
        print('Hotel is not free..')