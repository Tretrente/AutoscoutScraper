import re
from datetime import date


class Annuncio:
    def __init__(self, make="", model = "", price = 0, km = 0, link = "", year = 0, fuel = "", region = ""):
        self.make = make
        self.model = model
        self.price = Annuncio.numberReturn(price)
        self.km = Annuncio.numberReturn(km)
        self.link = "https://www.autoscout24.it/"+link
        self.year = year
        self.fuel = fuel
        self.region = region
        self.score = Annuncio.scoreCalculator(self.price, self.km, self.year)
        self.category = Annuncio.categorization(self.km)    

#This method return a string with only numbers
    @staticmethod
    def numberReturn(input_string):
        clean_string = re.sub(r'[^0-9]', '', input_string)
        if len(clean_string.strip()) == 0:
            return 1
        elif clean_string == "0":
            return 1
        else:
            return int(clean_string)

#This method format the year to make it contain only numbers    
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
        year_factor = 2024 - year + 1
        #LIVELLO IMPORTANZA:
        #PREZZO: 0.6, 0.3, 0.1
        #KM: 0.4, 0.4, 0.2
        #ANNO: 0.1, 0.1, 0.8
        convenience_score = (0.6 * price) + (0.2*(1/km)) + (0.2 * (1/year))
        #convenience_score = (1 / price) * (2024 - year + 1) * (1 / (km + 1))
        #convenience_score = year_factor / (price * km)
        return convenience_score
        
    
#This method return the category based on the number of km
    @staticmethod
    def categorization(km):
        category = ""
        if int(km) < 100:
            category = "new"
        else:
            category = "used"
        return category
