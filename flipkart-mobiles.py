from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('https://www.flipkart.com/search?q=mobiles&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY')
#response = urlopen('https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D2000')


#print(len(mobiles))

counter = 1

while True:
    html = BeautifulSoup( response , 'lxml' )
    mobiles = html.find_all( 'a' ,class_ = '_31qSD5' )
    for mobile in mobiles:
        print(mobile.find('div', class_ = '_3wU53n').text)
        rating = mobile.find('div', class_ = 'hGSR34')
        reviews = mobile.find('span', class_ ='_38sUEc')
        print(rating.text, reviews.text) if rating != None else print('Rating/reviews not available!')
        specs = mobile.find_all('li', class_ = 'tVe95H')
        for i in range(len(specs)):
            print(f"{i+1}. {specs[i].text}")
        print(mobile.find('div', class_ = '_1vC4OE').text)
        print(mobile.find('div', class_ = '_3auQ3N').text)
        print(mobile.find('div', class_ = 'VGWI6T').text)
        exchangeOffer = mobile.find_all('div', class_ = '_2nE8_R')
        print(exchangeOffer[-1].text) if len(exchangeOffer) != 0 else print('Exchange not available!')
        print()
    choice = input("Want to see more mobiles(y/n): ")
    if choice == 'y':
        nextPage = html.find_all('a', class_ = '_2Xp0TH')[counter]
        counter += 1
        url = 'https://flipkart.com' + nextPage['href']
        response = urlopen(url)
        print(url)
    else:
        break