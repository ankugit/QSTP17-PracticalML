
# coding: utf-8

# In[4]:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Loading data
data=pd.read_csv("database.csv")


# In[11]:

#Task-1 Show how the usage of a given weapon varied. Plot frequency of a weapon used vs year(simple line plot preferably). Take at least 4 weapons of your choice
#Analysis of Weapons that are not common for killing
plt.figure(1)
plt.subplot(211)
data["Weapon"][data["Weapon"]=="Fall"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Weapon"][data["Weapon"]=="Poison"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Weapon"][data["Weapon"]=="Drowning"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Weapon"][data["Weapon"]=="Suffocation"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()


# In[12]:

#Task-2 For a given relationship how the number of homicides has varied with time. Same analysis as above but with Relationship variable
plt.figure(2)
plt.subplot(211)
data["Relationship"][data["Relationship"]=="Son"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Relationship"][data["Relationship"]=="Daughter"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Relationship"][data["Relationship"]=="Wife"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()
plt.subplot(211)
data["Relationship"][data["Relationship"]=="Husband"].groupby(data["Year"]).value_counts().plot()
plt.xticks(rotation=45)
plt.show()


# In[13]:

#Task-3 A Box plot of weapon Vs year
import seaborn as sn

sn.boxplot(x=data["Year"],y=data["Weapon"])
plt.show()

