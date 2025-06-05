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

## Data Sources
American Community Survey (ACS)
- On-going survey from United States Census Bureau 
- Collects data on the social, economic, housing, and demographic characteristics of the U.S. population
- Our focus includes household income, educational attainment, householder/marital/civilian status, poverty level, and age

National Provider Identifier (NPI) Registry
- Free, public directory
- Contains active provider information based on the 10-digit unique NPI
- We pulled information for active hospice organizations based in CO

Other datasets include:
- Alzheimer's rates, Colorado County Boundaries

## Getting Started

### Dependencies

* Prerequisites, libraries, OS version, etc., needed before installing program:

## Python libraries:
- requests
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

### Installing

* How/where to download your program:
* 
* Any modifications needed to be made to files/folders:

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Interactive Notebook

View the full exploratory notebook: (https://nbviewer.org/github/erinbest017/COMP4447Hospice/blob/main/Code/hospiceEDA%20and%20Mapping%20by%20County.ipynb).

This includes data visualizations, EDA, and a county-level Plotly map of hospice-related metrics.

## Authors

Contributors names and contact info

- Dagmar Velez | https://www.linkedin.com/in/dagmarvelez/
- Erin Best    | www.linkedin.com/in/erin-best-msds

## Version History

