import ssl
import mechanize
from bs4 import BeautifulSoup
br = mechanize.Browser()

tin = raw_input('Enter tin number:')

br.open('http://mahavat.gov.in/Tin_Search/Tinsearch.jsp')
br.select_form('f1')
br.form['tin'] = tin
req = br.submit()

url = 'http://mahavat.gov.in/Tin_Search/Tin_display?tinnumber='+tin
r = br.open(url)
page=r.read()
page
soup = BeautifulSoup(page,'lxml')
l=soup.find_all("td",class_="head")
x=len(l)
i=0
while i<x:
    print(l[i].text+' : '+l[i+1].text)
    i=i+2
