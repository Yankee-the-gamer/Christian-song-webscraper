from bs4 import BeautifulSoup
import urllib.request
import re
import pathlib
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
content = requests.get("https://atheycreek.com/teachings/genesis", headers=headers).text
soup = BeautifulSoup(content, features="html.parser") #beautifulSoup initialization

links = [a['href'] for a in soup.find_all('a',href=re.compile('http.*\.mp3'))] #finds all .mp3 links in the site and puts it in a list
titles = [i.get_text().strip() for i in soup.find_all("a", class_="text-decoration-none")] # finds all title elements and puts it in a list

for i in range(len(links)):
    titles[i] = re.sub(r'[^\w\-_\. ]', '', titles[i]) #gets rid of invalid characters in the filename/title
    doc = requests.get(links[i])
    p = pathlib.Path( titles[i] + '/')
    p.mkdir(parents=True, exist_ok=True)
    filename = titles[i] + ".mp3" 
    filepath = p / filename
    with open(filepath, "wb") as f:
        print("downloading... new file")
        f.write(doc.content)
	
        
print("done downloading")
