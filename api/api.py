import requests
import os
import config
# API Docs found here: https://developer.usajobs.gov/Tutorials/Search-Jobs

host = 'data.usajobs.gov' 
# add these values in the config.py file
userAgent = config.EMAIL_ADDRESS
authKey = config.US_JOBS_API_KEY

base_url = "https://data.usajobs.gov/api/search"

parameters = {
    "JobCategoryCode": 2210,
    "Keyword": "Software Development",
    "LocationName": "Washington, DC"
}

headers = {
    "Host": host,          
    "User-Agent": userAgent,          
    "Authorization-Key": authKey  
}

resp = requests.request("GET", base_url,headers=headers, params=parameters)
result = resp.json()['SearchResult']['SearchResultItems']

# get Job Title 
print(result[1]['MatchedObjectDescriptor']['PositionTitle'])
# get Job Summary
print(result[1]['MatchedObjectDescriptor']['UserArea']['Details']['JobSummary'])
# more parameters are found here: https://developer.usajobs.gov/API-Reference/GET-api-Search
