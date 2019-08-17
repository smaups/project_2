import os

import pandas as pd
import numpy as np


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import *

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data/names_data.sqlite'

db = SQLAlchemy(app)

metadata = MetaData()
Base = automap_base()

Base.prepare(db.engine, reflect=True)
Girl_Names = Base.classes.femalenames
Boy_Names = Base.classes.malenames
Movies = Base.classes.movies


# from sqlalchemy import inspect
# inspector = inspect(db.engine)
# print(inspector.get_table_names())
# columns = inspector.get_columns('movies')
# for c in columns:
#     print(c['name'], c["type"])


# movies = Table('movies', metadata,
# Column('ID', Integer, primary_key=True),
# Column('Characters', String),
# Column("Actors", String),
# Column("Director", String),
# Column("Genre", String),
# Column('Metascore', Integer),
# Column("Poster", String),
# Column("Title", String),
# Column("Writer", String),ID
# Column('Year', Integer),
# Column("imdbID", String),
# Column('imdbRating', Integer),
# Column('imdbVotes', Integer),
# autoload=True, autoload_with=db.engine)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/female/years/<Year>")
def femaleyears(Year):
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

@app.route("/male/years/<Year>")
def maleyears(Year):
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
def years(Year):
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
        babynames_metadata["Title"] = result[8]
        babynames_metadata["Writer"] = result[9]
        babynames_metadata["Year"] = result[10]
        babynames_metadata["imdbID"] = result[11]
        babynames_metadata["imdbRating"] = result[11]
        babynames_metadata["imdbVotes"] = result[12]
        baby_something.append(babynames_metadata)
        print(baby_something)
    return jsonify(baby_something)


if __name__ == "__main__":
    app.run()
