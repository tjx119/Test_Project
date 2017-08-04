#Note: First array elements raised to powers from second array
import pandas as pd
from pandas import DataFrame, Series

movies = pd.read_csv("http://bit.ly/imdbratings")
#m = movies[movies.duration >= 200]['star_rating']
m = movies.loc[movies.duration <= 120]
print m.head()
print type(m)
