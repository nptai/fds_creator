# Download image from Google Search
# Nguyen Phat Tai
# nptai95@gmail.com


from bs4 import BeautifulSoup
import urllib2
import os
import cookielib
import json
import glob
import config


INPUT = config.FACE_LIST
OUTPUT = config.RAW_DIR

if not os.path.exists(OUTPUT):
    os.mkdir(OUTPUT)

def get_soup(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), "html.parser")

f = open(INPUT, 'r')
queries = f.read().split('\n')[:-1]

print queries

for query in queries:
    image_type = 'img'
    dir = os.path.join(OUTPUT, query)
    query = query.replace(' ', '+')
    url =  'https://www.google.co.in/search?q=' + query + '&source=lnms&tbm=isch'

    print dir
    header = { 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url, header)

    imgs = []
    for a in soup.find_all('div', {'class': 'rg_meta'}):
        link, type = json.loads(a.text)['ou'], json.loads(a.text)['ity']
        imgs.append((link, type))

    print 'there are total', len(imgs), 'images'

    for i, (img, type) in enumerate(imgs):
        try:
            req = urllib2.Request(img, headers={'User-Agent': header})
            raw_img = urllib2.urlopen(req).read()
            print 'Downloading', img
            if not os.path.exists(dir):
                os.mkdir(dir)
            
            cnt = len([i for i in os.listdir(dir) if image_type in i]) + 1

            if len(type) == 0:
                type = 'jpg'

            f = open('{0}/{1}_{2}.{3}'.format(dir, image_type, str(cnt), type), 'wb')

            f.write(raw_img)
            f.close()
        except Exception as e:
            # print 'could not load:', img
            # print e
            pass
