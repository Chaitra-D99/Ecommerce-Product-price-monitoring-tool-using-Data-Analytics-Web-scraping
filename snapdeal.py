from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv

my_url = 'https://www.snapdeal.com/search?keyword=mobiles&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#FILE OPERATIONS
filename = "snapdeal.csv"
f = open(filename,"w",encoding='utf-8')
headers = "number,model,rating,final_price, original_price, price_difference\n"
f.write(headers)
filename1 = "past_data_snapdeal.csv"
f1 = open(filename1,"a",encoding='utf-8')


page_soup = soup(page_html,'lxml')


#MAIN HEADING
title_web =  page_soup.title.text
print(title_web)
print("---------------")
div_web = page_soup.div.text
page_all = page_soup.find_all('div',{'class':'col-xs-24'})
print(page_all)
count = 1

k = 0
for y in page_all:
    every = page_soup.find_all('div', {'class': 'product-tuple-description'})
    for x in every:
        if count == 181:
            break
        print(count)
        #TITLE
        try:
            title = x.div.a.p.text
            title = title.replace(",","")
            title = title.lower()
            print("\nTitle          : ", title)
        except:
            print("\nTitle          : ", title)
            
        #OFFER PRICE
        find_div1 = x.find('div',class_='product-desc-rating')
        find_div2 = find_div1.find('div',class_='product-price-row clearfix')
        find_div3 = find_div2.find('div',class_='lfloat marR10')
        find_div4 = find_div3.find('span',class_='lfloat product-price')  
        
        #OFFER PRICE
        try:
            offprice = find_div4.text
            offprice = offprice.replace(",", "")
            offprice = offprice.replace("Rs.","")
            print("\nOffer Price    : ", offprice)
        except:
            print("\nOffer Price    : ", offprice)
            offprice = "1000"
            
        #ORIGINAL PRICE
        try:
            orgprice = x.div.a.div.div.span.text
            orgprice = orgprice.replace("Rs.","")
            orgprice = orgprice.replace(",","")
            print("\nOriginal Price : ",orgprice)
        except:
            print("\nOriginal Price : ",offprice)
            orgprice = offprice

        #RATING  
        try:
            star = x.find('div',class_='clearfix rating av-rating')
            find_div3 = star.find('div', class_='filled-stars')
            rating = find_div3.get('style')
            rating = rating.replace("width:", "")
            rating = rating.replace("%", "")
            frating = float(rating)
            frating = (5*frating)/100
            print("\nRating         : ",frating)
            frating = str(frating)

        except:
            print("\nRating         : NO RATING")
            frating = "0"
            
        no = str(count)
        count +=1 
        price_diff = float(orgprice) - float(offprice)      
        price_diff = str(price_diff)
        print("\nPrice diff     : ", price_diff)
    
        f.write(no + "," + title + "," + frating + "," + offprice + "," + orgprice + "," + price_diff + "\n")
        print("----------------------------------------------")
    k += 1

     
readdata = csv.reader(open('C:\\Users\\Shivam\\Desktop\\Mini pro\\27-2\\snapdeal\\snapdeal.csv', 'r'))
data = []
for row in readdata:
   if row is not None:
     data.append(row)
  
data.pop(0)  
q1 = []     
for i in range(len(data)):
   q1.append(float(data[i][5]))
print ('\nMean price of snapdeal : ', (np.mean(q1)))

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
print ("\ndate          : ", date)
f1.write(date + "," + str(np.mean(q1)) +  "\n")


f.close()
f1.close()
