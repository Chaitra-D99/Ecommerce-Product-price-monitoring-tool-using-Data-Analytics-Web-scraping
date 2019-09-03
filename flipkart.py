from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
    
my_url = ['https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=1',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=2',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=3',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=4',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=5',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=6',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=7',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=8',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=9',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=10',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=11',
          'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page=12']


#FILE OPERATIONS
filename = "flipkart.csv"
f = open(filename,"w",encoding='utf-8')
headers = "number,model,rating,final_price,original_price,price_difference\n"
f.write(headers)
filename1 = "past_data_flipkart.csv"
f1 = open(filename1,"a",encoding='utf-8')

count = 1
no_of_pages = 0

for y in my_url:
    uClient = uReq(y)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'lxml')
    every = page_soup.find_all('div', {'class': '_1-2Iqu row'})
    no_of_pages +=1
    
    for x in every :
        if count == 181:
            break
        print(count)   
        title = x.div.div.text 
        title = title.replace(",", "")
        title = title.lower()
        print("\nTitle          : ", title)
        
        #RATING
        try:
            rating = x.div.span.div.text
            print("\nRating         : ",rating)
        except:
            print("\nRating         : NO RATING")
            rating = "0"
        
        #OFFER PRICE
        price = x.find('div', class_ = 'col col-5-12 _2o7WAb')
        price1 = price.find('div',class_ = '_6BWGkk')
        price2 = price1.find('div', class_ = '_1uv9Cb')
        price_final = price2.find('div', class_ = '_1vC4OE _2rQ-NK')
        price_original = price2.find('div', class_ = '_3auQ3N _2GcJzG')
        
        try:
            price_final1 = price_final.text
            price_final1 = price_final1.replace(",", "")
            price_final1 = price_final1.replace("₹","")
            print("\nOffer Price    : ",price_final1)
            
        except:
            print("\nOffer Price : No discount")
            price_final1 = "1000"
        
        #ORIGINAL PRICE
        try:
            price_original1 = price_original.text
            price_original1 = price_original1.replace(",", "")
            price_original1 = price_original1.replace("₹","")
            print("\nOriginal Price : ", price_original1)

        except:
            print("\nOriginal Price : ", price_final1)
            price_original1 = price_final1               
        
        
        price_diff = float(price_original1) -float(price_final1)     
        price_diff = str(price_diff)
        print("\nPrice diff     : ", price_diff)
        
        no = str(count)
        f.write(no + "," + title + "," + rating + "," + price_final1 +  "," + price_original1 + "," + price_diff + "\n")
        count += 1
        print("----------------------------------------------")
  
        
#MEAN INTO PAST DATA CSV FILE        
readdata = csv.reader(open('C:\\Users\\Shivam\\Desktop\\Mini pro\\27-2\\flipkart\\flipkart.csv', 'r'))
data = []
for row in readdata:
   if row is not None:
     data.append(row)
  
data.pop(0)  
q1 = []     
for i in range(len(data)):
   q1.append(float(data[i][5]))
print ('Mean price of flipkart : ', (np.mean(q1)))

#TRACK OF DATE AND MEAN
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
print ("\ndate          : ", date)
f1.write(date + "," + str(np.mean(q1)) +  "\n")

f.close()
f1.close()
