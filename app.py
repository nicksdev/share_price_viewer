from urllib import request
from urllib import parse

# https://www.asx.com.au/asx/1/share/WBT/prices?interval=daily&count=30


perams = {"interval": "daily", "count": "30"}
querystring = parse.urlencode(perams)

sharecode = input("Enter Sharecode: ")

url = "https://www.asx.com.au/asx/1/share/" + sharecode + "/prices?" + querystring

resp = request.urlopen(url)
html = resp.read().decode("utf-8")

print(html)
