import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns


imdb  = pd.read_csv("data/top_50_genre_movies_2021-04-09.csv")
#print(imdb.info())
####################################################################################
### SPLIT AND CLEAN ACTORS INTO SEPERATE COLUMNS                               #####

# Split the genres into new dataframe
genre_split = imdb['sub-genre'].str.split(', ', expand=True)

# Add the genres back into the dataframe
imdb[["sub_genre_1", "sub_genre_2", "sub_genre_3"]] = genre_split[[0,1,2]]

# Drop the original genre column from data dataframe
imdb.drop(['sub-genre'], axis=1, inplace=True)

#####################################################################################
#### SPLIT AND CLEAN ACTORS INTO SEPERATE COLUMNS                               #####

# Split actors into seperate columns
actor_split = imdb['starring'].str.split(', ', expand=True)

# remove any columns after 5 actors as most are none values
made_the_cut = actor_split.drop([5,6,7,8,9,10,11,12,13,14],axis=1)

# add the remaining back to the orignal dataframe
imdb[['actor1', 'actor2', 'actor3', 'actor4', 'actor5']] = made_the_cut[[0,1,2,3,4]]

# Remove original column containing actors from dataframe
imdb.drop(['starring'], axis=1, inplace=True)

#####################################################################################
####                                                                            #####
print(imdb.head())
#print(imdb[["genre", "sub_genre_1","sub_genre_2","sub_genre_3"]])
def released_by_year(df):
    counts = df.groupby('release_year')["genre"].count()
    years = sorted(df['release_year'].unique())

    plt.figure(figsize=(10,10))
    plt.plot(years,counts)
    plt.title("Trend of movies that made got rated in imdb genre top 50 movies by year")
    plt.grid()
    plt.show()

def genre_by_year(df):
    imdb = df[['release_year','genre']]
    imdb["bracket"] = pd.cut(imdb.release_year, [i for i in range(1920, 2025,5)])
    gb = imdb.groupby(["bracket", "genre"]).count().reset_index()
    ch = imdb['bracket'].astype(str)

    imdb.plot(type="scatter")



    # gb['bracket'] = ch
    # gb.columns = ["bracket", "genre", "count"]
    # plt.figure(figsize=(10,10))
    # plt.plot(gb['bracket'], gb['count'])
    # plt.show()
    # # for bracket in gb['bracket'].unique():
    #     plt.plot()
    # print(gb.info())




    # #print(imdb.head())
    # #gb_bracket = imdb.groupby(["bracket", "genre"]).count().reset_index()
    # # year_slices = gb_bracket['bracket'].unique()
    #
    # plt.figure(figsize=(10,10))
    # genres = imdb['genre'].unique()
    # print(genres)
    # plt.plot()
    #
    # graph_data = []
    # for year in year_slices:
    #     graph_data.append((str(year), gb_bracket[gb_bracket.bracket == year]))
    #




genre_by_year(imdb)
#released_by_year(imdb)
