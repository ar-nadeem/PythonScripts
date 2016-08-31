print("Importing Modules")
from bs4 import BeautifulSoup
import requests
import socks
import socket
import time
print("Imported Modules \n NOTE: Google doesnt let you see more searches then a fixed number .")

def ProxyConnect () :
    try:
        print ("Connecting to Proxy")
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4,"127.0.0.1", 9050, True)
        socket.socket = socks.socksocket
        requests.get("https://www.google.com/")
    except:
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080, True)
        socket.socket = socks.socksocket
        print("Could Not Connect to Proxy")





def searchGoogle():
    global searchG
    global headers
    searchG=[]
    page=0
    page=str(page)
    search=raw_input("Dork ===> ? \n")
    print("Converting to string")
    search=str(search)
    print("Searching")
    for i in range (40):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        r = requests.get("https://www.google.com/search?sclient=psy-ab&client=windows10&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q="+search+"&start="+page,headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        page=int(page)
        page=page+10
        page=str(page)
        print (soup.contents)
        for cite in  soup.find_all('cite'):
            print("")
            print (cite.text)
            #searchG.append((cite.text))
            #print (cite.text)  result__url__domain
            print("")


def searchDuckDuckGo():
    global searchD
    searchD=[]
    search=raw_input("Dork ===> ? \n")
    print("Converting to string")
    search=str(search)
    print("Searching")


    r = requests.get("https://duckduckgo.com/?q="+search)
    soup = BeautifulSoup(r.content, "html.parser")
    for link  in soup.find_all('links'):
        print("")
        print (link.text)
        # searchG.append((cite.text))
        # print (cite.text)  result__url__domain
        print("")

def searchBing():
    global searchB
    searchB=[]
    search=raw_input("Dork ===> ? \n")
    print("Converting to string")
    search=str(search)
    print("Searching")


    r = requests.get("https://duckduckgo.com/?q="+search)
    soup = BeautifulSoup(r.content, "html.parser")
    for link  in soup.find_all('links'):
        print("")
        print (link.text)
        # searchG.append((cite.text))
        # print (cite.text)  result__url__domain
        print("")





#ProxyConnect()
while 1:
    #searchGoogle()
    searchDuckDuckGo()