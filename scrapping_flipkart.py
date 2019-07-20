from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient=req(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"lxml")

containers=page_soup.findAll("div",{"class":"_1UoZlX"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container=containers[0]

#print(container.div.img["alt"])
name=container.findAll("div",{"class":"_3wU53n"})
#print(name[0].text)

price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings=container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)

filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name_cont=container.findAll("div",{"class":"_3wU53n"})
    product_name=product_name_cont[0].text.strip()

    price_container=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container=container.findAll("div",{"class":"niH0FQ"})
    rating=rating_container[0].text
    '''
    print("Product_name: "+product_name)
    print("Price: "+price)
    print("Ratings: "+rating)

    '''
    trim_price=''.join(price.split(','))
    rm_rupee=trim_price.split("₹")
    add_rs_price="Rs."+rm_rupee[1]
    split_price=add_rs_price.split('U')
    split_price1=split_price[0].split('E')
    final_price=split_price1[0]

    split_rating=rating.split(",")
    split_rating1=split_rating[0].split(" ")
    final_rating=split_rating1[0]

    print(product_name.replace(",","|")+", "+final_price+", "+final_rating+"\n")
    f.write(product_name.replace(",","|")+", "+final_price+", "+final_rating+"\n")
f.close()

