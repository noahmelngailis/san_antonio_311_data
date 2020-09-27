import pandas as pd
import numpy as np
import datetime

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
    