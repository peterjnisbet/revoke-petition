# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:42:59 2019

@author: Pete Nisbet
"""

import pandas as pd

json_url = 'https://petition.parliament.uk/petitions/241584.json'#

import urllib.request, json 
with urllib.request.urlopen(json_url) as url:
    data = json.loads(url.read().decode())
data = data['data']['attributes']['signatures_by_constituency']

columns = ['name', 'ons_code', 'mp', 'signature_count']
petition_df = pd.DataFrame(columns = columns, index = range(len(data)))
idx = 0
for instance in data:
    for head in columns:
        petition_df.loc[idx, head] = instance[head]
    idx +=1

""" location of constituency data - https://data.parliament.uk/resources/constituencystatistics/population-detailed.xlsx """

fname = 'population-detailed.xlsx' # location - https://data.parliament.uk/resources/constituencystatistics/population-detailed.xlsx
df = pd.read_excel(fname,encoding='latin-1',sheet_name='Data')
df = df.sort_values('DateOfDataset')
df = df.drop_duplicates('ConstituencyName', keep='last')

petition_df['Population'] = 0 
for idx in range(len(petition_df)):
    if df['PopTotalConstNum'][df['ConstituencyName'] == petition_df.loc[idx,'name']].values:
        petition_df.loc[idx,'Population'] = df['PopTotalConstNum'][df['ConstituencyName'] == petition_df.loc[idx,'name']].values

petition_df['signature_count'] = petition_df['signature_count'].astype('int64')
petition_df['PercSigned'] = petition_df['signature_count'] / petition_df['Population']


""" party names are added manually to this csv before importing it prior to plotting
 - this data should eb pulled from somewhere - WIP """
 
petition_df.to_csv('all.csv')




