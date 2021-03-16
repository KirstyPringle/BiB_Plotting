# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:57:49 2021

@author: earkpr
"""

#import dash
#import dash_html_components as html
#import dash_leaflet as dl
#import parse,sys


##  use SED to remove USB from PA files
## sed "s/ UTC//" North\ Berwick\ \(outside\)\ \(56.051104\ -2.708487\)\ Primary\ Real\ Time\ 03_07_2021\ 03_09_2021.csv  > PA_A_03_07_2021_03_09_2021.csv

"North Berwick B (undefined) (56.051104 -2.708487) Primary Real Time 03_08_2021 03_09_2021.csv",
"North Berwick (outside) (56.051104 -2.708487) Primary Real Time 03_08_2021 03_09_2021.csv"

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import datetime as dt
import plotly.graph_objects as go

# Read PurpleAir Data

#pa1="North Berwick (outside) (56.051104 -2.708487) Primary Real Time 03_05_2021 03_08_2021.csv"
#pa2="North Berwick B (undefined) (56.051104 -2.708487) Primary Real Time 03_05_2021 03_08_2021.csv"

#Purple Air
#2021-03-07 07:35:31

#

#custom_date_parser = lambda x: datetime.strptime(x, "%Y-%d-%m %H:%M:%S")
#custom_date_parser = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")

pa1="PA_A_03_08_2021_03_09_2021.csv"
pa2="PA_B_03_08_2021_03_09_2021.csv"
#bb="simplesensor_09032021_decrypted.csv"
bb="sensor_short_Measurements_decrypted.csv"
path="/Users/earkpr/Desktop/BiB/Data/"

df_pa1 = pd.read_csv(path+pa1, usecols=["created_at", "PM2.5_ATM_ug/m3"],parse_dates= ['created_at'])
df_pa2 = pd.read_csv(path+pa2, usecols=["created_at", "PM2.5_ATM_ug/m3"],parse_dates= ['created_at'])
df_bb = pd.read_csv(path+bb,usecols=["DATE","PM3"],parse_dates=["DATE"])

df_bb=df_bb.dropna()

#x=df_bb["PM3"]
#x = x[x.between(x.quantile(.15), x.quantile(.85))] # without outliers
#x=df_bb["PM3"]

##df['PM3'] = df.iloc[:,1].rolling(window=100).mean()


df_bb['DATE'] = pd.to_datetime(df_bb['DATE'])
df_bb_5m = df_bb.set_index('DATE') 
df_bb_resampled=df_bb_5m.resample('5Min').mean()
df_bb_5m = df_bb_resampled.reset_index()


#%%

print(df_pa1.columns)
print(df_pa2.columns)
print(df_bb.columns)


df_new1 = df_pa1.rename(columns={"created_at":"created_at_1", "PM2.5_ATM_ug/m3":"PM2p5_1"})
df_new2 = df_pa2.rename(columns={"created_at":"created_at_2", "PM2.5_ATM_ug/m3":"PM2p5_2"})


fig = go.Figure()
fig.update_layout(yaxis_range=[-4,20])

# Add traces

fig.add_trace(go.Scatter(x=df_bb["DATE"], y=df_bb["PM3"],
                   mode='markers',
                    name='BB'))#

#fig.add_trace(go.Scatter(x=df_bb_5m["DATE"], y=df_bb["PM3"],
#                    mode='lines+markers',
#                    name='BB'))

#fig.add_trace(go.Scatter(x=df_new1['created_at_1'], y=df_new1["PM2p5_1"],
#                   mode='markers',
#                   name='PA1'))

#fig.add_trace(go.Scatter(x=df_new1['created_at_1'], y=df_new2["PM2p5_2"],
#                    mode='markers',
#                    name='PA2'))


fig.update_layout(
    title = 'Time Series with Custom Date-Time Format',
    )
    
##df_new1['DateStr'] = df_new1['created_at_1'].dt.strftime('%d%m%Y')

fig.update_xaxes(tickangle=45)

fig.write_image(path+"ZigZag_Timeseries.png")

fig.show()

#%%

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_bb["DATE"], y=df_bb["PM3"],
                    mode='markers',
                    name='lines'))

fig.update_layout(
    title = 'Time Series with Custom Date-Time Format',
    )
    
fig.show()
