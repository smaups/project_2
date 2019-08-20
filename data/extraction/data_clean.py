import sqlite3
import csv
import codecs
import pandas as pd
import numpy as np


# cnx = sqlite3.connect('/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_2/data/babynames.sqlite')

# df = pd.read_sql_query("SELECT * FROM NationalNames", cnx)

# df1 = df[df['Year'] > 1988].reset_index()
# df_Female = df1[df1["Gender"] != "M"]
# df_Male = df1[df1["Gender"] != "F"]


# df2Female = pd.DataFrame([])
# for x in range(1989,2015):
#     df2Female = df2Female.append(df_Female[df_Female.Year == x][:100])
# df2Male = pd.DataFrame([])
# for x in range(1989,2015):
#     df2Male = df2Male.append(df_Male[df_Male.Year == x][:100])

# group1 = df2Female.groupby('Year')
# df2Female["Rank"] = group1["Count"].rank()
# print(df2Female)

# group2 = df2Male.groupby('Year')
# df2Male["Rank"] = group2["Count"].rank()
# print(df2Male)

# df2Female.to_csv('./Female_Names.csv')
# df2Male.to_csv('./Male_Names.csv')


# omdb = pd.read_csv('/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_2/data/OMdb.csv')
# imdb = pd.read_csv('/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_2/data/final_character_names.csv')

# omdb_df = omdb[["Actors", "Country", "Director", "Genre", "Metascore", "Poster", "Ratings", "Title", "Writer", "Year", "imdbID", "imdbRating", "imdbVotes"]]

# movie_df = omdb_df.merge(imdb, on=['imdbID'])

# movie_df.head()

# movie_df.to_csv('./Movies.csv')


conn = sqlite3.connect("names_data.sqlite")

cur = conn.cursor()


cur.execute("CREATE TABLE femalenames(ID VARCHAR PRIMARY KEY, Name VARCHAR, Year NUMERIC, Gender VARCHAR, Count NUMERIC, Rank NUMERIC)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Female_Names.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:

    myData = [row[0], row[3], row[4], row[5], row[6], row[7]]
    cur.execute("INSERT INTO femalenames (ID, Name, Year, Gender, Count, Rank) VALUES (?, ?, ?, ?, ?, ?);", myData)
conn.commit()

cur.execute("CREATE TABLE malenames(ID VARCHAR PRIMARY KEY, Name VARCHAR, Year NUMERIC, Gender VARCHAR, Count NUMERIC, Rank NUMERIC)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Male_Names.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:
    if row[0] == str():
        pass
    else:
        myData = [row[0], row[3], row[4], row[5], row[6], row[7]]
        cur.execute("INSERT INTO malenames (ID, Name, Year, Gender, Count, Rank) VALUES (?, ?, ?, ?, ?, ?);", myData)
conn.commit()

cur.execute("CREATE TABLE movies(ID INT PRIMARY KEY, Characters VARCHAR, Actors VARCHAR, Director VARCHAR, Genre VARCHAR, Metascore INT, Poster VARCHAR, Title VARCHAR, Writer VARCHAR, Year INT, imdbID VARCHAR, imdbRating INT, imdbVotes INT)")

reader = open("/Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/Movies.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:

    myData = [row[0], row[14], row[1], row[3], row[4], row[5], row[6], row[8], row[9], row[10], row[11], row[12], row[13]]
    cur.execute("INSERT INTO movies (ID, Characters, Actors, Director, Genre, Metascore, Poster, Title, Writer, Year, imdbID, imdbRating, imdbVotes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", myData)
conn.commit()

conn.close()