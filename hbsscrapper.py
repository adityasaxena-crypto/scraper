from bs4 import BeautifulSoup
import requests
import csv
my_file_handle=open('hbs.csv','w')
for i in range(27):
  source = requests.get('https://hbswk.hbs.edu/Pages/browse.aspx?HBSTopic=Finance&page=i').text
  soup = BeautifulSoup(source,'lxml')
  
  csv_writer = csv.writer(my_file_handle)
  csv_writer.writerow(['headlines','authors','summary','link'])
  for article in soup.find_all('div',class_='highlight-container'):
      authors = article.div.text
      headline=article.h4.a.text
      summary = article.p.text
      link=article.find('a',class_='hbsred')['href']
      print(summary)
      print(authors)
      print(headline)
      print(link)
      csv_writer.writerow([headline,authors,summary,link])
    
my_file_handle.close()

