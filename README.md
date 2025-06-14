# Mapping Hospice Care Access in Colorado
### A County-Level Analysis Using Sociodemographic Indicators and Alzheimer’s and Dementia Prevalence

Research Questions:
- How do community characteristics, as captured by the American Community Survey (ACS) data, correlate with the presence and density of hospice providers across the state of Colorado?
- Can we identify gaps in hospice care access across Colorado by analyzing Alzheimer's disease prevalence and county-level demographic indicators?

## Description

This project explores disparities in hospice care access across Colorado using a blend of sociodemographic data and Alzheimer’s/dementia prevalence. We geospatially map hospice provider density and analyze trends based on:
- Age distribution
- Educational attainment
- Household and marital composition
- Alzheimer’s and Dementia prevalence in adults aged 65+

Our goal is to visualize and better understand geographic gaps in end-of-life care services.

## Data Sources (/Data)
**American Community Survey (ACS)**
- [Source: U.S. Census Bureau  ](https://data.census.gov/)
- Key features: Income, education, poverty level, age, and household composition

**National Provider Identifier (NPI) Registry**
- https://npiregistry.cms.hhs.gov/search
- Public directory of active U.S. healthcare providers  
- Filtered for active hospice providers in Colorado

**Other datasets**
- Alzheimer's and Dementia prevalence (65+) in Colorado by county
- Colorado county boundary GeoJSON  

## Getting Started

### Dependencies

## Make sure to install the following Python libraries:
- requests
- shapely.geometry
- time
- re
- fuzzywuzzy
- pandas
- numpy
- geopandas
- matplotlib
- seaborn
- pgeocode
- censusgeocode
- Point
- random
- plotly
- dash

### Running the Code (/Code)
Clone the repository: 
```
git clone https://github.com/erinbest017/COMP4447Hospice.git
cd COMP4447Hospice
```
Or Download all files from the COMP4447Hospice/Code/ Folder

## Description of Code (/Code)
  
#### 1) COMP4447Hospice/Code/NPI Info API.ipynb:
- pulls NPI Registry data to get provider counts and creates 'df_zip.pkl'
  
#### 2) COMP4447Hospice/Code/mainCounty.ipynb:
- pulls function from ACSDataImport.py
- pulls data from 'df_zip.pkl' (Hospice Provider Counts) and merges on ACS data
- creates 'mergedTableCounty.pkl'
- creates 'merged65andOver.pkl'

#### 3) COMP4447Hospice/Code/hospiceEDA and Mapping by County.ipynb
- uses 'mergedTableCounty.pkl' to create EDA and Hospice Provider Dashboard
- uses 'df_alzheimers.pkl' to merge to ACS data for visualization

#### 4) COMP4447Hospice/Code/hospiceMLCounty.ipynb:
- uses 'mergedTableCounty.pkl' for model development
- uses 'merged65andOver.pkl' for Gaps in Hospice Care analysis

## Interactive Notebook

View the full exploratory notebook: (https://nbviewer.org/github/erinbest017/COMP4447Hospice/blob/main/Code/hospiceEDA%20and%20Mapping%20by%20County.ipynb).

This includes data visualizations, EDA, and a county-level dashboard (using Plotly Dash) of hospice-related metrics.

## Authors

- Dagmar Velez | https://www.linkedin.com/in/dagmarvelez/
- Erin Best    | www.linkedin.com/in/erin-best-msds

## Version History
- v1.0 - initial release (June 2025)

## Acknowledgements
Thanks to our University of Denver COMP 4447 - Data Science Tools I course professor, Rahim Rasool, and our classmates for guidance and feedback throughout this project.
