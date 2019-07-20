from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req

my_url='https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2'

uClient=req(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"lxml")

containers=page_soup.findAll("div",{"class":"a-section a-spacing-medium"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container=containers[0]

name=container.findAll("div",{"class":"a-section a-spacing-none"})
#print(name[1].text)

price=container.findAll("span",{"class":"a-price-whole"})
#print(price[0].text)

ratings=container.findAll("span",{"class":"a-icon-alt"})
#print(ratings[0].text)

filename="products1.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name_cont=container.findAll("div",{"class":"a-section a-spacing-none"})
    product_name=product_name_cont[1].text.strip()
    try:
        price_container=container.findAll("span",{"class":"a-price-whole"})
        price=price_container[0].text.strip()
    except IndexError:
        price=""
    try:
        rating_container=container.findAll("span",{"class":"a-icon-alt"})
        rating=rating_container[0].text
    except IndexError:
        rating=""
    '''
    print("Product_name: "+product_name)
    print("Price: "+price)
    print("Ratings: "+rating)'''

    trim_price=''.join(price.split(','))
    add_rs_price="Rs."+trim_price
    split_rating=rating.split(" ")
    final_rating=split_rating[0]

    print(product_name.replace(","," |")+", "+add_rs_price+", "+final_rating+"\n")
    f.write(product_name.replace(",","|")+", "+add_rs_price+", "+final_rating+"\n")
f.close()
