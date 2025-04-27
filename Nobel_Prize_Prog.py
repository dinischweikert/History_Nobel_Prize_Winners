#!/usr/bin/env python
# coding: utf-8

# The Nobel Prize has been among the most prestigious international awards since 1901. Each year, 
# awards are bestowed in chemistry, literature, physics, physiology or medicine, economics, and peace. 
# In addition to the honor, prestige, and substantial prize money, the recipient also gets a gold medal 
# with an image of Alfred Nobel (1833 - 1896), who established the prize.
# 
# The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards 
# from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available 
# in the `nobel.csv` file. In this project, we explore and answer several questions related to this 
# prizewinning data. 


# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Read in data
df = pd.read_csv('nobel.csv')

#######################################################################################################
# most commonly awarded gender and birth country
#######################################################################################################
top_gender = df['sex'].mode()
top_country = df['birth_country'].mode()

#######################################################################################################
# decade with the highest ratio of US-born nobel prize winners to total winners split out decades
#######################################################################################################
def get_decade(year):
    return year // 10 * 10

df['usa_born_winner'] = df['birth_country'] == 'United States of America'
df['decade'] = df['year'].apply(get_decade)
prop_usa_winners = df.groupby('decade', as_index=False)['usa_born_winner'].mean()

# highest ratio of US-born nobel prize winners
max_decade_usa = prop_usa_winners[prop_usa_winners['usa_born_winner'] == prop_usa_winners['usa_born_winner'].max()]['decade'].values[0]

#######################################################################################################
# decade and nobel prize category combination had highest proportion of female winners
#######################################################################################################
df['female_winner'] = df['sex'] == 'Female'

prop_female_winner = df.groupby(['decade', 'category'],as_index=False)['female_winner'].mean()

# create dictionary
decade_key = prop_female_winner.loc[prop_female_winner['female_winner'] == prop_female_winner['female_winner'].max()]['decade'].values[0]
category_value = prop_female_winner.loc[prop_female_winner['female_winner'] == prop_female_winner['female_winner'].max()]['category'].values[0]

max_female_dict = {decade_key: category_value}

#######################################################################################################
# first woman to receive a nobel price and in what category
#######################################################################################################
female_df = df.loc[df['sex'] == 'Female']

# first woman name
first_woman_name = female_df.loc[female_df['year'] == female_df['year'].min()]['full_name'].values[0]

# first woman category
first_woman_category = female_df.loc[female_df['year'] == female_df['year'].min()]['category'].values[0]

#######################################################################################################
# individuals/organizations that have won more than 1 nobel prize
#######################################################################################################
name_list = []
repeat_list = []
name_list = df['full_name'].unique()
for name in name_list:
    if len(df.loc[df['full_name']==name]) > 1:
        repeat_list.append(name)


