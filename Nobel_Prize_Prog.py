#!/usr/bin/env python
# coding: utf-8

# The Nobel Prize has been among the most prestigious international awards since 1901. Each year, awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. In addition to the honor, prestige, and substantial prize money, the recipient also gets a gold medal with an image of Alfred Nobel (1833 - 1896), who established the prize.
# 
# ![](Nobel_Prize.png)
# 
# The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available in the `nobel.csv` file in the `data` folder.
# 
# In this project, you'll get a chance to explore and answer several questions related to this prizewinning data. And we encourage you then to explore further questions that you're interested in!

# In[6]:


# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Read in data
df = pd.read_csv('nobel.csv')

# most commonly awarded gender and birth country
top_gender = df['sex'].mode()
top_country = df['birth_country'].mode()

# decade with the highest ratio of US-born norbel prize winners to total winners
# split out decades
def get_decade(year):
    return year // 10 * 10

df['decade'] = df['year'].apply(get_decade)




