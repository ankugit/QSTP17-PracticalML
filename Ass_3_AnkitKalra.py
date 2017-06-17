
# coding: utf-8

# In[9]:

#Solution using python lib...will try using conventional mathemtaics of linear regression


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn


# In[26]:

data = pd.read_excel("sat.xls")


# In[30]:

from sklearn.linear_model import LinearRegression


# In[73]:

data.drop(['math_SAT','verb_SAT','comp_GPA'],axis=1, inplace=True)
#IMportant to do implace=True faced problems without it


# In[ ]:




# In[74]:

X=data.drop("univ_GPA", axis=1)
lm=LinearRegression()
lm.fit(X, data.univ_GPA)


# In[76]:

pd.DataFrame(zip(X.columns, lm.coef_), columns=["Features", "Est"])


# In[ ]:




# In[ ]:




# In[82]:

plt.plot(X, data.univ_GPA,'bo')
plt.plot(X, lm.predict(X) , 'g-')
plt.xlabel("GPAin High School")
plt.ylabel("GPA in University ")
plt.show()


# In[ ]:



