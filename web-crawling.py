Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import urlopen
>>> urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb%3Amp%3A0951e46510&fm=neo%2Fmerchandising&iid=M_a9e4f155-20a8-467f-9b54-6d4d36a14fac_2.TGGGGB02JCLZ&ssid=93byr922s00000001570693148014&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&cid=TGGGGB02JCLZ&p%5B%5D=facets.brand%255B%255D%3DDaniel%2BKlein')
<http.client.HTTPResponse object at 0x1060501d0>
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> import bs4
>>> response = urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb%3Amp%3A0951e46510&fm=neo%2Fmerchandising&iid=M_a9e4f155-20a8-467f-9b54-6d4d36a14fac_2.TGGGGB02JCLZ&ssid=93byr922s00000001570693148014&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&cid=TGGGGB02JCLZ&p%5B%5D=facets.brand%255B%255D%3DDaniel%2BKlein')
>>> from bs4 import BeautifulSoup as bs
>>> bs(response)

>>> htmlPage = bs(response)
>>> htmlPage.find('div', class='IIdQZO')
SyntaxError: invalid syntax
>>> htmlPage.find('div', class_ = 'IIdQZO')
>>> htmlPage.find('div', class_ = 'IIdQZO')
>>> response = urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&offer=nb%3Amp%3A0951e46510&fm=neo%2Fmerchandising&iid=M_a9e4f155-20a8-467f-9b54-6d4d36a14fac_2.TGGGGB02JCLZ&ssid=93byr922s00000001570693148014&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&cid=TGGGGB02JCLZ&p%5B%5D=facets.brand%255B%255D%3DDaniel%2BKlein')
>>> htmlPage = bs(response)
>>> htmlPage.find('div', class_ = 'IIdQZO')
<div class="IIdQZO _1R0K0g _1SSAGr"><a class="_3dqZjq" href="/daniel-klein-dk11637-5-premium-ladys-analog-watch-women/p/itmf6y7tbm9zkadk?pid=WATF6Y7TEGEUUMH9&amp;lid=LSTWATF6Y7TEGEUUMH9J5UQXJ&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&amp;fm=organic&amp;iid=16f90eeb-ac3a-4df9-95a5-48c87d7cd3b5.WATF6Y7TEGEUUMH9.SEARCH&amp;ssid=s5m5bp18cw0000001570695177383" rel="noopener noreferrer" target="_blank"><div><div><div class="_3JlYXy" style="padding-top:120.00%"><div class="_3ZJShS _31bMyl" style="padding-top:120.00%"><img alt="" class="_3togXc" src=""/></div></div></div></div><div></div><div class="_3gDSOa _2HqUcN _2RN9ef"><div class="DsQ2eg"><svg class="_2oLiqr" height="28" viewbox="0 0 20 16" width="28" xmlns="http://www.w3.org/2000/svg"><path class="_35Y7Yo" d="M8.695 16.682C4.06 12.382 1 9.536 1 6.065 1 3.219 3.178 1 5.95 1c1.566 0 3.069.746 4.05 1.915C10.981 1.745 12.484 1 14.05 1 16.822 1 19 3.22 19 6.065c0 3.471-3.06 6.316-7.695 10.617L10 17.897l-1.305-1.215z" fill="#2874F0" fill-rule="evenodd" opacity=".9" stroke="#FFF"></path></svg></div></div><div class="_2DOcq6"></div></a><div class="_2LFGJH" style="transform:translate3d(0, 0, 0)"><div class="_2B_pmu">Daniel Klein</div><a class="_2mylT6" href="/daniel-klein-dk11637-5-premium-ladys-analog-watch-women/p/itmf6y7tbm9zkadk?pid=WATF6Y7TEGEUUMH9&amp;lid=LSTWATF6Y7TEGEUUMH9J5UQXJ&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&amp;fm=organic&amp;iid=16f90eeb-ac3a-4df9-95a5-48c87d7cd3b5.WATF6Y7TEGEUUMH9.SEARCH&amp;ssid=s5m5bp18cw0000001570695177383" rel="noopener noreferrer" target="_blank" title="DK11637-5 Premium-ladys Analog Watch  - For Women">DK11637-5 Premium-ladys Analog Watch  - For Women</a><div class="_3AqcXr"><img height="18" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/fa_8b4b59.png"/></div><a class="_2W-UZw" href="/daniel-klein-dk11637-5-premium-ladys-analog-watch-women/p/itmf6y7tbm9zkadk?pid=WATF6Y7TEGEUUMH9&amp;lid=LSTWATF6Y7TEGEUUMH9J5UQXJ&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&amp;fm=organic&amp;iid=16f90eeb-ac3a-4df9-95a5-48c87d7cd3b5.WATF6Y7TEGEUUMH9.SEARCH&amp;ssid=s5m5bp18cw0000001570695177383" rel="noopener noreferrer" target="_blank"><div class="_1uv9Cb"><div class="_1vC4OE">₹1,912</div><div class="_3auQ3N">₹<!-- -->4,250</div><div class="VGWI6T"><span>55% off</span></div></div></a></div></div>
>>> watch = htmlPage.find('div', class_ = 'IIdQZO')
>>> watch.find('div', class_ = '_2B_pmu')
<div class="_2B_pmu">Daniel Klein</div>
>>> watch.find('div', class_ = '_2B_pmu').text
'Daniel Klein'
>>> watch.find('a', class_ = '_2mylT6')
<a class="_2mylT6" href="/daniel-klein-dk11637-5-premium-ladys-analog-watch-women/p/itmf6y7tbm9zkadk?pid=WATF6Y7TEGEUUMH9&amp;lid=LSTWATF6Y7TEGEUUMH9J5UQXJ&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&amp;fm=organic&amp;iid=16f90eeb-ac3a-4df9-95a5-48c87d7cd3b5.WATF6Y7TEGEUUMH9.SEARCH&amp;ssid=s5m5bp18cw0000001570695177383" rel="noopener noreferrer" target="_blank" title="DK11637-5 Premium-ladys Analog Watch  - For Women">DK11637-5 Premium-ladys Analog Watch  - For Women</a>
>>> watch.find('a', class_ = '_2mylT6').text
'DK11637-5 Premium-ladys Analog Watch  - For Women'
>>> watch.find('div', class_ = '_1vC4OE').text
'₹1,912'
>>> watch.find('div', class_ = 'VGWI6T').find('span').text
'55% off'
>>> watches = htmlPage.find_all('div', class_ = 'IIdQZO')
>>> len(watches)
40
>>> for watch in watches:
	print(watch.find('div', class_ = '_2B_pmu').text + " " +  watch.find('a', class_ = '_2mylT6').text + " - " + watch.find('div' , class_ = '_1vC4OE').text + " - " + watch.find('div', class_ = 'VGWI6T').find('span').text)

	
Daniel Klein DK11637-5 Premium-ladys Analog Watch  - For Women - ₹1,912 - 55% off
Daniel Klein DK11599-5 Analog Watch  - For Men - ₹2,294 - 55% off
Daniel Klein DK11637-6 Premium-ladys Analog Watch  - For Women - ₹2,099 - 50% off
Daniel Klein DK11914-5 Analog Watch  - For Women - ₹2,062 - 45% off
Daniel Klein DK11328-3 Analog Watch  - For Women - ₹2,575 - 50% off
Daniel Klein DK11407-8 Analog Watch  - For Women - ₹1,768 - 40% off
Daniel Klein DK11328-5 Analog Watch  - For Women - ₹2,575 - 50% off
Daniel Klein DK12011-5 Analog Watch  - For Men - ₹2,172 - 45% off
Daniel Klein DK11159-2 Analog Watch  - For Women - ₹2,362 - 55% off
Daniel Klein DK11404-5 Analog Watch  - For Women - ₹1,487 - 65% off
Daniel Klein DK12016-4 Analog Watch  - For Men - ₹2,172 - 45% off
Daniel Klein DK11739-1 EXCLUSIVE-GENTS Analog Watch  - For Men - ₹2,997 - 45% off
Daniel Klein DK11992-7 Analog Watch  - For Women - ₹2,612 - 45% off
Daniel Klein DK11775-3 Analog Watch  - For Men - ₹3,277 - 43% off
Daniel Klein DK11135-5 Analog Watch  - For Women - ₹2,475 - 50% off
Daniel Klein DK11407-4 Analog Watch  - For Women - ₹1,327 - 55% off
Daniel Klein DK12011-3 Analog Watch  - For Men - ₹2,070 - 40% off
Daniel Klein DK11650-2 Analog Watch  - For Men - ₹2,964 - 45% off
Daniel Klein DK12011-6 Analog Watch  - For Men - ₹1,897 - 45% off
Daniel Klein DK12005-2 Analog Watch  - For Men - ₹2,722 - 45% off
Daniel Klein DK11699-4 Analog Watch  - For Women - ₹3,272 - 45% off
Daniel Klein DK11652-3 Premium-gents Analog Watch  - For Men - ₹2,111 - 60% off
Daniel Klein DK11642-3 Fiord-gents Analog Watch  - For Men - ₹2,069 - 50% off
Daniel Klein DK12014-4 Analog Watch  - For Men - ₹2,722 - 45% off
Daniel Klein DK12012-5 Analog Watch  - For Men - ₹2,172 - 45% off
Daniel Klein DK11684-1 FIORD-LADYS Analog Watch  - For Women - ₹2,722 - 45% off
Daniel Klein DK12017-4 Analog Watch  - For Men - ₹2,670 - 40% off
Daniel Klein DK11986-7 Analog Watch  - For Women - ₹2,282 - 45% off
Daniel Klein DK11637-1 Premium-ladys Analog Watch  - For Women - ₹1,687 - 55% off
Daniel Klein DK11959-5 Analog Watch  - For Men - ₹3,822 - 45% off
Daniel Klein DK11946-2 Analog Watch  - For Men - ₹4,170 - 40% off
Daniel Klein DK11914-4 Analog Watch  - For Women - ₹2,062 - 45% off
Daniel Klein DK12017-2 Analog Watch  - For Men - ₹2,172 - 45% off
Daniel Klein DK12016-2 Analog Watch  - For Men - ₹2,172 - 45% off
Daniel Klein DK11752-2 Analog Watch  - For Men - ₹4,449 - 45% off
Daniel Klein DK12011-4 Analog Watch  - For Men - ₹1,897 - 45% off
Daniel Klein DK11665-5 Analog Watch  - For Women - ₹3,225 - 50% off
Daniel Klein DK11821-1 Analog Watch  - For Men - ₹1,851 - 43% off
Daniel Klein DK11958-4 Analog Watch  - For Men - ₹3,570 - 40% off
Daniel Klein DK11995-1 Analog Watch  - For Men - ₹2,062 - 45% off
>>> response = urlopen('https://www.flipkart.com/watches/pr?sid=r18&marketplace=FLIPKART&p%5B%5D=facets.price_range.from%3D10000&offer=nb%3Amp%3A0951e46510&fm=neo%2Fmerchandising&iid=M_a9e4f155-20a8-467f-9b54-6d4d36a14fac_2.TGGGGB02JCLZ&ssid=93byr922s00000001570693148014&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_6_2.dealCard.OMU_TGGGGB02JCLZ_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_6_NA_view-all_2&cid=TGGGGB02JCLZ&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.brand%255B%255D%3DTitan&p%5B%5D=facets.brand%255B%255D%3DTissot&p%5B%5D=facets.serviceability%5B%5D%3Dtrue')

>>> htmlPage = bs(response)
>>> htmlPage

>>> watches = htmlPage.find_all('div', class_ = 'IIdQZO')
>>> for watch in watches:
	print(watch.find('div', class_ = '_2B_pmu').text + " " +  watch.find('a', class_ = '_2mylT6').text + " - " + watch.find('div' , class_ = '_1vC4OE').text + " - " + watch.find('div', class_ = 'VGWI6T').find('span').text)

	
Titan 1688KM01 Analog Watch  - For Men - ₹10,920 - 5% off
Titan 1696QC02 Slimmest Ceramic Watch by Edge Analog Watch  -... - ₹20,895 - 5% off
Titan 1684SL01 Edge Analog Watch  - For Men - ₹10,920 - 5% off
Titan NH1043YL03 Analog Watch  - For Men - ₹9,970 - 5% off
Titan NH13772385BM01 Analog Watch  - For Couple - ₹11,395 - 5% off
Titan NH90013WD01J Analog Watch  - For Men - ₹12,820 - 5% off
Titan NH1296NM01 Edge Analog Watch  - For Men - ₹12,820 - 5% off
Titan NH1688KM02 Analog Watch  - For Men - ₹11,395 - 5% off
Titan NH9812WM01 Raga Analog Watch  - For Women - ₹12,820 - 5% off
Titan NH1043NM01 Analog Watch  - For Men - ₹11,870 - 5% off
Titan 95044WM01J Raga Analog Watch  - For Women - ₹11,395 - 5% off
Titan 17332570KM01 Modern Bandhan Analog Watch  - For Men & W... - ₹10,445 - 5% off
Titan NH1043WL01 Edge Analog Watch  - For Men - ₹10,445 - 5% off
Titan NH1044NL01 The Agent Analog Watch  - For Men - ₹10,445 - 5% off
Titan NH95011WM03 Raga Analog Watch  - For Women - ₹14,720 - 5% off
Titan NH1296BM01 Edge Analog Watch  - For Men - ₹12,820 - 5% off
Titan 1793KM02 Analog Watch  - For Men - ₹18,045 - 5% off
Tissot T091.420.44.081.00 Analog-Digital Watch  - For Men - ₹54,590 - 20% off
Titan NH1043BM01 Analog Watch  - For Men - ₹11,870 - 5% off
Titan 1747KM01 Regalia Sovereign Analog Watch  - For Men - ₹9,642 - 5% off
Titan 1683NL01A Edge Analog Watch  - For Men - ₹10,445 - 5% off
Titan NH1577TL01A Skeletal Edge Analog Watch  - For Men - ₹15,005 - 5% off
Titan 1683YL01A Edge Analog Watch  - For Men - ₹10,255 - 5% off
Titan 95043WM01J Raga Analog Watch  - For Women - ₹12,820 - 5% off
Titan 95063WM01F Raga Espana Analog Watch  - For Women - ₹10,920 - 5% off
Titan NH1595WL03 Analog Watch  - For Men - ₹10,445 - 5% off
Titan 1748BM01 Regalia Sovereign Analog Watch  - For Men - ₹10,521 - 5% off
Titan 95055WM01F Raga Espana Analog Watch  - For Women - ₹9,970 - 5% off
Titan NH1296YM02 Edge Analog Watch  - For Men - ₹12,345 - 5% off
Titan 1683WL01A Edge Analog Watch  - For Men - ₹10,445 - 5% off
Titan 1684YM01 Edge Analog Watch  - For Men - ₹12,630 - 5% off
Titan 1748KM01 Regalia Sovereign Analog Watch  - For Men - ₹10,958 - 5% off
Titan 1793KM01 Analog Watch  - For Men - ₹16,145 - 5% off
Titan NH9931WM01 Raga Analog Watch  - For Women - ₹11,015 - 5% off
Titan 95030YM01 Raga Analog Watch  - For Women - ₹16,620 - 5% off
Titan NH19262926BM01 Bandhan Analog Watch  - For Couple - ₹13,295 - 5% off
Titan NH1044YL04 Edge Analog Watch  - For Men - ₹10,445 - 5% off
Titan NH1296BM02 Edge Analog Watch  - For Men - ₹12,820 - 5% off
Titan NH1044BM02 Edge Analog Watch  - For Men - ₹12,345 - 5% off
Titan 1684YL01 Edge Analog Watch  - For Men - ₹11,395 - 5% off
>>> response = urlopen('https://www.flipkart.com/mens-footwear/pr?sid=osp%2Ccil&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3D199&p%5B%5D=facets.price_range.to%3DMax&sort=popularity&offer=nb:mp:096b037309&fm=neo%2Fmerchandising&iid=M_57a17f9b-6c5f-4b17-a001-59f460f16a8c_2.Q9W9CLWQ4F8O&ppt=hp&ppn=hp&ssid=jqj6onm64w0000001570693157178&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_2.dealCard.OMU_Q9W9CLWQ4F8O_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_2&cid=Q9W9CLWQ4F8O')

>>> htmlPage = bs(response)
>>> shoes = htmlPage.find_all('div', class_ = 'IIdQZO')
>>> for product in shoes:
	print(product.find('div', class_ = '_2B_pmu').text + " " +  product.find('a', class_ = '_2mylT6').text + " - " + product.find('div' , class_ = '_1vC4OE').text + " - " + product.find('div', class_ = 'VGWI6T').find('span').text)

	
BRUTON Men 201 & Cubic-1 Combo Pack of 2 Casual Sneakers For M... - ₹499 - 79% off
BUWCH Buwch Derby Lace Up For Men  (Tan) Lace Up For Men - ₹636 - 36% off
Asian WNDR-13 Running Shoes For Men - ₹474 - 20% off
BRUTON Combo Pack Of 5 Casual Shoes Loafers For Men - ₹899 - 77% off
Oricum Boxer-303 Sneakers For Men - ₹261 - 47% off
Bersache Combo(BR)-1077-349 Sneakers For Men - ₹362 - 63% off
Beerock Oxygen Running Shoes For Men - ₹459 - 54% off
BRUTON Combo Pack of 2 Casual Sneakers For Men - ₹525 - 78% off
Asian Cosco Running Shoes For Men - ₹616 - 38% off
Asian WNDR-13 Running Shoes For Men - ₹474 - 20% off
Oricum ORIFWSH(A)-303 Casuals For Men - ₹283 - 43% off
AA Trendy stylish comfortable elegant decent lace-up butto... - ₹256 - 74% off
Oricum ORIFWSH(OR)-1077 Sneakers For Men - ₹214 - 57% off
believe high top Sneakers for men High Tops For Men - ₹446 - 55% off
ADIDAS DROGO M SS 19 Running Shoes For Men - ₹1,709 - 36% off
BRUTON Men 201 & Cubic-1 Combo Pack of 2 Casual Sneakers For M... - ₹499 - 79% off
Asian Jio-13 Running Shoes For Men - ₹474 - 20% off
Kraasa Climber Boots For Men - ₹500 - 49% off
Sukun Running Shoes For Men - ₹474 - 52% off
Kraasa Casuals,Party Wear Sneakers For Men - ₹527 - 47% off
Asian WNDR-13 Running Shoes For Men - ₹474 - 20% off
Beerock Oxygen Running Shoes For Men - ₹459 - 54% off
Asian WNDR-13 Running Shoes For Men - ₹474 - 20% off
BRUTON Combo Pack Of 3 Loafer Shoes Loafers For Men - ₹616 - 78% off
Fashionboom Men Black - ₹474 - 52% off
Asian Jio-13 Running Shoes For Men - ₹474 - 20% off
Fashionboom Flip Flops - ₹284 - 71% off
casela Accupressure Yoga Paduka Power Mat Full Body Relaxer Na... - ₹486 - 62% off
ADIDAS DROGO M SS 19 Running Shoes For Men - ₹1,709 - 36% off
A-CLASS Men Combo Pack of 2 Casual Shoes Casuals For Men - ₹499 - 79% off
ZIXER Exclusive Hip Hop Dancing Boots Sneakers Dancing Shoes ... - ₹555 - 44% off
Asian Black Sports Shoes,Running Shoes,Walking Shoes,Training... - ₹569 - 43% off
My Cool Step Blue Denim Men's Sneakers Shoes Canvas Shoes For Men - ₹299 - 40% off
Believe Sneakers for men(black_7) Sneakers For Men - ₹446 - 55% off
Kraasa Men Synthetic Leather Chappal (Camel) Slippers - ₹379 - 57% off
SCATCHITE Combo Pack of 3 Casual ,Party ,Lace Up Shoes Canvas Sho... - ₹569 - 61% off
Asian Running Shoes For Men - ₹616 - 38% off
Asian Running Shoes For Men - ₹616 - 38% off
Arise Men's Breathable Mesh Sports Running Shoes Running Shoe... - ₹474 - 52% off
BRUTON Men Pack of 2 Casual Sneakers For Men - ₹499 - 80% off
>>> 
