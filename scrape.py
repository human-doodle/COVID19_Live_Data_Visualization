# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:29:26 2020

@author: Shivani
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore certification errors

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url='https://covidindia.org/maharashtra/'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

data=[]  
table = soup.find('table', attrs={'id':'tablepress-61'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
for e in data:
    print(e)