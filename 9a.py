#9a
import requests
from bs4 import BeautifulSoup
import os
folder = input("ENTER THE DIECTORY : ")
if not os.path.exists(folder):
    os.makedirs(folder)
for i in range(1,20):
    soup = BeautifulSoup(requests.get('https://xkcd.com/' + str(i) + '/').content, 'html.parser')
    src = soup.find('div', id='comic').find('img')['src']
    download = requests.get('https:' + src)
    print("DOWNLOADING : https:", src)
    image_path = os.path.join(folder, 'image' + str(i) + '.png')
    with open(image_path, 'wb') as f:
        f.write(download.content)

import requests
from bs4 import BeautifulSoup
import os
folder=input("Enter Dir: ")
if not os.path.exists(folder):
    os.makedirs(folder)
for i in range(1,20):
    soup=BeautifulSoup(requests.get('https://xkcd/'+str(i)+'/').content,'html.parser')
    src=soup.find('div',id='comic').find('img')['src']
    download=requests.get('https:',src)
    print("DOWNLOADING : https:", src)
    image_path=os.path.join(folder,str(i),'.png')
    with open(image_path,'wb') as f:
        f.write(download.content)
import requests
from bs4 import BeautifulSoup as BS
import os
