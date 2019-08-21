import os

import pandas as pd
import numpy as np

from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, DateTime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import *

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://///////Users/samanthamaupin/Desktop/DABCHW/Project_2/project_local/data/popular_names.sqlite'

db = SQLAlchemy(app)

metadata = MetaData()
Base = automap_base()

Base.prepare(db.engine, reflect=True)
Girl_Names = Base.classes.femalenames
Boy_Names = Base.classes.malenames
Movies = Base.classes.movies

@app.route("/")
def index():
    """/guagechart/male/<Year>/"""
    """/guagechart/female/<Year>/"""
    """/comparison/<Movie_Year>/<Baby_Year>"""
    """/male/names/<Year>"""
    """/female/names/<Year>"""
    """/number/unique/babynames"""
    """/all/femalenames"""
    """/all/malenames"""
    """/years/"""
    return render_template("index.html")

@app.route("/years/")
def years():
    results = db.session.query('DISTINCT Year FROM femalenames').all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []    
    for result in results:
        babynames_metadata = {}
        baby_something.append(result[0])
    print(baby_something)
    return jsonify(baby_something)

@app.route("/all/malenames")
def maleNAMES():
    """Return a list of colums."""
    sel = [
        Boy_Names.Name,
    ]
    results = db.session.query(*sel).all()
    # Create a dictionary entry for each row of metadata information
    malenames = []    
    for result in results:
        malenames.append(result[0])
    
    string = str(malenames)
    # .repalce("'", "").replace(",", ""))
    males = string.replace("'", "").replace(",", "")
    print(males)
    
    return jsonify(males)

@app.route("/all/femalenames")
def femaleNames():
    """Return a list of colums."""
    """Return a list of colums."""
    sel = [
        Girl_Names.Name,
    ]
    results = db.session.query(*sel).filter(Girl_Names.Rank > 24).all()
    # Create a dictionary entry for each row of metadata information
    femalenames = []    
    for result in results:
        femalenames.append(result[0])
    
    string = str(femalenames)
    # .repalce("'", "").replace(",", ""))
    females = string.replace("'", "").replace(",", "")
    print(females)
    
    return jsonify(females)

@app.route("/number/unique/babynames")
def uniquemaleNAMES():
    """Return a list of colums."""
    Mresults = db.session.query('DISTINCT Name FROM malenames').all()
    # Create a dictionary entry for each row of metadata information
    Fresults = db.session.query('DISTINCT Name FROM femalenames').all()
    unique = {
        "Unique Boy Baby Names" : len(Mresults),
        "Unique Girl Baby Names" : len(Fresults)
    }
    return jsonify(unique)


@app.route("/female/names/<Year>")
def femalenamesbyyear(Year):
    """Return a list of colums."""
    sel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]

    results = db.session.query(*sel).filter(Girl_Names.Year == Year).all()

    # Create a dictionary entry for each row of metadata information
    baby_something = []
    
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)

@app.route("/male/names/<Year>")
def malenamesbyyears(Year):
    """Return a list of colums."""
    sel = [
        Boy_Names.ID,
        Boy_Names.Name,
        Boy_Names.Year,
        Boy_Names.Gender,
        Boy_Names.Count,
        Boy_Names.Rank
    ]

    results = db.session.query(*sel).filter(Boy_Names.Year == Year).all()

    # Create a dictionary entry for each row of metadata information
    baby_something = []
    
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)


@app.route("/comparison/<Movie_Year>/<Baby_Year>")
def comparisoncharts(Movie_Year, Baby_Year):
    """Return a list of colums."""
    sel = [
        Movies.ID,
        Movies.Characters,
        Movies.Actors,
        Movies.Poster,
        Movies.Title,
        Movies.Year,
        Movies.imdbID,
    ]
    selF = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
    ]
    selM = [
        Boy_Names.ID,
        Boy_Names.Name,
        Boy_Names.Year,
    ]
    Mresults = db.session.query(*selM).filter(Boy_Names.Year == Baby_Year).limit(10)
    Fresults = db.session.query(*selF).filter(Girl_Names.Year == Baby_Year).limit(10)
    
        # Create a dictionary entry for each row of metadata information

    results = db.session.query(*sel).filter((Movies.Year == Movie_Year)).all()
    # print(results)
    movie_something = []
    Fbaby_something = []
    Mbaby_something = []
    MMmovies = []
    for result in results:
        babynames_metadata = {}
        MMmovies.append(result[1])
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Characters"] = result[1]
        babynames_metadata["Year"] = result[5]
        movie_something.append(babynames_metadata)

    for result in Fresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        Fbaby_something.append(babynames_metadata)
    for result in Mresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        Mbaby_something.append(babynames_metadata)
    # return jsonify(baby_something)
    graphdata = []
    fcounter = []
    mcounter = []
    print(MMmovies)
    fname = []
    mname = []
    
    for i in range(len(Fbaby_something)):
        Fname = Fbaby_something[i]["Name"]
        count = 0
        for j in MMmovies:
            
            k = j.replace(",", " ")
            k = k.replace("/", " ")
            k = k.replace("(", " ")
            k = k.replace(")", " ")
            k = str(k).split(" ")
            if Fname in k:
                count = count +1

        fcounter.append(count)
        fname.append(Fname)
    femalegraphdata = {
        "Names": fname,
        "Number": fcounter,
        "Year": Fbaby_something[0]["Year"]
}
    for i in range(len(Mbaby_something)):
        Mname = Mbaby_something[i]["Name"]
        count = 0
        for j in MMmovies:   
            k = j.replace(",", " ")
            k = k.replace("/", " ")
            k = k.replace("(", " ")
            k = k.replace(")", " ")
            k = str(k).split(" ")
            if Mname in k:
                count = count +1

        mcounter.append(count)
        mname.append(Mname)
    malegraphdata = {
        "Names": mname,
        "Number": mcounter,
        "Year": Mbaby_something[0]["Year"]
}

    graphdata.append(femalegraphdata)
    graphdata.append(malegraphdata)

    return jsonify(graphdata)

@app.route("/guagechart/female/<Year>/")
def femaleguageChart(Year):
    sel = [
        Girl_Names.Name,
        Girl_Names.Year
    ]

    results = db.session.query(*sel).filter(Girl_Names.Year == Year).all()
    movieResults = db.session.query(Movies.Characters).all()

    movie_something = []
    Fbaby_something = []
    MMmovies = []
    for result in movieResults:
        babynames_metadata = {}
        MMmovies.append(result[0])
        babynames_metadata["Characters"] = result[0]
        movie_something.append(babynames_metadata)

    for result in results:
        babynames_metadata = {}
        babynames_metadata["Name"] = result[0]
        babynames_metadata["Year"] = int(result[1])
        Fbaby_something.append(babynames_metadata)

    print(MMmovies)


    fcounter = []
    fname = []
    
    for i in range(len(Fbaby_something)):
        Fname = Fbaby_something[i]["Name"]
        count = 0
        for j in MMmovies:
            
            k = j.replace(",", " ")
            k = k.replace("/", " ")
            k = k.replace("(", " ")
            k = k.replace(")", " ")
            k = str(k).split(" ")
            if Fname in k:
                count = count +1

        fcounter.append(count)
        fname.append(Fname)
    guagedata = {
        "Names": fname,
        "Number": fcounter,
        "Year": Fbaby_something[0]["Year"]}
    
    return jsonify(guagedata)


@app.route("/guagechart/male/<Year>/")
def maleguageChart(Year):
    sel = [
        Boy_Names.Name,
        Boy_Names.Year
    ]

    results = db.session.query(*sel).filter(Boy_Names.Year == Year).all()
    movieResults = db.session.query(Movies.Characters).all()

    movie_something = []
    Mbaby_something = []
    MMmovies = []
    for result in movieResults:
        babynames_metadata = {}
        MMmovies.append(result[0])
        babynames_metadata["Characters"] = result[0]
        movie_something.append(babynames_metadata)

    for result in results:
        babynames_metadata = {}
        babynames_metadata["Name"] = result[0]
        babynames_metadata["Year"] = int(result[1])
        Mbaby_something.append(babynames_metadata)

    print(MMmovies)


    mcounter = []
    mname = []
    
    for i in range(len(Mbaby_something)):
        Mname = Mbaby_something[i]["Name"]
        count = 0
        for j in MMmovies:
            
            k = j.replace(",", " ")
            k = k.replace("/", " ")
            k = k.replace("(", " ")
            k = k.replace(")", " ")
            k = str(k).split(" ")
            if Mname in k:
                count = count +1

        mcounter.append(count)
        mname.append(Mname)
    guagedata = {
        "Names": mname,
        "Number": mcounter,
        "Year": Mbaby_something[0]["Year"]}
    
    return jsonify(guagedata)

@app.route("/female/names/<Name>")
def femalenames(Name):
    """Return the MetaData for a given sample."""
    sel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]

    results = db.session.query(*sel).filter(Girl_Names.Name == Name).all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)




@app.route("/male/names/<Name>")
def malenames(Name):
    """Return a list of colums."""
    sel = [
        Boy_Names.ID,
        Boy_Names.Name,
        Boy_Names.Year,
        Boy_Names.Gender,
        Boy_Names.Count,
        Boy_Names.Rank
    ]

    results = db.session.query(*sel).filter(Boy_Names.Name == Name).all()

    # Create a dictionary entry for each row of metadata information
    baby_something = []
    
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)

    print(baby_something)
    return jsonify(baby_something)


@app.route("/baby/years/<Year>")
def babynamesbyyear(Year):
    """Return a list of colums."""
    Msel = [
        Boy_Names.ID,
        Boy_Names.Name,
        Boy_Names.Year,
        Boy_Names.Gender,
        Boy_Names.Count,
        Boy_Names.Rank
    ]
    Fsel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]
    Mresults = db.session.query(*Msel).filter(Boy_Names.Year == Year).all()
    Fresults = db.session.query(*Fsel).filter(Girl_Names.Year == Year).all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []
    
    for result in Fresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    for result in Mresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)

@app.route("/female/names")
def females():
    """Return the MetaData for a given sample."""
    sel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]

    results = db.session.query(*sel).filter(Girl_Names.Gender == "F").all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)
@app.route("/male/names")
def males():
    """Return the MetaData for a given sample."""
    sel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]

    results = db.session.query(*sel).filter(Boy_Names.Gender == "M").all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)

@app.route("/baby/names/<Name>")
def names(Name):
    """Return a list of colums."""
    Msel = [
        Boy_Names.ID,
        Boy_Names.Name,
        Boy_Names.Year,
        Boy_Names.Gender,
        Boy_Names.Count,
        Boy_Names.Rank
    ]
    Fsel = [
        Girl_Names.ID,
        Girl_Names.Name,
        Girl_Names.Year,
        Girl_Names.Gender,
        Girl_Names.Count,
        Girl_Names.Rank
    ]
    Mresults = db.session.query(*Msel).filter(Boy_Names.Name == Name).all()
    Fresults = db.session.query(*Fsel).filter(Girl_Names.Name == Name).all()
    # Create a dictionary entry for each row of metadata information
    baby_something = []
    
    for result in Fresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    for result in Mresults:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Name"] = result[1]
        babynames_metadata["Year"] = int(result[2])
        babynames_metadata["Gender"] = result[3]
        babynames_metadata["Count"] = int(result[4])
        babynames_metadata["Rank"] = int(result[5])
        baby_something.append(babynames_metadata)
    print(baby_something)
    return jsonify(baby_something)


@app.route("/movie/years/<Year>")
def movieyears(Year):
    """Return a list of colums."""
    sel = [
        Movies.ID,
        Movies.Characters,
        Movies.Actors,
        Movies.Director,
        Movies.Genre,
        Movies.Metascore,
        Movies.Poster,
        Movies.Title,
        Movies.Writer,
        Movies.Year,
        Movies.imdbID,
        Movies.imdbRating,
        Movies.imdbVotes
    ]
    results = db.session.query(*sel).filter(Movies.Year == Year).all()
    print(results)
    baby_something = []
    
    for result in results:
        babynames_metadata = {}
        babynames_metadata["Id"] = result[0]
        babynames_metadata["Characters"] = result[1]
        babynames_metadata["Actors"] = result[2]
        babynames_metadata["Director"] = result[3]
        babynames_metadata["Genre"] = result[4]
        babynames_metadata["Metascore"] = result[5]
        babynames_metadata["Poster"] = result[6]
        babynames_metadata["Title"] = result[7]
        babynames_metadata["Writer"] = result[8]
        babynames_metadata["Year"] = result[9]
        babynames_metadata["imdbID"] = result[10]
        babynames_metadata["imdbRating"] = result[11]
        babynames_metadata["imdbVotes"] = result[12]
        baby_something.append(babynames_metadata)
        print(baby_something)
    
    return jsonify(baby_something)







if __name__ == "__main__":
    app.run()
