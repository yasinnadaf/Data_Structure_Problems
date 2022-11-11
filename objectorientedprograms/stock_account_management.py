class Stock:
    def __init__(self, stock_list):
        self.data = stock_list


    def show_details(self, name, share_quantity, share_price,total_price):
         print(f'{name:<20}{share_quantity:<20}{share_price:<20}{total_price:<20}')

    def show_all(self):
        self.show_details(name='name', share_quantity='share_quantity', share_price='share_price', total_price='total_price')

        for i in self.data:
            # print(i)
            self.show_details(name=i.get('name'),share_quantity=i.get('share_quantity'),share_price=i.get('share_price'), total_price=i.get('total_price'))


if __name__ == '__main__':
    stock_list =  [
        {
            'name': 'TataSteel',
            'share_quantity': 450,
            'share_price': 300,
            'total_price': 300*450
        },
        {
            'name': 'Dmart',
            'share_quantity': 800,
            'share_price': 250,
            'total_price': 250*800
        },
        {
            'name': 'Amazon',
            'share_quantity': 600,
            'share_price': 1000,
            'total_price': 1000*600
        }
    ]
    obj = Stock(stock_list)
    obj.show_all()






