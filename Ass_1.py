#Ankit Kalra

#The analysis is based on the dataset http://redirect.viglink.com/?format=go&jsonp=vglnk_149605411547714&key=bbb516d91daee20498798694a42dd559&libId=j39zu5q4010004m6000DA4d5isaqx&loc=http%3A%2F%2Fqstp-ml.freeforums.net%2Fthread%2F2%2Flesson-1-data-visualization&v=1&out=https%3A%2F%2Fgithub.com%2FSaloniDash7%2FQSTP17-PracticalML&ref=http%3A%2F%2Fqstp-ml.freeforums.net%2Fboard%2F1%2Fgeneral-discussion&title=Lesson%20-%201%20Data%20Visualization%20%7C%20Qstp-ml&txt=github.com%2FSaloniDash7%2FQSTP17-PracticalML
#Assignment-1
import matplotlib.pyplot as plt

#As I am new to Data Analysis I have not used predefined functions and sticked to conventional python....
#with time I plan to improve my code 

#Task1-"How many crimes were solved"

import pandas
data=pandas.read_csv("database.csv", dtype=str)

count=0
for t in data["Crime Solved"]:
    if t=="Yes":
        count=count+1
print("The number of crimes solved")
print(count)

#dat.count()

#Task2-"Top five weapons used"
import numpy as np

known_weapon=[]
for t in data["Weapon"]:
    if t!="Unknown":
        known_weapon.append(t)
from collections import Counter

top=Counter(known_weapon)

#Here top is a dictionary
top_list=top.most_common()
print("The top 5 weapons are-")
for t in top_list[0:5]:
    print(t[0])
    
#Task3-"Top weapon in each state with its percentage(count of weapon/total count)"
data=pandas.read_csv("database.csv", dtype=str)
import operator

temp=Counter(data["State"])
States=[]
for t in temp:
    States.append(t)
#A list which has names of all the States

def weapon_state(state):
    temp=data[data["State"]==state]
    temp_1=temp["Weapon"]
    temp_2=Counter(temp_1)
    return(temp_2)

def freq(t,raw_2):
    temp=data[data["State"]==t]
    count=0
    for i in temp["Weapon"]:
        if i==raw_2:
            count=count+1
    return(float(count)/float(len(temp))*100)
    
    

most_used_weapon_statewise=[]
print "Statewise most used weapon with its percentages are as follows-"
for t in States:
    raw_1=weapon_state(t)
    raw_2=max(raw_1.iteritems(), key=operator.itemgetter(1))[0]  #Code to find maximun in a Dict.
    fre=freq(t,raw_2)
    temp=[t,raw_2,freq(t,raw_2)]
    most_used_weapon_statewise.append(temp)
    
    
    print "%s-%s-%.2f %%." %(t,raw_2, float(fre))
#most_used_weapon_statewise

#Task4-"Bar plot of number of homicide vs year"

<<<<<<< HEAD
"""def no_of_homicides(year):
=======
def no_of_homicides(year):
>>>>>>> 2e39a7ecfd17e9b41a2ae9df14051607f159666f
    count=0
    temp=data[data["Year"]==year]
    for t in temp["Incident"]:
        count=count+int(t)
    return(count)

#To make a list of all the years
Year=[]
temp_3=Counter(data["Year"])
for t in temp_3:
    Year.append(t)
Year.sort()    
yr_vs_homicides=[]    
for t in Year:
    temp_4=no_of_homicides(t)
    yr_vs_homicides.append([temp_4])
 
temp_6=[]
for t in yr_vs_homicides:
    temp_6=temp_6+t
plt.bar(Year, temp_6,width=0.35,color='r')
plt.xlabel('Year')
#plt.ylabel('No. Of Homicides')
plt.title('No. Of Homicides')

<<<<<<< HEAD
plt.show()"""

#Task4-"Bar plot of number of homicide vs year"

""""def no_of_homicides(year):
    count=0
    temp=data[data["Year"]==year]
    for t in temp["Incident"]:
        count=count+int(t)
    return(count)

#To make a list of all the years
Year=[]
temp_3=Counter(data["Year"])
for t in temp_3:
    Year.append(t)
Year.sort()    
yr_vs_homicides=[]    
for t in Year:
    temp_4=no_of_homicides(t)
    yr_vs_homicides.append([temp_4])
 
temp_6=[]
for t in yr_vs_homicides:
    temp_6=temp_6+t
plt.bar(Year, temp_6,width=0.35,color='r')
plt.xlabel('Year')
#plt.ylabel('No. Of Homicides')
plt.title('No. Of Homicides')

plt.show()"""


import seaborn as sns
sns.countplot(data=data,x = 'Year')
plt.xticks(rotation =90)
plt.show()

=======
plt.show()
>>>>>>> 2e39a7ecfd17e9b41a2ae9df14051607f159666f
