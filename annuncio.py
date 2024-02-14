import re
from datetime import date


class Annuncio:
    def __init__(self, make="", model = "", price = 0, km = 0, link = "", year = 0, fuel = "", region = "", type = ""):
        self.make = make
        self.model = model
        self.price = Annuncio.numberReturn(price)
        self.km = Annuncio.numberReturn(km)
        self.link = "https://www.autoscout24.it/"+link
        self.year = int(Annuncio.yearFormatter(year))
        self.fuel = Annuncio.fuelType(fuel)
        self.region = Annuncio.countryCode(region)
        self.score = 0 #Annuncio.scoreCalculator(self.price, self.km, self.year)
        self.type = type
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
        convenience_score = (0.6 * price) + (0.2*(1/km)) + (0.2 * (1/year))
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
    
    @staticmethod
    def fuelType(fuel):
        match fuel:
            case 'b':
                return "Benzina"
            case 'd':
                return "Diesel"
            case 'm':
                return "Etanolo"
            case 'e':
                return "Elettrico"
            case 'h':
                return "Idrogeno"
            case 'l':
                return "GPL"
            case 'c':
                return "Metano"
            case '2':
                return "Elettrica/Benzina"
            case '3':
                return "Elettrica/Diesel"
            case 'o':
                return "Altro"
        return "Unknow"
    
    @staticmethod
    def countryCode(country):
        match country:
            case 'i':
                return "Italia"
            case 'd':
                return "Germania"
            case 'a':
                return "Austria"
            case 'b':
                return "Belgio"
            case 'e':
                return "Spagna"
            case 'f':
                return "Francia"
            case 'l':
                return "Lussemburgo"
            case 'nl':
                return "Olanda"
        return "Unknow"
