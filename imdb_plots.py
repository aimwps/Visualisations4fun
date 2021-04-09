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
    #print(imdb.head())
    gb_bracket = imdb.groupby(["bracket", "genre"]).release_year.count().reset_index()
    year_slices = gb_bracket['bracket'].unique()
    print(year_slices)
    print(type(year_slices))
    graph_data = []
    for year in year_slices:
        graph_data.append((str(year), gb_bracket[gb_bracket.bracket == year]))

    # last_year = graph_data[-1]
    # plt.figure(figsize=(10,10))
    # plt.scatter(x=)
    # transform_brackets_to_strings = group_brackets["bracket"].astype(str)
    # group_brackets['bracket']= transform_brackets_to_strings


    #print(type(x.iloc[0]))

    #check = imdb[imdb['bracket'] == '(1920, 1925]']
    #print(check)
    # check = imdb[imdb['genre']=='Western']
    # check2 = check[check['release_year'] > 2015]
    # print(len(check2))

    #gb = imdb.groupby([ "brackets"]).genre.count().reset_index()
    #print(gb.head(100))
# click_source_by_month_pivot = click_source_by_month.pivot(columns='month',
# index='utm_source',
# values='id').reset_index()


genre_by_year(imdb)
#released_by_year(imdb)
