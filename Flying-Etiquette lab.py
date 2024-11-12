#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# In[10]:


df = pd.read_csv('flying-etiquette.csv')


# In[6]:


# display the first few rows and summary
df.head()
df.info()
df.describe(include='all')


# In[8]:


#3a: Create a copy of the height column
df['Height (Inches)'] = df['How tall are you?']

#3b: Normalize the height values
def height_to_inches(height):
    if height == 'Under 5 ft.':
        return 60  # 5'0"
    elif height.startswith('6\''):
        return 78  # 6'6"
    else:
        feet, inches = map(int, height.split("'"))
        return feet * 12 + inches

# Apply the conversion
df['Height (Inches)'] = df['Height (Inches)'].apply(height_to_inches)


# In[ ]:


# visualize age breakdown, x and y axis shown below
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Age', order=df['Age'].value_counts().index)
plt.title('Percent Breakdown of Survey Participants by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


# display seat switching
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Switch Seat Rude', order=df['Switch Seat Rude'].value_counts().index)
plt.title('Feelings on Asking to Switch Seats')
plt.xlabel('Is it rude to ask to switch seats?')
plt.ylabel('Number of Respondents')
plt.xticks(rotation=45)
plt.show()


# In[ ]:


# display age and seat Switching responses
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Age', hue='Switch Seat Rude')
plt.title('Age vs. Perception of Switching Seats')
plt.xlabel('Age Range')
plt.ylabel('Number of Respondents')
plt.legend(title='Is it rude?', loc='upper right')
plt.show()


# In[ ]:


# display the relationship between reclining and height
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Recline Seat', y='Height (Inches)')
plt.title('Relationship Between Reclining and Height')
plt.xlabel('Do You Recline Your Seat?')
plt.ylabel('Height (Inches)')
plt.show()

