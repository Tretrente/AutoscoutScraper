import re
from datetime import date


class Annuncio:
    def __init__(self, make="", model = "", price = 0, km = 0, link = "", year = 0):
        self.make = make
        self.model = model
        self.price = Annuncio.numberReturn(price)
        self.km = Annuncio.numberReturn(km)
        self.link = "https://www.autoscout24.it/"+link
        self.year = year
        self.score = Annuncio.scoreCalculator(self.price, self.km, self.year)
        self.category = Annuncio.categorization(self.km)    

    @staticmethod
    def numberReturn(input_string):
        clean_string = re.sub(r'[^0-9]', '', input_string)
        if len(clean_string.strip()) == 0:
            return 1
        elif clean_string == "0":
            return 1
        else:
            return int(clean_string)
    
    @staticmethod 
    def yearFormatter(year):
        current_year = ""
        if year == "new":
            current_year = date.today().year
        else:
            current_year = year[3:7]
        return current_year

#This method will calculate the score. The lower is the score, the better is the car
    @staticmethod 
    def scoreCalculator(price: int, km: int, year):
        year = int(Annuncio.yearFormatter(year))
        price = int(price)
        km = int(km)
        score = (price / 1000) * km * (1 / (year))
        return score
    
    @staticmethod
    def categorization(km):
        category = ""
        if int(km) < 100:
            category = "new"
        else:
            category = "used"
        return category
