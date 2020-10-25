import os
import urllib3
from bs4 import BeautifulSoup

# all data
http = urllib3.PoolManager()
source_url = 'https://nadc.china-vo.org/data/mirror/Gaia/dr2/gaia_source/csv/'
save_dir = 'H:/Gaia_dr2'

os.system('mkdir '+save_dir)
os.chdir(save_dir)

dl_page = http.request('Get', source_url)
dl_page_html = BeautifulSoup(dl_page.data.decode('utf-8'))

list_dl_url = dl_page_html.findAll('a')

for dl_url in list_dl_url:
    href_url = dl_url.get('href')
    if 'csv.gz' in href_url:
        print('Downloading: '+href_url.split('/')[-1])
        os.system('wget '+source_url+href_url)
