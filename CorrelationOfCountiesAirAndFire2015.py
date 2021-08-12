#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import requests
import json
import matplotlib.pyplot as plt
import seaborn
import scipy 
from bokeh.models import ColumnDataSource


# In[2]:


#Goal of my Analysis - possible correlation of counties with worse air quality and fires 
#Focus on year 2015 and inhable particulates PM2.5 (PM = Particulate Matter)


# In[3]:


#Fire Data
fire_file = "./Fires.csv"


fire_file_df = pd.read_csv(fire_file, encoding="ISO-8859-1")

fire_file_df.columns


# In[4]:


# #fips_codes https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt
# fips_file = './fips.txt'

# fips_file_df = pd.read_csv('./fips.txt', delimiter = ",")
# fips_file_df.head()


# In[5]:


# #Only fips for CA
# keep_fips_CA = {'fips_state': [6]}

# filtered_fips_file_df = fips_file_df[fips_file_df[list(keep_fips_CA)].isin(keep_fips_CA).all(axis=1)]

# filtered_fips_file_df


# In[6]:


#reduce fire columns
reduced_fire_file_df = fire_file_df[['FIRE_YEAR','FIRE_NAME','DISCOVERY_DATE', 'DISCOVERY_DOY',
       'DISCOVERY_TIME', 'STAT_CAUSE_CODE', 'STAT_CAUSE_DESCR', 'CONT_DATE','FIRE_SIZE', 'FIRE_SIZE_CLASS', 'LATITUDE',
       'LONGITUDE', 'OWNER_CODE', 'OWNER_DESCR', 'STATE', 'COUNTY',
       'FIPS_CODE', 'FIPS_NAME']]
                                                                   

reduced_fire_file_df.head()


# In[7]:


#filter fire data for year and state

keep_fire = {'FIRE_YEAR': [2015], 'STATE': ['CA']}
filtered_fire = reduced_fire_file_df[reduced_fire_file_df[list(keep_fire)].isin(keep_fire).all(axis=1)]

filtered_fire_df = pd.DataFrame(filtered_fire)


# In[8]:


# #change fips code to county
# inner_join_fire_fips = pd.merge(reduced_fire_file_df, 
#                       fips_file_df, 
#                       on ='FIPS_CODE', 
#                       how ='inner')
# inner_join_fire_fips_df = pd.DataFrame(inner_join_fire_fips) 
# inner_join_fire_fips_df


# In[9]:


# #filter fire data for year and state

# keep_fire = {'FIRE_YEAR': [2015], 'STATE': ['CA']}
# filter_fire_ca_df = filtered_fire_df[list(keep_fire)].isin(keep_fire).all(axis=1)


# In[10]:


filtered_fire_df


# In[11]:


# Create a group based on the values in the 'fips_county' column with more than 2000 total acres in 2015
fire_county_group = filtered_fire_df.groupby('FIPS_NAME')

# Count how many times each maker appears in our group
fire_size_sum = fire_county_group['FIRE_SIZE'].sum()[fire_county_group['FIRE_SIZE'].sum() > 10000 ]

# Create a bar chart based off of the group series from before
fire_size_sum_chart = fire_size_sum.plot(kind='bar')

# Set the xlabel and ylabel using class methods
fire_size_sum_chart.set_xlabel("County",)
fire_size_sum_chart.set_ylabel("Sum of the size of all of 2015's fires (acres)")

plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


#Air Quality Data 
CA_air_quality = "./CA_air_quality_annual_summary.csv"

CA_air_quality_df = pd.read_csv(CA_air_quality, encoding="ISO-8859-1")


CA_air_quality_df



# In[13]:


CA_air_quality_df.columns


# In[14]:


#reduce air quality columns
reduced_CA_air_quality_df = CA_air_quality_df[['state_code', 'county_code', 'site_num',
       'latitude', 'longitude', 'parameter_name', 'sample_duration', 'metric_used', 'year',
       'units_of_measure', 'event_type', 'observation_count',
       'observation_percent', 'arithmetic_mean',
       'arithmetic_standard_dev', 'first_max_value',  'address', 'state_name', 'county_name', 'city_name',
       'date_of_last_change']]

reduced_CA_air_quality_df


# In[15]:


#filter air quality data for 2.5 PM /24 hr duration/2015
keep_air = {'year': [2015], 'state_name': ['California'], 'sample_duration': ['24-HR BLK AVG'], 'parameter_name':['PM2.5 - Local Conditions']}

filtered_air_df = reduced_CA_air_quality_df[reduced_CA_air_quality_df[list(keep_air)].isin(keep_air).all(axis=1)]

filtered_air_df



# In[ ]:


filtered_air_df 


# In[57]:


# Create a group based on the values in the 'county_name' column
filtered_air_group = filtered_air_df.groupby('county_name')


filtered_air_group_max = filtered_air_group['first_max_value'].max()[filtered_air_group['first_max_value'].max() > 75 ]

# Create a bar chart based off of the group series from before
air_mean_chart = filtered_air_group_mean.plot(kind='bar')

# Set the xlabel and ylabel using class methods
air_mean_chart.set_xlabel("County")
air_mean_chart.set_ylabel("Max PM2.5 value for the year")


plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[58]:


#Analysis - possible correlation of counties with worse air quality and fires 
#plot two counties side by side fire vs air quality

fig, axes = plt.subplots(nrows=1, ncols=2)

ax1 = fire_size_sum.plot(ax = axes[1], kind='bar')
ax1.set_ylabel('Sum of the size of all of 2015 fires (acres)')
ax1.set_xlabel('County')



ax2 = filtered_air_group_max.plot(ax = axes[0], kind='bar')
ax2.set_ylabel('Max PM2.5 value for the year')
ax2.set_xlabel('County')


plt.tight_layout()


# In[18]:


get_ipython().system(' pip3 install gmaps')


# In[19]:


get_ipython().system(' jupyter nbextension enable --py gmaps')


# In[20]:


# Dependencies and Setup
import gmaps
import os

# Import API key
from api_keys import g_key


# In[21]:


#config gmaps
gmaps.configure(api_key=g_key)


# In[39]:


#narrowed dataframe show biggest fires
narrow_fire_df = filtered_fire_df[['FIRE_YEAR','FIRE_NAME','FIRE_SIZE','LATITUDE',
                                    'LONGITUDE','STATE','FIPS_NAME']]
narrow_fire_acre_100 = narrow_fire_df.loc[narrow_fire_df['FIRE_SIZE'] > 100]


narrow_fire_acre_100.head()


# In[ ]:





# In[70]:


#heatmap of fire data california
locations = narrow_fire_df[['LATITUDE', 'LONGITUDE']]
fire_size = narrow_fire_df['FIRE_SIZE']
fig = gmaps.figure()
heat_layer = gmaps.heatmap_layer(locations, weights=fire_size, dissipating=True, max_intensity=300, point_radius=5)
fig.add_layer(heat_layer)
fig


# In[68]:


#air dataframe Max PM2.5 value for the year > 75 
#longitude and latitude for counties here https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2020_Gazetteer/2020_gaz_counties_06.txt


filtered_air_group_max_df = pd.DataFrame(filtered_air_group_max)


filtered_air_group_max_df 


# In[84]:


#heatmap of air quality by Max PM2.5 value for the year
locations = filtered_air_df[['latitude', 'longitude']]
max_air_quality = filtered_air_df['first_max_value']

fig = gmaps.figure()
heat_layer = gmaps.heatmap_layer(locations=locations, weights=max_air_quality, dissipating=True, max_intensity=300, point_radius=10)
fig.add_layer(heat_layer)
fig



# In[ ]:




