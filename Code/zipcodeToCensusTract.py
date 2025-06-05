""""
This file takes a dataframe of NPI, zipcodes+4, and other information and adds the censustract
to the df by converting the zipcode +4 to the appropriate censustract
"""

### Install if needed
# !pip install pgeocode
# !pip install censusgeocode

### Import Libraries 
import pandas as pd
import numpy as np
import pgeocode as pg
import censusgeocode as cg
import time

################# TO BE REPLACED WITH DAGMAR'S WORK #################
## TEST DATA
testData = {'NPI': ['1760093470', '1861097982', '1447936901', '1043826795'], 
            'zipPlusFour': ['80237-2857', '81008-2130', '80111-2213', '80111-7957'],    ##Last zipcode is not accurate - just used for testing
            'taxType': ['NPI-2 Organization', 'NPI-2 Organization', 'NPI-2 Organization', 'NPI-2 Organization'], 
            'primaryTax': ['Yes', 'Yes', 'Yes', 'No'], 
            'Issuer': ['MEDICAID', '', '', ''], 
            'status': ['Active', 'Active', 'Active', 'Active']}

## CREATE TEST DF
df = pd.DataFrame(testData)

####################################################################


## Function - postal code to lat/long
def convertPostalToLatLong(zipcode):
    postal = pg.Nominatim('us')
    lat = postal.query_postal_code(zipcode)['latitude']
    long = postal.query_postal_code(zipcode)['longitude']
    return lat, long

## Function - lat/long to Census Tract
def convertLatLongToCensusTract(lat, long):
    time.sleep(0.1)
    try:
        result = cg.coordinates(x = long, y = lat)
        censusTract = result['Census Tracts'][0]['GEOID']
        censusTract = '1400000US' + censusTract
        return censusTract
    except Exception as e:
        print(f'Error {e} at lat = {lat}, long = {long}')
        return None
    
## Create zipcode column
df['zip'] = df['zipPlusFour'].str[:5]

## Call function and add lat/long to df
df[['lat', 'long']] = df['zip'].apply(lambda zip: pd.Series(convertPostalToLatLong(zip)))

## Call function and censustract to df
df['censusTract'] = df.apply(lambda row: convertLatLongToCensusTract(row['lat'], row['long']), axis = 1)
df
