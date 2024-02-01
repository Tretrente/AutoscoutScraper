import re


class Annuncio:
    def __init__(self, make="", model = "", price = 0, km = 0, link = "", year = 0):
        self.make = make
        self.model = model
        self.price = Annuncio.numberReturn(price)
        self.km = Annuncio.numberReturn(km)
        self.link = "https://www.autoscout24.it/"+link
        self.year = year

    @staticmethod
    def numberReturn(input_string):
        clean_string = re.sub(r'[^0-9]', '', input_string)
        if len(clean_string.strip()) == 0:
            return 0
        else:
            return int(clean_string)
