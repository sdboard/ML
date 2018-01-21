
# coding: utf-8

# In[3]:

import pandas as whiteAndFluffy
import numpy as np
import os
import csv
whiteAndFluffy.options.display.max_rows = 200


# In[4]:

filename = ' '
global bulk_data, cleanData
bulk_data = whiteAndFluffy.read_csv(filename, error_bad_lines=False, engine='python', header = 0)
cleanData = whiteAndFluffy.DataFrame()

global states
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


# In[4]:

bulk_data


# In[10]:

bulk_data.iloc[87,0]


# In[5]:

cleanerdata1 = bulk_data.iloc[81:]


# In[6]:

cleanerdata1


# In[8]:

quiteclean = whiteAndFluffy.DataFrame()
testing = []
i = 0
curVal = bulk_data.iloc[i,0]
while (curVal != 'Purchases,' and i < len(bulk_data)):
    curVal = bulk_data.iloc[i,0]
    i = i + 1

j = i
print('WE OUT')
while j < len(bulk_data):
    testing.append(bulk_data.iloc[j])

    j = j+1
    
quiteclean2 =quiteclean.append(testing, ignore_index = True)
   


# In[11]:

quiteclean2


# In[9]:

infodata = cleanerdata1.iloc[0]


# In[10]:

cleanerdata2 = cleanerdata1.iloc[:63]


# In[11]:

cleanerdata2


# In[12]:

cleanerdata3 = cleanerdata2.iloc[:,:-9]


# In[13]:

infodata


# In[14]:

cleanerdata3


# In[15]:

cleanerdata4 = cleanerdata3.iloc[6:]


# In[16]:

cleanerdata4


# In[17]:

print(cleanerdata4.iloc[36,0])


# In[18]:

len(cleanerdata4)


# In[19]:

soclean = whiteAndFluffy.DataFrame()
testing = []
i = 0
curVal = cleanerdata4.iloc[i,0]
while curVal != 'TOTAL':
    i = i + 1;
    testing.append(cleanerdata4.iloc[i])
    curVal = cleanerdata4.iloc[i,0]
    print(i)
    
prettycleanedup =soclean.append(testing, ignore_index = True)
    
'''
for i in range(len(cleanerdata4)):
    curVal = cleanerdata4.iloc[i,0]
    #print(curVal)
    if curVal == 'TOTAL':
        print(i)
        prettycleanedup.append(cleanerdata4.iloc[i])
'''


# In[20]:

prettycleanedup


# In[21]:

dates= prettycleanedup.iloc[:,[0]]


# In[22]:

prettycleanedup2 = prettycleanedup.iloc[:,3:]


# In[23]:

prettycleanedup2


# In[24]:

description = []
charge = []
location = []
for i in range(len(prettycleanedup2)-1):
    newSeries = prettycleanedup2.iloc[i,:]
    words = []
    j = 0
    while newSeries[j] not in states:
        print(j)
        words.append(newSeries[j])
        j = j+1
    location.append(newSeries[j])
    charge.append(newSeries[j+1])
    curStr = ' '.join(words)
    description.append(curStr)
#        Series(['a', 'b', 'c']).str.cat(['A', 'B', 'C'], sep=',')
    


# In[25]:

location


# In[26]:

charge


# In[27]:

words


# In[28]:

charges = list(map(float, charge))
charges


# In[29]:

sum = 0
for item in charges:
    sum += item
sum


# In[30]:

datesDF= whiteAndFluffy.DataFrame(dates)
datesDF.columns=['date']
descriptionDF = whiteAndFluffy.DataFrame(description)
descriptionDF.columns = ['description']
chargesDF = whiteAndFluffy.DataFrame(charges)
chargesDF.columns = ['charges']
FinalData = whiteAndFluffy.concat([datesDF,descriptionDF,chargesDF], axis=1)


# In[31]:

FinalData


# In[32]:

chargesDF


# In[ ]:



