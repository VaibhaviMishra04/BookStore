#Importing important Libraries
import urllib.request as ur
from bs4 import BeautifulSoup as BSoup
import os

#Working on Flipkart
base_url = "https://www.flipkart.com"

#Opening title page 
html = ur.urlopen(base_url+"/theliterature-fiction-store").read()
soup = BSoup(html, 'html.parser')

#Extracting all genre
list1 = list(map(lambda x: [x.a.get('href'),x.a.div.img.get('alt')],soup.find_all('div',{'class':'NYE9b8 col col-4-12'})))

#Giving users option to choose a genre of his choice
t=1
for i in list1:
    print(str(t),i[1])
    t+=1

#Taking input from the user
genre = input("\n\nEnter the serial number of Genre of your choice:\n   >> ")

#Opening the home page of that genre
html = ur.urlopen(base_url+list1[int(genre)-1][0]).read()
soup = BSoup(html, 'html.parser')

#Printing Variety of Books
list1 = soup.find_all('div',{'class':'_3liAhj _1R0K0g'})
t=1
print()
for i in list1:
    name = i.find('a',{'class':'_2cLu-l'}).get('title')
    #link = i.find('a',{'class':'_2cLu-l'}).get('href')
    try:
        rating = i.find('div',{'class':'hGSR34'}).get_text()+'/5.00'
    except:
        rating = 'Not Rated'
    price = i.find('div',{'class':'_1vC4OE'}).get_text()
    print(str(t)+' '+name+'\n   Rating:'+rating+'\tPrice: '+price)
    t+=1

#Taking input from the user
book = input("\n\nEnter the serial number of Book:\n   >> ")

#Extracting the link of the book
link = list1[int(book)-1].find('a',{'class':'_2cLu-l'}).get('href')

#Printing the link
print("\n----------\nFollowing is the link to the Book:\n"+base_url+link+"\n----------\n")
