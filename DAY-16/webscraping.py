# -*- coding: utf-8 -*-
"""webScraping

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6RASmr9i4V3qgS1rnhMT3mKBrKMWX6W
"""

# %%
!pip install lxml
# !pip install html5lib

# %%
file = open('test.htm','r')
test = file.read()
file.close()

#%%
!pip install beautifulsoup
# from bs4 import BeautifulSoup 
print(BeautifulSoup('<b class="boldest">Extremely bold</b>','html5lib'))
# tag = soup.b
# type(tag)

#%%
from bs4 import BeautifulSoup
css_soup = beautifulsoup('<p class="body"></p>', 'html5lib')
css_soup.p['class']
# %%
