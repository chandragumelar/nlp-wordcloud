#!/usr/bin/env python
# coding: utf-8

# In[14]:


import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[12]:


# construct the path
file_path = os.path.join(cwd, 'data/SDFB_people.csv')

# read the file
df = pd.read_csv(file_path)
df.head()


# In[15]:


# get all the text that is not null
histsign = df['Historical Significance'][-pd.isnull(df['Historical Significance'])]
text = ' '.join(histsign)

# making wordcloud
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

