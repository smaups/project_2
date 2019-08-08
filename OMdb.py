from bs4 import BeautifulSoup
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import requests
import pandas as pd
import numpy as np
import re
import json
import pprint

# ['bo_year_rank','title','studio','worldwide-gross','domestic-gross','domestic-pct','overseas-gross','overseas-pct']
MOJO (API):
***Search string
Bo_year
Title
Domestic Gross
Worldwide Gross

mojo_df = pd.read_csv('data/annual_mojo.csv')
# print(mojo_df.head())

mojo_title = mojo_df.title
mojo_year = mojo_df.bo_year
mojo_domestic = mojo_df.domestic-gross
mojo_worldwide = mojo_df.worldwide-gross

url = 'http://www.omdbapi.com/'

# def OMdbAPI():

#     mojo_df = pd.read_csv('/data/annual_mojo.csv')
#     print(mojo_df.head())
#     url = 'http://www.omdbapi.com/'


# if __name__ == "__main__": 

# OMdbAPI()