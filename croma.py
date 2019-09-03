from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv

my_url = ['https://www.croma.com/phones/c/1',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=2',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=3',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=4',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=5',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=6',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=7',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=8',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=9',
          'https://www.croma.com/phones/c/1?q=%3Arelevance%3AskuStockFlag%3Atrue&page=10']


#FILE OPERATIONS
filename = "croma.csv"
f = open(filename,"w",encoding='utf-8')
headers = "number,model,rating,offer_price,original_price,price_difference\n"
f.write(headers)
filename1 = "past_data_croma.csv"
f1 = open(filename1,"a",encoding='utf-8')



count = 1
no_of_pages = 0

for y in my_url :
    uClient = uReq(y)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'lxml')
    every = page_soup.find_all('li',{'class' :'product__list--item'})
    no_of_pages +=1
    
    for x in every:
        if count == 181:
            break
        print(count)
        lol = x.find('div',class_ = 'row')
        lol2 = lol.find('div',class_ = 'row')
        tit = lol2.find('a',class_ = 'product__list--name') 
        title = tit.text
        title = title.replace(",","")
        title = title.lower()
        if((title[0] == 'x') and (title[1] == 'i') and (title[2] == 'a') and (title[3] == 'o') and (title[4] == 'm') and (title[5] == 'i')):
            title = title.replace('xiaomi','redmi')
            print("\nTitle          : ", title)
                     
        else:
            print("\nTitle          : ", title)
            
        #FINAL PRICE
        offprice = lol2.find('div',class_ = 'col-md-4 col-xs-8')
        offprice1 = offprice.find('div',class_='_priceRow')
        offprice2 = offprice1.find('span',class_='pdpPrice')
        offprice3 = offprice2.text  
        final_price = offprice3.replace("₹","")
        final_price = final_price.replace(",","")
        print("\nFinal Price    : ", final_price)
        
        
        #ORIGINAL PRICE
        try:
            orgprice = offprice1.find('span',class_ = 'pdpPriceMrp')
            
            original_price = orgprice.text
            original_price = original_price.replace("₹","")
            original_price = original_price.replace(",","")
            print("\nOriginal Price : ",original_price)
    
        except:
            original_price = final_price
            print("\nOriginal Price : ",original_price)
            
        #RATING    
        for tag in lol.find_next_siblings('div',class_ = 'row'):
            try:
                rat = tag.find('div',class_ = 'col-xs-12 col-sm-4 col-md-3')
                rat1 = rat.find('div',class_ = 'rating')
                rat2 = rat1.find('div',class_ = 'rating-stars pull-left js-ratingCalc ')
                rat3 = rat2.find('div',class_ = 'greenStars js-greenStars')
                rat4 = rat3.find('span',class_ = 'glyphicon glyphicon-star active')
                laugh = rat4.find_next_siblings('span',class_ = 'glyphicon glyphicon-star active')
                star = len(laugh)
                print("\nRating         : ",star)
                rating = str(star)
            except:
                print("\nRating         :  NO RATING")
                rating = '0'

        #CALCULATINIG PRICE DIFFERENCE
        price_diff = float(original_price) - float(final_price)
        price_diff = str(price_diff)
        print("\nPrice Difference: ", price_diff)
        no = str(count)
        count += 1
        print("----------------------------------------------")  
        f.write(no + "," + title + "," + rating + "," + final_price + "," + original_price + "," + price_diff +  "\n")
        

print("\nProducts :", count)
print("\nPages    :", no_of_pages)
 
#MEAN INTO PAST DATA CSV FILE   
readdata = csv.reader(open('D:\\6th Semester\\Project\\27-2\croma\\croma.csv', 'r'))
data = []
for row in readdata:
   if row is not None:
     data.append(row)
  
data.pop(0)  
q1 = []     
for i in range(len(data)):
   q1.append(float(data[i][5]))
print ('Mean price of croma : ', (np.mean(q1)))

#TRACK OF DATE AND MEAN
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
print ("\ndate          : ", date)
f1.write(date + "," + str(np.mean(q1)) +  "\n")


f.close()
f1.close()
