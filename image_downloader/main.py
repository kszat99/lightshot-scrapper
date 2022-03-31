from bs4 import BeautifulSoup
import requests
import shutil
import exrex

page_start = 'https://prnt.sc/'
while 1 < 2:
    url_end = exrex.getone('[a-z0-9]{6}')
    page_url = page_start + url_end
    page = requests.get(page_url, headers={'User-Agent': 'Chrome'})
    soup = BeautifulSoup(page.content, 'html.parser')
    imglist = soup.find('img', {'id': 'screenshot-image'})
    if imglist is not None and imglist != []:
        image_url = imglist['src']
        filename = image_url.split("/")[-1]
        try:
            r = requests.get(image_url, headers={'User-Agent': 'Chrome'}, stream=True)
        except requests.exceptions.MissingSchema:
            continue
        r.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image successfully Downloaded: ', filename)
    else:
        print('Error downloading image url')
