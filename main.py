from collections import defaultdict
import bs4, requests, webbrowser
from annuncio import Annuncio

totalResults=0
annunci = []

#Create the link for the search page
#TODO implement more search filter
def linkCreator(make, model, page):
    BASE_LINK = "https://www.autoscout24.it/lst/"+make+"/"+model+"?atype=C&cy=I&desc=0&page="+str(page)+"&sort=standard&source=homepage_search-mask&ustate=N%2CU"
    return BASE_LINK

#Take the article in the page and pass it to the list population method
def pageResearch(soup):
    #Looking for the list in the html of the page
    div_annunci=soup.find('main', class_='ListPage_main___0g2X')#Html object, html class
    article_annunci = div_annunci.find_all('article', class_='cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__qyYw7') #Extraction of all cars of the page
    annunci = listPopulation(article_annunci)
    #printList(annunci)
    #return annunci

#Populate the list with all the announcements
def listPopulation(page):
    global annunci
    for articolo in page:
        marca = str(articolo.get('data-make'))
        modello = str(articolo.get('data-model'))
        prezzo = str(articolo.get('data-price'))
        km = str(articolo.get('data-mileage'))
        link = str((articolo.find('a', class_='ListItem_title__ndA4s ListItem_title_new_design__QIU2b Link_link__Ajn7I')).get('href'))
        anno = str(articolo.get('data-first-registration'))
        car = Annuncio(marca, modello, prezzo, km, link, anno)
        annunci.append(car)
    return annunci

#Print the list
#TODO print fuel type and country also
def printList(annunci):
    global totalResults
    totalResults += len(annunci)
    for annuncio in annunci:
        print("----------------------------------")
        print("prezzo = " + str(annuncio.price))
        print("marca = " + annuncio.make)
        print("modello = " + annuncio.model)
        print("km = " + str(annuncio.km))
        print("anno = "+ annuncio.year)
        print("link = " + annuncio.link)
        print("----------------------------------")

#Calculates how many pages are avabile for the search you made
def pageCalculator(soup):
    pageNavigator = soup.find('div', class_='ListPage_pagination__4Vw9q')
    pageNumbers = pageNavigator.find_all('li', class_='pagination-item')
    number_of_page = 0
    for n in pageNumbers:
        page = int(n.get_text())
        if  page> number_of_page:
            number_of_page = page
    return number_of_page

#Make the call to the link and check if the response is correct. Returns the suop with the hrml code
def linkCall(link):
    response = requests.get(link)
    response.raise_for_status()
    soup=bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

#Compare the cars list to find the best km/price car
def listCompare():
    global annunci
    sorted_annuncios = sorted(annunci, key=lambda x: (x.price / x.km if x.km != 0 else float('inf')))
    printList(sorted_annuncios)


#Start the program
#TODO implemente the possibility tho choice wich make and model you want to search for
def start():
    link = linkCreator(make="toyota", model="prius", page=1)
    soup = linkCall(link)
    pages = pageCalculator(soup)
    for n in range(pages+1):
        link = linkCreator(make="toyota", model="prius", page=n)
        soup = linkCall(link)
        pageResearch(soup)
        #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+str(n))
    global totalResults
    listCompare()
    #print (totalResults)

start()

