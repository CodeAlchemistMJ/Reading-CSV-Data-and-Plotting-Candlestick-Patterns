#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install --upgrade mplfinance


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import ipywidgets as widgets
from IPython.display import display


# Step-1 : Read CSV data into a dataframe

# In[3]:


data = "https://trello.com/1/cards/6438c561324b51d6acb221e1/attachments/643ff55dd651987ffe1ad119/download/StockDataBANKBARODA_1.csv"
df = pd.read_csv(data)
print(df)


# Step-2: Cleaning and Preprocessing of data

# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.isnull()


# In[8]:


#Let's assume the CSV contains columns: "Date", "Open", "High", "Low", "Close"
#Hence converting "Date" column to datetime

df['Date'] = pd.to_datetime(df['Date'])


# Step-3: Plot candlestick chart

# In[9]:


#Convert date to mdates format
df['Date'] = df['Date'].apply(mdates.date2num)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']]
print(ohlc)


# In[10]:


#Function to update candlestick chart based on slider value
def chart_update(candlestick_width):
  plt.figure(figsize=(12,6))
  ax = plt.subplot()
  ax.xaxis_date()
  candlestick_ohlc(ax, ohlc.values, width=candlestick_width, colorup="b", colordown="r")
  plt.title('BANK of BARODA - Candlestick Chart')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.xticks(rotation=45)
  plt.show()


# In[11]:


# Create slider widget for candlestick width adjustment
candlestick_slider = widgets.FloatSlider(min= 0.1, max=1.0, step=0.1, value=0.6, description='Candlestick Width')


# In[12]:


#Display the initial chartwith default candlestick width
chart_update(candlestick_slider.value)


# In[13]:


widgets.interactive(chart_update, candlestick_width = candlestick_slider)


# In[ ]:





# In[ ]:




