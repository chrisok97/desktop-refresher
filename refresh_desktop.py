import requests
import urllib
import os

URL = "https://api.unsplash.com/photos/random/?client_id=ca6cbc378f73e470af786c9a93b0fe19c0c5a031a8131b74e30" \
      "7e1eeda577d10&count=1&orientation=landscape&query=nature"

r = requests.get(url=URL)
data = r.json()

download_link = data[0]['urls']['full']
ID = data[0]['id']

# print(data)

urllib.urlretrieve(download_link, ("/Users/Chris/UnsplashImages/Image-{}.jpg" .format(ID)))
# urllib.urlretrieve(download_link, "abc123.jpg")

os.system(""" sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '/Users/Chris/UnsplashImages/Image-{}.jpg'" """ .format(ID))
os.system('killall Dock;')