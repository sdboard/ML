
# coding: utf-8

# In[33]:

import numpy as np
import pandas as whiteAndFluffy
whiteAndFluffy.options.display.max_rows = 200
whiteAndFluffy.options.display.max_columns = 30
import os
#import csv
filename = ' '# eg /Users/username/foldername/filename.csv
global bulk_data, cleanData, states
bulk_data = whiteAndFluffy.read_csv(filename, error_bad_lines=False, engine='python', header = 0)
cleanData = whiteAndFluffy.DataFrame()
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


# In[34]:

#bulk_data


# In[42]:

period = whiteAndFluffy.DataFrame()
info = []
i = 0
curVal = bulk_data.iloc[i,0]
while (curVal != 'Statement' and i < len(bulk_data)):
    curVal = bulk_data.iloc[i,0]
    i = i + 1
i = i - 1
info.append(bulk_data.iloc[i,3])
info.append(bulk_data.iloc[i,4])
info.append(bulk_data.iloc[i,5])
period = period.append(info, ignore_index = True)


# In[43]:

#period


# In[44]:

quiteclean = whiteAndFluffy.DataFrame()
selection = []
i = 0
curVal = bulk_data.iloc[i,0]
while (curVal != 'Purchases,' and i < len(bulk_data)):
    curVal = bulk_data.iloc[i,0]
    i = i + 1
while curVal != 'TOTAL':
    selection.append(bulk_data.iloc[i])
    i = i + 1;
    curVal = bulk_data.iloc[i,0]       
quiteclean =quiteclean.append(selection, ignore_index = True)


# In[45]:

#quiteclean


# In[46]:

dates= quiteclean.iloc[:,[0]]
#dates


# In[47]:

description = []
charge = []
location = []
for i in range(len(quiteclean)):
    newSeries = quiteclean.iloc[i,:]
    words = []
    j = 3
    while newSeries[j] not in states:
        words.append(newSeries[j])
        j = j + 1
    location.append(newSeries[j])
    charge.append(newSeries[j+1])
    curStr = ' '.join(words)
    description.append(curStr)   


# In[48]:

#location


# In[49]:

#charge


# In[50]:

#words


# In[51]:

#description


# In[52]:

charges = list(map(float, charge))
#charges


# In[65]:

sum = 0
for item in charges:
    sum += item
print('it\'s ' + str(int(sum - 1.9)))


# In[58]:

datesDF= whiteAndFluffy.DataFrame(dates)
datesDF.columns=['date']
descriptionDF = whiteAndFluffy.DataFrame(description)
descriptionDF.columns = ['description']
chargesDF = whiteAndFluffy.DataFrame(charges)
chargesDF.columns = ['charges']
locationDF = whiteAndFluffy.DataFrame(location)
locationDF.columns = ['state']
GoodData = whiteAndFluffy.concat([datesDF,descriptionDF,locationDF,chargesDF], axis=1)


# In[59]:

GoodData


# In[ ]:




# In[ ]:



