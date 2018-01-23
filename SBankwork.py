
# coding: utf-8

# In[138]:

import numpy as np
import pandas as whiteAndFluffy
whiteAndFluffy.options.display.max_rows = 200
whiteAndFluffy.options.display.max_columns = 30
import os
#import csv
filename = ' ' #eg /Users/username/direcotry/folder/filename.csv
global bulk_data, cleanData, states
bulk_data = whiteAndFluffy.read_csv(filename, error_bad_lines=False, engine='python', header = 0)
cleanData = whiteAndFluffy.DataFrame()
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


# In[159]:

def isanan(value):
    try:
        np.isnan(value)
        return True
    except ValueError:
        return False


# In[140]:

bulk_data


# In[141]:

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


# In[142]:

period


# In[143]:

quiteclean = whiteAndFluffy.DataFrame()
selection = []
i = 0
curVal = bulk_data.iloc[i,0]
while (curVal != 'Purchases,' and i < len(bulk_data)):
    curVal = bulk_data.iloc[i,0]
    i = i + 1
while curVal != 'TOTAL':
    if curVal == 'Detach':
        while (curVal != 'Purchases,' and i < len(bulk_data)):
            curVal = bulk_data.iloc[i,0]
            i = i + 1
    selection.append(bulk_data.iloc[i])
    i = i + 1;
    curVal = bulk_data.iloc[i,0]       
quiteclean =quiteclean.append(selection, ignore_index = True)


# In[144]:

quiteclean


# In[165]:

whiteAndFluffy.isnull(quiteclean.iloc[4,7])


# In[146]:

dates= quiteclean.iloc[:,[0]]
#dates


# In[176]:

description = []
charge = []
location = []
for i in range(len(quiteclean)):
    newSeries = quiteclean.iloc[i,:]
    words = []
    j = 3
    while not whiteAndFluffy.isnull(newSeries[j]):
        if j > 5:
            words.append(newSeries[j-3])
        j = j + 1
    location.append(newSeries[j-2])
    charge.append(newSeries[j-1])
    curStr = ' '.join(words)
    description.append(curStr)   

'''description = []
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
    description.append(curStr)'''   


# In[177]:

location


# In[178]:

charge


# In[179]:

#words


# In[180]:

#description


# In[181]:

charges = list(map(float, charge))
#charges


# In[182]:

sum = 0
for item in charges:
    sum += item
print('it\'s ' + str(int(sum - 1.9)))


# In[183]:

datesDF= whiteAndFluffy.DataFrame(dates)
datesDF.columns=['date']
descriptionDF = whiteAndFluffy.DataFrame(description)
descriptionDF.columns = ['description']
chargesDF = whiteAndFluffy.DataFrame(charges)
chargesDF.columns = ['charges']
locationDF = whiteAndFluffy.DataFrame(location)
locationDF.columns = ['state']
GoodData = whiteAndFluffy.concat([datesDF,descriptionDF,locationDF,chargesDF], axis=1)


# In[184]:

GoodData


# In[186]:

Cat = whiteAndFluffy.DataFrame({"Category":['groceries','food','education','food','travel','water','groceries','health','groceries','travel','food','groceries','food','music','groceries','groceries','taxes','taxes','parking','taxes','water','food','fuel','parking','groceries','education'], 
                                "Outcome":['living','personal','business','personal','personal','living','living','living','living','personal','personal','living','personal','personal','living','living','business','business','business','business','living','personal','business','business','living','business']})


# In[188]:

GoodData = whiteAndFluffy.concat([GoodData,Cat], axis = 1)


# In[189]:

GoodData


# In[89]:

GoodDataJan = GoodData


# In[90]:

GoodDataJan = GoodData


# In[91]:

GoodDataJan


# In[190]:

GoodDataFeb = GoodData


# In[191]:

GoodDataFeb


# In[195]:

TotalGoodDataTF = GoodDataJan.append(GoodDataFeb, ignore_index = True)


# In[196]:

TotalGoodDataTF


# In[199]:

TotalGoodDataTF.to_csv(path_or_buf=' ') #eg /Users/username/Desktop/TotalData.csv


# In[ ]:



