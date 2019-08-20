import sqlite3
import csv
import codecs

conn = sqlite3.connect("OMdbmovies.sqlite")

cur = conn.cursor()

cur.execute("CREATE TABLE movies(ID PRIMARY KEY, Actors VARCHAR, Awards VARCHAR, BoxOffice VARCHAR, Country VARCHAR, DVD VARCHAR, Director VARCHAR, Genre VARCHAR, Metascore NUMERIC, Plot VARCHAR, Poster VARCHAR, Rated NUMERIC, Ratings NUMERIC, Released NUMERIC, Runtime NUMERIC, Title VARCHAR, Type VARCHAR, Website VARCHAR, Writer VARCHAR, Year NUMERIC, imdbID NUMERIC, imdbRating NUMERIC, imdbVotes NUMERIC)")

reader = open("project_2/data/OMdb.csv", "rb")
read = csv.reader(codecs.iterdecode(reader, 'utf-8'))
for row in read:
    # ,0Actors,A1wards,2BoxOffice,3Country,4DVD,5Director,E6rror,7Genre,8Language,9Metascore110,11Plot,12Poster,13Production,14Rated,15Ratings,16Released,17Response18,Runtime,T19itle,20Type,21Website,22Writer,23Year,24imdbID,i25mdbRating,26imdbVotes,27totalSeasons
    myData = [row[0], row[1], row[2], row[3], row[4], row[5], row[7], row[9], row[10], row[11], row[13], row[14], row[15], row[16], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25]]
    cur.execute("INSERT INTO movies (Actors, Awards, BoxOffice, Country,DVD, Director, Genre, Metascore, Plot, Poster, Rated, Ratings,Released, Runtime, Title, Type, Website, Writer, Year, imdbID,imdbRating, imdbVotes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", myData)
conn.commit()