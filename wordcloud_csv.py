#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[7]:


# construct the path
cwd = os.getcwd()
file_path = os.path.join(cwd, 'data/live.csv')

# read the file
df = pd.read_csv(file_path)
df.head()


# In[8]:


# get all the text that is not null
histsign = df['title'][-pd.isnull(df['title'])]
text = ' '.join(histsign)

# making wordcloud
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

