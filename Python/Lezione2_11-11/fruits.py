class fruit:
    def __init__(self, name, color):
         self.name = name
         self.color = color
    def print_info(self):
         print('This is a', self.color, self.name)
class tropical_fruit(fruit):
    def __init__(self, name, color, country):
        super().__init__(name, color)
        self.country = country

    def print_info(self):
         print('This is a', self.color, self.name, 'from', self.country)
