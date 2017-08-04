import pandas as pd
from pandas import DataFrame, Series

movies = pd.read_csv("http://bit.ly/imdbratings")
#How do I filter rows of a pandas DataFrame by column value?
#two methods
m = movies[movies.duration >= 200]['star_rating']
m = movies.loc[movies.duration >= 200, 'star_rating']
#print m.head()

#How do I apply multiple filter criteria to a pandas DataFrame?
#can not use "and, or", you shoule use "&, |"
m1 = movies[(movies.duration >= 200) & (movies.star_rating > 8.5)]
m1 = movies[movies.genre.isin(['Crime', "Drama"]) & (movies.duration >= 200)]
#print m1.head()

#How do I sort a pandas DataFrame or a Series?
#This is Series method
m2 = movies.star_rating.sort_values()
#This is DataFrame method
m2 = movies.sort_values('star_rating', ascending=False)
print m2.head()
