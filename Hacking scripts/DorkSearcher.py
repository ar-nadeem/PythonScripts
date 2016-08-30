print("Importing Modules")
from bs4 import BeautifulSoup
import requests
import socks
import socket
print("NOTE: Google doesnt let you see more searches then a fixed number .")

def TORconnect():
		try:
			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1",9050,True)
			socket.socket = socks.socksocket
			requests.get("https://www.google.com/search?sclient=psy-ab&client=windows10&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=TEST")






def main():
	page=0
	page=str(page)
	search=raw_input("Dork ===> ? \n")
	print("Converting to string")
	search=str(search)
	print("Searching")
	print("Here are the link that i found in the first page of google :) please select me ;D")

	try:
		for i in range (40):
			r = requests.get("https://www.google.com/search?sclient=psy-ab&client=windows10&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q="+search+"&start="+page)
			soup = BeautifulSoup(r.content, "html.parser")
			page=int(page)
			page=page+10
			page=str(page)
			for cite in  soup.find_all('cite'):
				print("")
				print (cite.text)
				print("")

	except:
		print("These are all the results")

#TORconnect()
while 1:
	main()