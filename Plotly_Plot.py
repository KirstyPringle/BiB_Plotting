# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:19:33 2021

@author: earkpr
"""

# conda install -c plotly plotly=4.3.0
# conda install -c plotly plotly-orca

# Using plotly.express
import pandas as pd
#import matplotlib.pyplot as plt

#import plotly

import plotly.express as px


path="/Users/earkpr/Desktop/BiB/Data/"

#df = pd.read_csv(path+"data_new.csv")

df = pd.read_csv(path+"data_new_2021-02-19_2021-03-04.csv")
#df = pd.read_csv(path+"data_new_2021-02-22_2021-02-26.csv")

df['DATETIME'] = pd.to_datetime(df['DATETIME'])

df_new = df.set_index('DATETIME') 
df_resampled=df_new.resample('30Min').mean()
df_new = df_resampled.reset_index()



print(df.columns)
#df.reset_index()
#df_resampled.reset_index()

print("2", df.columns)

fig=px.scatter(df_new, x="DATETIME", y="PM3")

#fig=px.scatter(df_resampled, x=df_resampled["PM3"].index, y="PM3")

##fig.write_image(file=path+'staff_plot.png', format='.png')
##fig.savefig("plot.png")

fig.show()
