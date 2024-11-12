class Holiday:
    def __init__(self, location, country, price, date):
        self.location = location
        self.country = country
        self.price = price
        self.date = date

    def print_info(self):
        print('This is a', self.location, 'in', self.country, 'on', self.date, 'for', self.price)

    def sort_price(self):
        return sorted(self.price)

class Foreign_holiday(Holiday):
    def __init__(self, location, country, price, date, visa):
        super().__init__(location, country, price, date)
        self.visa = visa
class European_holiday(Holiday):
    def __init__(self, location, country, price, date):
        super().__init__(location, country, price, date)