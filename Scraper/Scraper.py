from bs4 import BeautifulSoup
import urllib.request
import csv

class Scraper:
    
    def Scrape(self):
        #Get the url and then read the data on that url
        baseurl = "http://money.cnn.com/data/premarket/?iid=H_MKT_QL"
        url = urllib.request.urlopen(baseurl).read()

        #pass the data to a beautiful soup object
        soup = BeautifulSoup(url)

        #find the correct table and its descendants
        tables = soup.find_all("table", attrs={"class": "wsod_dataTable wsod_dataTableBig"})
        symbols = soup.find_all("a", attrs={"class": "wsod_symbol"})
        children = tables[0].find_all("td", attrs={"class": "wsod_aRight"})

        #open the output file and write the data from the table to the file
        with open("Scraper_Output.csv", "w", newline = '') as csvfile:
            outputwriter = csv.writer(csvfile)
            counter = 0
            for symbol in symbols:
                if any(symbol):
                    if "symb" in str(symbol.get('href')):
                        ticker = symbol.contents[0]
                        price = children[counter].get_text()
                        counter += 1
                        change = children[counter].get_text()
                        change = change.replace("%", "")
                        outputwriter.writerow([ticker] + [price] + [change])
                        counter += 2


X = Scraper()
X.Scrape()
