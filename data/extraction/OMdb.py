from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from config import omdb_api_s, omdb_api_b, omdb_api_l
import requests
import pandas as pd
import numpy as np
import re
import json
import pprint

# def OMdbAPI():

mojo_dff = pd.read_csv('data/annual_mojo.csv')


mojo_df = mojo_dff[mojo_dff['bo_year_rank'] <101].reset_index()

# print(mojo_df)
mojo_title = mojo_df.title
mojo_year = mojo_df.bo_year
mojo_domestic = mojo_df['domestic-gross']
mojo_worldwide = mojo_df['worldwide-gross']
# print(mojo_title[5])
# print(len(mojo_year))

omdb_data = []
base_url = 'http://www.omdbapi.com/'
print(len(mojo_title)-1649)
for i in range(len(mojo_title)-1649):
    # print(mojo_title[i])
    try:
        url = base_url +'?apikey=' + omdb_api_b + '&t=' + str(mojo_title[i]) + '&y=' + str(mojo_year[i])
        request = requests.get(url)
        results = json.loads(request.text)
        print(json.dumps(results, indent=4))
        omdb_data.append(results)
    except KeyError:
        print("OMdb does not have this title"+ mojo_title[i])

for i in range(len(mojo_title)- 1649):
    print(mojo_title[i+825])  
    try:
        url = base_url +'?apikey=' + omdb_api_l + '&t=' + str(mojo_title[i+825]) + '&y=' + str(mojo_year[i+825]) 
        request = requests.get(url)
        results = json.loads(request.text)
        print(json.dumps(results, indent=4))
        omdb_data.append(results)
    except KeyError:
        print("OMdb does not have this title" + mojo_title[i+825])

for i in range(len(mojo_title)- 1649): 
    print(mojo_title[i+ 1649])   
    try:  
        url = base_url +'?apikey=' + omdb_api_s + '&t=' + str(mojo_title[i+1649]) + '&y=' + str(mojo_year[i+1649])
        request = requests.get(url)
        results = json.loads(request.text)
        print(json.dumps(results, indent=4))
        omdb_data.append(results) 
    except KeyError:
        print("OMdb does not have this title" + mojo_title[i+825])

with open('OMdb.json', 'w') as omdb_file:
     json.dump(omdb_data, omdb_file, indent=4)

omdb_df = pd.DataFrame(omdb_data)
omdb_df.to_csv('./data/OMdb.csv')
print(omdb_df.head())


# def init_browser():
#     executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#     return Browser('chrome', **executable_path, headless=False)

# def api():
#     base_url = 'http://www.omdbapi.com/'
#     url = base_url +'?apikey=' + omdb_api + '?t=' + mojo_title[i] + '&y=' + mojo_year[i] 
#     request = requests.get(url)
#     omdb_data = json.loads(request.text)
# def OMdbAPI():

#     mojo_df = pd.read_csv('/data/annual_mojo.csv')
#     print(mojo_df.head())
#     url = 'http://www.omdbapi.com/'


# if __name__ == "__main__": 

# OMdbAPI()