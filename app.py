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
# App Contents
#
# Database Setup
# Define Sample Names and Query Addresses
#
# Routes
# Homepage Route (@app.route("/")) - HTML Template
# Names Route (@app.route("/names")) - JSON
# Metadata Totals (@app.route("/metadatatotals/<sample>")) - JSON
# Metadata States Groupy (@app.route("/metadata_states/<sample>")) - JSON
# Example of hard Coded Query (@app.route("/metadata/GunBC")) - JSON
#
# Debugger (not active)
#################################################

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

#################################################
# Define Sample Names and Query Addresses
#################################################
# Gun Questions
GunBackgroundChecks_16 = Cces.GunBackgroundChecks_16
ProhibitPublication_16 = Cces.ProhibitPublication_16
BanAssultWeapons_16 = Cces.BanAssultWeapons_16
MakeCCPEasier_16 = Cces.MakeCCPEasier_16

# Abortion Questions
AlwaysAllowChoice_16 = Cces.AlwaysAllowChoice_16
RapeIncestorHealth_16 = Cces.RapeIncestorHealth_16
ProhibitMoreThan20Weeks_16 = Cces.ProhibitMoreThan20Weeks_16
Employersdeclinebenefits_16 = Cces.Employersdeclinebenefits_16
ProhibitFedFunds_16 = Cces.ProhibitFedFunds_16

# Gay Marriage Question
GayMarriage = Cces.GayMarriage

#################################################
# Homepage Route
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#################################################
# JSON - Column Names Route
#################################################

@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = session.query(Cces).statement
    df = pd.read_sql_query(stmt, session.bind)

    # Return a list of the column names (sample names - start with the 8th column since columns 0-7 are respondent profile, not survey responses)
    return jsonify(list(df.columns)[8:])

#################################################
# JSON - Totals Route - returning 2, 4, or 6 results
#################################################

@app.route("/metadatatotals/<sample>")
def sample_metadatatotals(sample):
    """Return the totals for a given sample"""
    TotalResults = []
    
    TotalApprove = {}
    TotalOppose = {}
    
    ApproveTemp = session.query(Cces).filter(sample == 'Support').count()
    TotalApprove['Approve'] = ApproveTemp
    TotalResults.append(TotalApprove)
    
    OpposeTemp = session.query(Cces).filter(sample == 'Oppose').count()
    TotalOppose['Oppose'] = OpposeTemp
    TotalResults.append(TotalOppose)

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - State Totals Route based on Dropdown
#################################################

@app.route("/metadata_states/<sample>")
def Metadata_States(sample):
    
    # Query to create two lists of tuples (state, number)
    StatesFor = session.query(Cces.StateName, func.count(sample)).\
                filter(sample == 'Support').\
                group_by(Cces.StateName).all()
    StatesNot = session.query(Cces.StateName, func.count(sample)).\
                filter(sample == 'Oppose').\
                group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, j in zip(StatesFor, StatesNot):

        tempfile = {}
        tempfile['State'] = i[0]
        tempfile['Support'] = i[1]
        tempfile['Oppose'] = j[1]
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        tempfile['Overall'] = tempoverall

        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#################################################
# JSON - Example JSON return for a single hard-coded query on Gun Background Checks
#################################################
@app.route("/metadata/GunBC")
def sample_metadata():


    StatesFor = session.query(Cces.StateName, func.count(Cces.GunBackgroundChecks_16)).filter(Cces.GunBackgroundChecks_16 == 'Support').group_by(Cces.StateName).all()
    StatesNot = session.query(Cces.StateName, func.count(Cces.GunBackgroundChecks_16)).filter(Cces.GunBackgroundChecks_16 == 'Oppose').group_by(Cces.StateName).all()

    # Create a dictionary entry for each row of metadata information
    SecondTry = []

    for i, j in zip(StatesFor, StatesNot):

        tempfile = {}
        tempfile['State'] = i[0]
        tempfile['Support'] = i[1]
        tempfile['Oppose'] = j[1]
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        tempfile['Overall'] = tempoverall
            
        SecondTry.append(tempfile)


    print(SecondTry)
    return jsonify(SecondTry)

#################################################
# Debugger
#################################################

if __name__ == "__main__":
    app.run()
