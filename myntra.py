import wsurlopen
import bs4
import re
import io
import pandas as pd
import time,datetime

var=wsurlopen.urlopen('https://www.myntra.com/amp/men-tshirts')
read=bs4.BeautifulSoup(var.text, "lxml")
#print(read)

count=read.findAll("span",{"class":"index-productCount"})
counter=count[0].getText()
#print(counter)

counter=(re.sub("styles","",counter)).strip()
#print(counter)
counter=int(counter)//500
#print(counter)

with io.open("file1.csv","w",encoding="utf8") as f1:
    f1.write("BRAND,PRODUCT,ACTUAL PRICE,DISCOUNTED PRICE,DISCOUNT\n")
with io.open("file2.csv","w",encoding="utf8") as f2:
    f2.write("LINK\n")

#for i in range(int(counter)+1):
for i in range(2):
    i=i+1
    url1="https://www.myntra.com/amp/men-tshirts?rows=500&p="
    url1=url1+str(i)
    var1=wsurlopen.urlopen(url1)
    readfull=bs4.BeautifulSoup(var1.text,"lxml")
    read1=readfull.findAll("div",{"class":"productInfo"})
    read2=readfull.findAll("div",{"class":"product"})
    #print(read1)
    #print(read2)
    for j in read1:
        brand=j.findAll("div",{"class":"name"})
        try:
            brand=brand[0].text
        except IndexError:
            brand=""
            
        itemname=j.findAll("h4",{"class":"name-product"})
        try:
            itemname=itemname[0].text
        except IndexError:
            itemname=""

        sp=j.findAll("span",{"class":"price-discounted"})
        try:
            sp=sp[0].text
            sp=sp[1:]
            sp="Rs."+sp
        except IndexError:
            sp=""

        cp=j.findAll("span",{"class":"price"})
        try:
            cp=cp[0].text
            cp=cp[1:]
            cp="Rs."+cp
        except IndexError:
            cp=sp

        dis=j.findAll("span",{"class":"price-discount"})
        try:
            dis=dis[0].text.strip()
            dis1=dis.split("O")
            disf=dis1[0].replace("(","")
        except IndexError:
            disf="0%"

        data=brand+", "+itemname+", "+cp+", "+sp+", "+disf+"\n"
        with io.open("file1.csv","a",encoding="utf8")as f1:
            f1.write(data)
            f1.close()

    for k in read2:
        link=k.a["href"]
        link="https://www.myntra.com/"+link
        data1=link+"\n"
        with io.open("file2.csv","a",encoding="utf8")as f2:
            f2.write(data1)
            f2.close()

        #print(brand+", "+itemname+", "+cp+", "+sp+", "+disf)


#https://www.myntra.com/amp/men-tshirts?rows=500&p=4
