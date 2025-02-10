# εναλλακτική λύση, υλοποίηση από Βασίλη Νάστο (14/4/2022) με χρήση pandas

import os,pandas as pd
from tabulate import tabulate

file_to_movies_len_ratings=os.path.join('','src','ml-100k','u.data')
file_to_movies_len_names=os.path.join('','src','ml-100k','u.item')

if __name__ == '__main__':
    # read data
    ratings=pd.read_csv(file_to_movies_len_ratings,sep='\t',names=['user id','movie id','rating','timestamp']).drop(['timestamp'],axis=1)
    desc_movie_info=pd.read_csv(file_to_movies_len_names,sep='|',encoding = "ISO-8859-1",usecols=[0,1],names=['movie id','movie name'])
    
    # group data per movie_id
    ratings=ratings.groupby(['movie id'],sort=False).agg({'user id':'count','rating':'mean'})

    # search for mean rating value of movies with # of ratings>50
    top_10=ratings[ratings['user id']>50].sort_values(['rating'],ascending=False).head(10)
    
    # find top_10 movie names
    n=desc_movie_info[desc_movie_info['movie id'].isin(top_10.index)]
    top_10['movie name']=[n.iloc[i]['movie name'] for j in top_10.index for i in range(n.shape[0]) if n.iloc[i]['movie id']==j]
    
    # print data in tabulate format
    print(tabulate(top_10,headers=['#USERS','RATING','MOVIE NAME'],showindex=False,tablefmt='fancy_grid'))