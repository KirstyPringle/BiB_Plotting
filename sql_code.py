# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:35:08 2020

@author: earkpr
"""

#https://www.bluehost.com/help/article/managing-databases-with-command-line-ssh 
import pandas as pd
import sqlite3
#import sys
#from os import listdir
#from os.path import isfile, join
#import os
import glob
from datetime import datetime

# Get path to files
##mypath ="C://Users\\earkpr\\OneDrive - University of Leeds/BiB/Pilot/"
mypath="/Users/earkpr/Desktop/BiB/Data/"

myfiles=glob.glob(mypath+"*db")
print(myfiles)
print(len(myfiles))

for f in myfiles:
    print("f = ", f)
    print("")

    file = f
    file_trunk = f[:-3]

    '''
    pip3 uninstall numpy #remove previously installed package
    sudo apt install python3-numpy
    '''
    
    # Read sqlite query results into a pandas DataFrame
    
    conn = sqlite3.connect(file)
    #conn = sqlite3.connect("/root/sensor.db")
    
    df = pd.read_sql_query("SELECT * from MEASUREMENTS", conn)
    
    print("f = ",file, pd.unique(df["SERIAL"]))
    
    # cursor = conn.execute("SELECT * from MEASUREMENTS")
    
    # Verify that result of SQL query is stored in the dataframe
    #print(df.drop('LOC',axis=1).tail(n=50))
    
    #if 'csv' in sys.argv:
    #  print("here")
    #  df.drop('LOC',axis=1).to_csv(file+'.csv')
    #  print(' Written to /root/deleteme.csv. Please Delete after')
    
    # Convert Unix datetime to normal datetime
    date_time = df.apply(lambda x: datetime.fromtimestamp(x['UNIXTIME']), axis=1)
    df["DATETIME"]=date_time
    print(date_time)
    
##    df.to_csv(file_trunk+'_Measurements.csv', columns = ['TIME', 'PM1', 'PM3', 'PM10', 'SP', 'RC'], index=False)

    #print("About to write to file")
    df.to_csv(file_trunk+'_Measurements.csv', columns = ['SERIAL', 'TYPE', 'TIME', 'LOC', 'PM1', 'PM3', 'PM10', 'T', 'RH', 'SP','RC', 'UNIXTIME','DATETIME'], index=False)    
    
    #df.to_csv('./Measurements.csv', columns = ['TIME', 'PM1', 'PM3', 'PM10', 'SP', 'RC'], index=False)
    
    conn.close()


print("End of script")
