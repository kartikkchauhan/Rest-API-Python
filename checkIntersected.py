#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
import json


# In[16]:


url_bbf="http://127.0.0.1:8000/bbf_api/company_list/"
url_kinaway="http://127.0.0.1:8000/kinaway_api/company_list/"
url="http://127.0.0.1:8000/api/add_company/"
header={'Authorization':'Token 7d6c2613edec17081afcbafb7a02ce9353f5b691'}

company_name=None
company_abn=None
contacted=0
intersected=0
data_from_bbf="BBF"
data_from_kinaway="KINAWAY"


# In[17]:


response_bbf= requests.get(url_bbf, headers=header)
response_kinaway= requests.get(url_kinaway, headers=header)


# In[20]:


for row_kinaway in response_kinaway.json():
    for row_bbf in response_bbf.json():
        if int(row_kinaway['company_abn']) == int(row_bbf['company_abn']):
            company_name=row_kinaway['name']
            company_abn=row_kinaway['company_abn']
            intersected=1
            
            data={
                "company_name": company_name,
                "company_abn": company_abn,
                "contacted": contacted,
                "intersected": intersected,
                "data_from":  data_from_kinaway
            }
            
            response= requests.post(url, headers=header, data=data)
            
            print(str(response.status_code) + " " + response.text)
            


# In[21]:


for row_kinaway in response_kinaway.json():
    company_name=row_kinaway['name']
    company_abn=row_kinaway['company_abn']
    intersected=0

    data={
        "company_name": company_name,
        "company_abn": company_abn,
        "contacted": contacted,
        "intersected": intersected,
        "data_from":  data_from_kinaway
    }

    response= requests.post(url, headers=header, data=data)

    print(str(response.status_code) + " " + response.text)


# In[22]:


for row_bbf in response_bbf.json():
    company_name=row_bbf['name']
    company_abn=row_bbf['company_abn']
    intersected=0

    data={
        "company_name": company_name,
        "company_abn": company_abn,
        "contacted": contacted,
        "intersected": intersected,
        "data_from":  data_from_bbf
    }

    response= requests.post(url, headers=header, data=data)

    print(str(response.status_code) + " " + response.text)


# In[ ]:




