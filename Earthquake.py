#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:34:36 2022

@author: angela
"""

#%% Imports 

import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import numpy as np 
import datetime
import os 

#%% Constants 

CSV_PATH = os.path.join(os.getcwd(),'database.csv')


#%% 

def magnitude_classification (dataframe: pd.DataFrame): 
    '''
    Classify earthquake based on magnitude

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe containing earthquake data.

    Returns
    -------
    Str.
    Returns the classification of the earthquake as a string. 
    '''
    if dataframe['Magnitude']>= 5.0 and dataframe['Magnitude']<=5.9:
        return 'Moderate (5.0-5.9)'
    elif dataframe['Magnitude']>= 6.0 and dataframe['Magnitude']<=6.9: 
        return 'Strong (6.0-6.9)'
    elif dataframe['Magnitude']>=7.0 and dataframe['Magnitude']<=7.9: 
        return 'Major(7.0-7.9)'
    elif dataframe['Magnitude']>= 8.0 :
        return 'Great (>8.0)'


#%% 1) Data Loading 

df = pd.read_csv(CSV_PATH)


#%% 2) Data Inspection 

df.info()  # total entries = 23412
df.isna().sum() # Depth Error, Depth Seismic Stations , Magnitude Error,Magnitude Seismic Stations,Azimuthal Gap,Horizontal Distance,Horizontal Error has a lot of NaNs value 


#%% 

df['Class'] = df.apply(magnitude_classification, axis=1)

print(df)


#%% Plotting out year vs magnitude

g = sns.FacetGrid(df,col='Type')
df['Date']= pd.to_datetime(df['Date'],utc=True)
df['year']= pd.DatetimeIndex(df['Date']).year

g.map(sns.scatterplot,'year','Magnitude',alpha=0.5) 

#%% Plotting out year vs depth, with ylim set

g = sns.FacetGrid(df,col='Type')
df['Date']= pd.to_datetime(df['Date'],utc=True)
df['year']= pd.DatetimeIndex(df['Date']).year

g.map(sns.scatterplot,'year','Depth',alpha=0.5) 
g.set(ylim=([750,-10]))

#%% Add column and rows to the facet grid 

g = sns.FacetGrid(df,col='Type', row='Class')
df['Date']= pd.to_datetime(df['Date'],utc=True)
df['year']= pd.DatetimeIndex(df['Date']).year

g.map(sns.scatterplot,'year','Depth',alpha=0.5) 
g.set(ylim=([750,-10]))

#%% Cleaning up subplot titles 

g = sns.FacetGrid(df,col='Type', row='Class')
df['Date']= pd.to_datetime(df['Date'],utc=True)
df['year']= pd.DatetimeIndex(df['Date']).year

g.map(sns.scatterplot,'year','Depth',alpha=0.5) 
g.set_titles(col_template='{col_name}',row_template='{row_name}')
g.set(ylim=([750,-10]))


#%% Odering the subplot in Facet grid 

g = sns.FacetGrid(df,col='Type', row='Class',row_order=['Moderate (5.0-5.9)',
                                                        'Strong (6.0-6.9)',
                                                        'Major(7.0-7.9)',
                                                        'Great (>8.0)'])
df['Date']= pd.to_datetime(df['Date'],utc=True)
df['year']= pd.DatetimeIndex(df['Date']).year

g.map(sns.scatterplot,'year','Depth',alpha=0.5) 
g.set_titles(col_template='{col_name}',row_template='{row_name}')
g.set(ylim=([750,-10]))


#%% Histogram in Facet Grid 

g = sns.FacetGrid(df,col='Type')
g.map(sns.histplot,'year')
# g.set(ylim=(0,100))  # this is comment out as after setting ylim the data visualization is bad for earthquake 

#%% Histogram in Facet Grid> change bins 

g = sns.FacetGrid(df,col='Type')
g.map(sns.histplot,'year', bins=5)


#%% Boxplot in Facet Grid 

g = sns.FacetGrid(df,col='Type')
g.map(sns.boxplot,'year')
