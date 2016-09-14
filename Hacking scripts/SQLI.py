print("Importing Modules")
from bs4 import BeautifulSoup
import requests
import socks
import socket
import time
print("Imported Modules \n NOTE: There is a fixed number search results you can get from a website.")
print("==Remember Connecting to TOR will make Google ask you Captcha so you will be Automatically Shifted To Yahoo and Bing Skipping Google!.==\n\n\n")






def main():
    global pages
    pages = input("How many pages you want to search in each engine (Google,Bing and Yahoo) eg. 5 :   ")
    pages=int(pages)

    proxy=raw_input("\n Would you like to connect to TOR PROXY \n Y / N \n ")
    if (proxy.upper()) == "Y":
        ProxyConnect()
        global searchG
        searchG=[]
        global search
        search = raw_input("Dork ===> ? \n")
        print("Converting to string")
        search = str(search)
        print ("====YAHOO=====")
        global printyahoo
        printyahoo=0
        searchYahoo()
    else:
        printyahoo=1
        searchGoogle()

def ProxyConnect () :
    try:
        print ("Connecting to Proxy")
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4,"127.0.0.1", 9050, True)
        socket.socket = socks.socksocket
        requests.get("https://www.google.com/")
        temp = socket.socket
    except:
        socket.socket = temp
        print("Could Not Connect to Proxy")

def searchGoogle():
    print ("====GOOGLE====")
    global searchG
    global headers
    global search
    searchG=[]
    page=1
    page=str(page)
    search=raw_input("Dork ===> ? \n")
    print("Converting to string")
    search=str(search)
    print("Searching")
    for i in range (pages):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        try:
            r = requests.get("https://www.google.com/search?client=ubuntu&channel=fs&q="+search+"&ie=utf-8&oe=utf-8&start="+page,headers=headers)
        except:
            print("Could not Connect to GOOGLE")
        soup = BeautifulSoup(r.content, "html.parser")
        page=int(page)
        page=page+10
        page=str(page)
        #print (soup.contents)
        for cite in  soup.find_all('cite'):
            if (cite.text.find("."))<0:
                searchYahoo()
            #print (cite.text)
            searchG.append((cite.text))
    searchYahoo()

def searchYahoo():
    if printyahoo==1:
        print ("====YAHOO=====")

    global searchY
    searchY=[]
    #search=raw_input("Dork ===> ? \n")
    #print("Converting to string")
    #search=str(search)
    print("Searching")
    page=1
    for i in range(pages):
        page=str(page)
        try:
            r = requests.get("https://search.yahoo.com/search;_ylc=X3oDMTFiN25laTRvBF9TAzIwMjM1MzgwNzUEaXRjAzEEc2VjA3NyY2hfcWEEc2xrA3NyY2h3ZWI-?p="+search+"&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8&b="+page)
            page=int(page)
            page=page+10
        except:
            print("Could Not Connect To the Yahoo")
            searchBing()

        soup = BeautifulSoup(r.content, "html.parser")
        #print(soup.prettify())
        for span  in soup.findAll("span",attrs={'class':" fz-ms fw-m fc-12th wr-bw lh-17"}):
            if (span.text.find("."))<0:
                searchBing()
            #print (span.text)
            searchY.append((span.text))
    searchBing()

def searchBing():
    print ("=====BING=====")
    global searchB
    searchB=[]
    #search=raw_input("Dork ===> ? \n")
    #print("Converting to string")
    #search=str(search)
    print("Searching")
    page=1
    for i in range(pages):
        page=str(page)
        try:
            r = requests.get("http://www.bing.com/search?q="+search+"&qs=n&pq=hello&sc=8-1&sp=-1&sk=&cvid=D0DB7A1DD2F24D0AB7151873430136F6&first="+page+"&FORM=PERE")
            page=int(page)
            page=page+10

        except:
            print("Could Not Connect To the BING")
            results()

        soup = BeautifulSoup(r.content, "html.parser")
        #print(soup.prettify())
        for cite  in soup.findAll("cite"):
            #print("")
            #print (cite.text)
            searchB.append((cite.text))
    results()

def results():
    print("\nHere are your Results :) \n")
    print("Remember the Common results are omitted out")
    global URLResult
    URLResult=[]
    URLResult=list(set().union(searchB,searchY,searchG))
    for i in URLResult:
        print (i)

def SQLI():
    print("\n\n\nChecking for SQL Vulnerability ....")
    global SQLIURL
    SQLIURL=[]
    for i in URLResult:
        SQL=i+"'"
        if SQL.find("http") < 0 and SQL.find("www.") < 0:
            SQL=("http://www."+SQL)
        elif SQL.find("http") < 0 and SQL.find("www.") > -1:
            SQL=("http://"+SQL)
        #print SQL
        try:
            r=requests.get(SQL)
        except:
            print("Could not Connect to the URL "+i)
        soup=BeautifulSoup(r.content,"html.parser")
        HTML=soup.get_text
        HTML=str(HTML)
        if HTML.find("SQL syntax") > -1 or HTML.find("mysqli_num_rows") > -1 or HTML.find("MySQL server") > -1 or HTML.find("mysqli_result") > -1 or HTML.find("expects parameter") > -1  :
            SQLIURL.append(i)
            print("==========================================================")
            print (i+" Is Vulnerable !")
            print("==========================================================\n\n\n\n")
        else:
            print (i+" is not Vulnerable\n\n")
    if SQLIURL:
        name = str(time.strftime("%H-%M-%S--%b-%d"))
        savefile = open(name+".txt","w")
        for websites in SQLIURL:
            savefile.write(websites+"\n")
        print("Saved Vulnerable Sites to "+savefile.name)
        savefile.close()

main()
SQLI()