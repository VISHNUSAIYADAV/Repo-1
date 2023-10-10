#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df =pd.read_csv(r"C:\Users\91939\Downloads\1._Weather_Data_2.csv")


# In[3]:


#1)
df["Wind Speed_km/h"].unique()


# In[4]:


df["Wind Speed_km/h"].value_counts()


# In[117]:


#2)
df.loc[df["Weather"]=="exactly Clear"]


# In[118]:


#3)
df.loc[df["Wind Speed_km/h"]=="4 km/h"]


# In[119]:


#4)
df.isnull().sum().sum()


# In[120]:


#5)
df.rename(columns = {"Weather":"Weather Condition"})


# In[121]:


#6)
df["Visibility_km"].mean()


# In[123]:


#7)
df["Press_kPa"].std()


# In[124]:


#8)
df["Rel Hum_%"].var()


# In[155]:


#9)
df.loc[df["Weather"]=="Snow"]


# In[126]:


#!10)
df.loc[(df["Wind Speed_km/h"]>24) & (df["Visibility_km"]== 25)]


# In[132]:


#11)
sd=df.groupby("Weather").mean()
sd


# In[144]:


#12)
sf=df.groupby("Weather").min()
print(sf)
Wm = df.groupby("Weather").max()
print(Wm)


# In[143]:


#13)

df.loc[df["Weather"]=="Fog"]


# In[147]:


#14)
df.loc[(df["Weather"]=="Clear") & (df["Visibility_km"]>40)]


# In[149]:


#15)
# A)
df.loc[(df["Weather"]=="Clear") & (df["Rel Hum_%"]>50)]


# In[152]:


# B
df.loc[df["Visibility_km"] >40]


# In[ ]:




