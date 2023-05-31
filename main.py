import csv,requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
pagenum=1
url=f"https://quotes.toscrape.com/page/{pagenum}/"


with open("quotes.csv","w", newline="\n") as file:
    csv_file=csv.writer(file)
    for _ in range(10):
        url=f"https://quotes.toscrape.com/page/{pagenum}/"
        res=requests.get(url)
        htmltext=res.text
        pagesoup=BeautifulSoup(htmltext, 'html.parser')
        listsoup=pagesoup.find_all('div', class_="row")[1]
        listsoup=listsoup.find('div',class_="col-md-8")
        quotesList=listsoup.find_all('div', class_="quote")
        print(url)
        for elem in quotesList:
            row=text,author=elem.find('span', class_="text").text.replace("“","").replace("”",""),elem.find("small",class_="author").text
            print(row)
            csv_file.writerow(row)
        
        pagenum+=1
        sleep(randint(15,20))