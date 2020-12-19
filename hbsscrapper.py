from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://hbswk.hbs.edu/Pages/browse.aspx?HBSTopic=Finance').text
soup = BeautifulSoup(source,'lxml')
my_file_handle=open('maal.csv','w')
csv_writer = csv.writer(my_file_handle)
csv_writer.writerow(['headlines','authors','summary'])
for article in soup.find_all('div',class_='highlight-container'):
    authors = article.div.text
    headline=article.h4.a.text
    summary = article.p.text
    print(summary)
    print(authors)
    print(headline)
    csv_writer.writerow([headline,authors,summary])
    
my_file_handle.close()