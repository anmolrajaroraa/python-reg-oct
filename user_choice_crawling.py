Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import urlopen
>>> from bs4 import BeautifulSoup as bs
>>> choice = input("Enter the product name for which you want to see the details: ")
Enter the product name for which you want to see the details: oneplus 7 pro
>>> choice
'oneplus 7 pro'
>>> choice = choice.replace(' ', '%20')
>>> choice
'oneplus%207%20pro'
>>> url = 'https://www.flipkart.com/search?q=' + choice + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
>>> res = urlopen(url)
>>> html = bs(res)
>>> allProducts = html.find_all('div' , class_ = '_3wU53n')
>>> for i in range(len(allProducts)):
	print(f"{i + 1}. {allProducts[i].text}")

	
1. OnePlus 7 Pro (Nebula Blue, 256 GB)
2. OnePlus 7 Pro (Mirror Grey, 128 GB)
3. OnePlus 7 Pro (Mirror Grey, 256 GB)
4. OnePlus 7 Pro (Almond, 256 GB)
>>> productNo = input("Which one: ")
Which one: 2
>>> productNo
'2'
>>> productNo = int(input("Which one: "))
Which one: 2
>>> productNo
2
>>> productNo = productNo - 1
>>> product = allProducts[productNo]
>>> product
<div class="_3wU53n">OnePlus 7 Pro (Mirror Grey, 128 GB)</div>
>>> blocks = html.find_all('a', class_ = '_31qSD5')
>>> selectedBlock = blocks[productNo]
>>> selectedBlock
<a class="_31qSD5" href="/oneplus-7-pro-mirror-grey-128-gb/p/itmbdc9c2e788399?pid=MOBFJJW3NSR3KQS4&amp;srno=s_1_2&amp;otracker=search&amp;otracker1=search&amp;lid=LSTMOBFJJW3NSR3KQS47NNEYU&amp;fm=organic&amp;iid=c91fc0a2-dc26-4d68-877c-d19e5b642788.MOBFJJW3NSR3KQS4.SEARCH&amp;ssid=r36kccdbeo0000001571206107731&amp;qH=430521230d5db8b8" rel="noopener noreferrer" target="_blank"><div class="_3SQWE6"><div class="_1OCn9C"><div style="-webkit-filter:grayscale(1);-moz-filter:grayscale(1);-o-filter:grayscale(1);-ms-filter:grayscale(1);filter:grayscale(1);opacity:0.6"><div class="_3BTv9X" style="height:200px;width:200px"><img alt="OnePlus 7 Pro (Mirror Grey, 128 GB)" class="_1Nyybr" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/placeholder_9951d0.svg"/></div></div><div class="_3aV9Tq"><span class="_1GJ2ZM">Not Deliverable</span></div></div><div class="_2lesQu"><div class="_1O_CiZ"><span class="_1iHA1p"><div class="_2kFyHg"><label><input class="_3uUUD5" readonly="" type="checkbox"/><div class="_1p7h2j"></div></label></div></span><label class="_10TB-Q"><span>Add to Compare</span></label></div></div><div class="_3gDSOa _32A6AP"><div class="DsQ2eg"><svg class="_2oLiqr" height="16" viewbox="0 0 20 16" width="16" xmlns="http://www.w3.org/2000/svg"><path class="_35Y7Yo" d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"></path></svg></div></div></div><div class="_1-2Iqu row"><div class="col col-7-12"><div class="_3wU53n">OnePlus 7 Pro (Mirror Grey, 128 GB)</div><div class="niH0FQ"><span class="_2_KrJI" id="productRating_LSTMOBFJJW3NSR3KQS47NNEYU_MOBFJJW3NSR3KQS4_"><div class="hGSR34">4.9<img class="_2lQ_WZ" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/></div></span><span class="_38sUEc"><span><span>7 Ratings </span><span class="_1VpSqZ">&amp;</span><span> 0 Reviews</span></span></span></div><div class="_3ULzGw"><ul class="vFw0gD"><li class="tVe95H">6 GB RAM | 128 GB ROM |</li><li class="tVe95H">16.94 cm (6.67 inch) Display</li><li class="tVe95H">48 MP + 8 MP + 16 MP | 16MP Front Camera</li><li class="tVe95H">4000 mAh Battery</li><li class="tVe95H">1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories including batteries from the date of purchase</li></ul></div></div><div class="col col-5-12 _2o7WAb"><div class="_6BWGkk"><div class="_1uv9Cb"><div class="_1vC4OE _2rQ-NK">₹48,990</div><div class="_3auQ3N _2GcJzG">₹<!-- -->48,999</div></div></div><div class="_3n6o0t"><img height="21" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/></div></div></div></a>
>>> print(product.text)
OnePlus 7 Pro (Mirror Grey, 128 GB)
>>> print(selectedBlock.find('div',class_='_1vC4OE').text)
₹48,990
>>> print(selectedBlock.find('div',class_='hGSR34').text)
4.9
>>> specs = selectedBlock.find_all('li', class_ = 'tVe95H')
>>> for feature in specs:
	print(feature.text)

	
6 GB RAM | 128 GB ROM |
16.94 cm (6.67 inch) Display
48 MP + 8 MP + 16 MP | 16MP Front Camera
4000 mAh Battery
1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories including batteries from the date of purchase
>>> choice = input("Enter the product name for which you want to see the details: ")
Enter the product name for which you want to see the details: iphone 11 pro
>>> choice = choice.replace(' ', '%20')
>>> url = 'https://www.flipkart.com/search?q=' + choice + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
>>> url
'https://www.flipkart.com/search?q=iphone%2011%20pro&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
>>> res = urlopen(url)
>>> html = bs(res)
>>> allProducts = html.find_all('div' , class_ = '_3wU53n')
>>> for i in range(len(allProducts)):
	print(f"{i + 1}. {allProducts[i].text}")

	
1. Apple iPhone 11 Pro (Space Grey, 256 GB)
2. Apple iPhone 11 Pro (Silver, 256 GB)
3. Apple iPhone 11 Pro (Gold, 256 GB)
4. Apple iPhone 11 Pro (Space Grey, 512 GB)
5. Apple iPhone 11 Pro (Midnight Green, 64 GB)
6. Apple iPhone 11 Pro (Midnight Green, 512 GB)
7. Apple iPhone 11 Pro (Space Grey, 64 GB)
8. Apple iPhone 11 Pro (Silver, 64 GB)
9. Apple iPhone 11 Pro Max (Silver, 512 GB)
10. Apple iPhone 11 Pro (Midnight Green, 256 GB)
11. Apple iPhone 11 Pro (Gold, 64 GB)
12. Apple iPhone 11 Pro Max (Silver, 256 GB)
13. Apple iPhone 11 Pro Max (Midnight Green, 512 GB)
14. Apple iPhone 11 Pro Max (Space Grey, 64 GB)
15. Apple iPhone 11 Pro Max (Silver, 64 GB)
16. Apple iPhone 11 Pro Max (Space Grey, 256 GB)
17. Apple iPhone 11 Pro Max (Gold, 256 GB)
18. Apple iPhone 11 Pro Max (Gold, 64 GB)
19. Apple iPhone 11 Pro Max (Space Grey, 512 GB)
20. Apple iPhone 11 Pro (Gold, 512 GB)
21. Apple iPhone 11 Pro (Silver, 512 GB)
22. Apple iPhone 11 Pro Max (Midnight Green, 256 GB)
23. Apple iPhone 11 Pro Max (Gold, 512 GB)
24. Apple iPhone 11 Pro Max (Midnight Green, 64 GB)
>>> productNo = input("Which one: ")
Which one: 4
>>> productNo = int(input("Which one: "))
Which one: 4
>>> productNo = productNo - 1
>>> product = allProducts[productNo]
>>> product
<div class="_3wU53n">Apple iPhone 11 Pro (Space Grey, 512 GB)</div>
>>> blocks = html.find_all('a', class_ = '_31qSD5')
>>> selectedBlock = blocks[productNo]
>>> print(product.text)
Apple iPhone 11 Pro (Space Grey, 512 GB)
>>> print(selectedBlock.find('div',class_='_1vC4OE').text)
₹1,31,900
>>> print(selectedBlock.find('div',class_='hGSR34').text)
4.7
>>> specs = selectedBlock.find_all('li', class_ = 'tVe95H')
>>> for feature in specs:
	print(feature.text)

	
512 GB ROM |
14.73 cm (5.8 inch) Super Retina XDR Display
12MP + 12MP + 12MP | 12MP Front Camera
A13 Bionic Chip Processor
Brand Warranty for 1 Year
>>> 
