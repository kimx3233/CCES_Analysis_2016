import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db/CCES_Ver50.sqlite")
conn = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save reference to the table
Cces = Base.classes.CCES_16
# Create our session (link) from Python to the DB
session = Session(engine)




@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = session.query(Cces).statement
    df = pd.read_sql_query(stmt, session.bind)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        Cces.GunBackgroundChecks_16
        
        
    ]

    GBCfor = session.query(*sel).filter(Cces.GunBackgroundChecks_16 == 'Support').count()
    GBCno = session.query(*sel).filter(Cces.GunBackgroundChecks_16 == 'Oppose').count()

    # Create a dictionary entry for each row of metadata information
    sample_metadata = {}
    sample_metadata["GBCfor"] = GBCfor
    sample_metadata["GBCno"] = GBCno
    
        

    print(sample_metadata)
    return jsonify(sample_metadata)



if __name__ == "__main__":
    app.run()
