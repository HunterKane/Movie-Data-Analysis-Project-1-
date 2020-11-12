#!/usr/bin/env python
# coding: utf-8

# # Project 1: Explanatory Data Analysis & Data Presentation (Movies Dataset)

# # Project Brief for Self-Coders

# Here you´ll have the opportunity to code major parts of Project 1 on your own. If you need any help or inspiration, have a look at the Videos or the Jupyter Notebook with the full code. <br> <br>
# Keep in mind that it´s all about __getting the right results/conclusions__. It´s not about finding the identical code. Things can be coded in many different ways. Even if you come to the same conclusions, it´s very unlikely that we have the very same code. 

# ## Data Import and first Inspection

# 1. __Import__ the movies dataset from the CSV file "movies_complete.csv". __Inspect__ the data.

# __Some additional information on Features/Columns__:

# * **id:** The ID of the movie (clear/unique identifier).
# * **title:** The Official Title of the movie.
# * **tagline:** The tagline of the movie.
# * **release_date:** Theatrical Release Date of the movie.
# * **genres:** Genres associated with the movie.
# * **belongs_to_collection:** Gives information on the movie series/franchise the particular film belongs to.
# * **original_language:** The language in which the movie was originally shot in.
# * **budget_musd:** The budget of the movie in million dollars.
# * **revenue_musd:** The total revenue of the movie in million dollars.
# * **production_companies:** Production companies involved with the making of the movie.
# * **production_countries:** Countries where the movie was shot/produced in.
# * **vote_count:** The number of votes by users, as counted by TMDB.
# * **vote_average:** The average rating of the movie.
# * **popularity:** The Popularity Score assigned by TMDB.
# * **runtime:** The runtime of the movie in minutes.
# * **overview:** A brief blurb of the movie.
# * **spoken_languages:** Spoken languages in the film.
# * **poster_path:** The URL of the poster image.
# * **cast:** (Main) Actors appearing in the movie.
# * **cast_size:** number of Actors appearing in the movie.
# * **director:** Director of the movie.
# * **crew_size:** Size of the film crew (incl. director, excl. actors).

# In[4]:


#import libraries needed for the data 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
pd.options.display.max_columns = 30 
pd.options.display.float_format = '{:.2f}'.format


# # Load data and explore basic info

# In[6]:


#load movie data info  
df = pd.read_csv("movies_complete.csv", parse_dates= ["release_date"])


# In[36]:


df.count()


# In[10]:


df.info()


# In[12]:


#Explore genre types
df.genres[1]


# In[14]:


#Explore cast for one movie
df.cast[1]


# In[17]:


#Pull up summary of data 
df.describe()


# In[21]:


# Put data into his
df.hist(figsize = (20,12), bins = 100)
plt.show()


# In[27]:


#Explore budget value and count. Do not drop null values 
df.budget_musd.value_counts(dropna = False).head(20)


# In[26]:


#Explore revenue value and count. Do not drop null values
df.revenue_musd.value_counts(dropna = False).head(20)


# In[30]:


#Summary with object included
df.describe(include= "object")


# In[35]:


#Explore a title with multiply entries 
df[df.title == "Cinderella"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## The best and the worst movies...

# 2. __Filter__ the Dataset and __find the best/worst n Movies__ with the

# - Highest Revenue
# - Highest Budget
# - Highest Profit (=Revenue - Budget)
# - Lowest Profit (=Revenue - Budget)
# - Highest Return on Investment (=Revenue / Budget) (only movies with Budget >= 10) 
# - Lowest Return on Investment (=Revenue / Budget) (only movies with Budget >= 10)
# - Highest number of Votes
# - Highest Rating (only movies with 10 or more Ratings)
# - Lowest Rating (only movies with 10 or more Ratings)
# - Highest Popularity

# __Define__ an appropriate __user-defined function__ to reuse code.

# __Movies Top 5 - Highest Revenue__

# In[ ]:





# __Movies Top 5 - Highest Budget__

# In[ ]:





# __Movies Top 5 - Highest Profit__

# In[ ]:





# __Movies Top 5 - Lowest Profit__

# In[ ]:





# __Movies Top 5 - Highest ROI__

# In[ ]:





# __Movies Top 5 - Lowest ROI__

# In[ ]:





# __Movies Top 5 - Most Votes__

# In[ ]:





# __Movies Top 5 - Highest Rating__

# In[ ]:





# __Movies Top 5 - Lowest Rating__

# In[ ]:





# __Movies Top 5 - Most Popular__

# In[ ]:





# ## Find your next Movie

# 3. __Filter__ the Dataset for movies that meet the following conditions:

# __Search 1: Science Fiction Action Movie with Bruce Willis (sorted from high to low Rating)__

# __Search 2: Movies with Uma Thurman and directed by Quentin Tarantino (sorted from short to long runtime)__

# __Search 3: Most Successful Pixar Studio Movies between 2010 and 2015 (sorted from high to low Revenue)__

# __Search 4: Action or Thriller Movie with original language English and minimum Rating of 7.5 (most recent movies first)__

# In[ ]:





# ## Are Franchises more successful?

# 4. __Analyze__ the Dataset and __find out whether Franchises (Movies that belong to a collection) are more successful than stand-alone movies__ in terms of:

# - mean revenue
# - median Return on Investment
# - mean budget raised
# - mean popularity
# - mean rating

# hint: use groupby()

# __Franchise vs. Stand-alone: Average Revenue__

# In[ ]:





# __Franchise vs. Stand-alone: Return on Investment / Profitability (median)__

# In[ ]:





# __Franchise vs. Stand-alone: Average Budget__

# In[ ]:





# __Franchise vs. Stand-alone: Average Popularity__

# In[ ]:





# __Franchise vs. Stand-alone: Average Rating__

# In[ ]:





# ## Most Successful Franchises

# 5. __Find__ the __most successful Franchises__ in terms of

# - __total number of movies__
# - __total & mean budget__
# - __total & mean revenue__
# - __mean rating__

# In[ ]:





# ## Most Successful Directors

# 6. __Find__ the __most successful Directors__ in terms of

# - __total number of movies__
# - __total revenue__
# - __mean rating__

# In[ ]:




