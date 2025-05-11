""" 
This File imports a variety of American Community Survey (ACS) 
data tables from the United States Census Bureau.
"""

### Import Libraries 
import requests
import pandas as pd

### Using APIs, import ACS data
## Fetch Data Function
def _fetch_data(url, params):
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data[1:], columns = data[0])
    else:
        raise Exception(f'Failed to retrieve data: {response.status_code}')
    
## Median Income
def getS1903():
    url = 'https://api.census.gov/data/2023/acs/acs5/subject'
    params = {
        'get' : 'group(S1903)',
        'ucgid' : 'pseudo(0400000US08$1400000)'
    }
    return _fetch_data(url, params)

## Educational Attainment
def getS1501():
    url = 'https://api.census.gov/data/2023/acs/acs5/subject'
    params = {
        'get' : "group(S1501)",
        'ucgid' : 'pseudo(0400000US08$1400000)'
    }
    return _fetch_data(url, params)

## Households
def getDP02():
    url = 'https://api.census.gov/data/2023/acs/acs5/profile'
    params = {
        'get' : 'group(DP02)',
        'ucgid' : 'pseudo(0400000US08$1400000)'
    }
    return _fetch_data(url, params)

## Poverty Level
def getB17001():
    url = 'https://api.census.gov/data/2023/acs/acs5'
    params = {
        'get' : 'group(B17001)',
        'ucgid' : 'pseudo(0400000US08$1400000)'
    }
    return _fetch_data(url, params)

## Age
def getS0101():
    url = 'https://api.census.gov/data/2023/acs/acs5/subject'
    params = {
        'get' : 'group(S0101)',
        'ucgid' : 'pseudo(0400000US08$1400000)'
    }
    return _fetch_data(url, params)