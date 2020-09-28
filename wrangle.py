import pandas as pd
import numpy as np
import datetime

import os

def acquire_data():
    
    if os.path.isfile('./311data.csv') == True:
    
        df = pd.read_csv('311data.csv')
        
        df.drop(columns=('Unnamed: 0'), inplace=True)
    
    else:
    
        url = '''https://data.sanantonio.gov/dataset/93b0e7ee-3a55-4aa9-b27b-d1817e91aec3/resource/20eb6d22-7eac-425a-85c1-fdb365fd3cd7/download/allservicecalls.csv'''
    
        df = pd.read_csv(url)
    
        df.to_csv('311data.csv')
    
    return df


def change_data_types(df):
    """Change Data Types for columns in df"""
        
    # changing floats and ints to objects
    df.CASEID = df.CASEID.astype('object')
    df.XCOORD = df.XCOORD.astype('object')
    df.YCOORD = df.YCOORD.astype('object')
    df['Council District'] = df['Council District'].astype('object')
    
    # change objects to datetime
    df.OPENEDDATETIME = pd.to_datetime(df.OPENEDDATETIME)
    df.CLOSEDDATETIME = pd.to_datetime(df.CLOSEDDATETIME)
    df['Report Starting Date'] = pd.to_datetime(df['Report Starting Date'])
    df['Report Ending Date'] = pd.to_datetime(df['Report Starting Date'])
    
    return df

def change_column_names(df):
    """this function changes columns into a pythonic naming convention"""
    
    # change the column names and save them in a list
    new_column_names = []
    for i in df.columns:
        i = i.lower().replace(" ", "_")
        new_column_names.append(i)
    
    # create a dictionary with original column names and new column names
    d = {}
    for i in range(len(df.columns)):
        d[df.columns[i]] = new_column_names[i]
        
    # rename column names in df
    df = df.rename(columns=d)
    
    return df    