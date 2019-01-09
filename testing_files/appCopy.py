import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#################################################
# APP TABLE OF CONTENTS - THIS SECTION IS JUST COMMENTS - NOT MEANT TO BE CODE:
#
# Database Setup
# Define Sample Names and Query Addresses
#
# Routes
# Homepage Route (@app.route("/")) - HTML Template
# Names Route (@app.route("/names")) - JSON - List of strings
# Metadata Totals (@app.route("/metadatatotals/<sample>")) - JSON - List of Dict
# Metadata States Groupy (@app.route("/metadata_states/<sample>")) - JSON - List of Dict
# Example of hard Coded Query (@app.route("/metadata/GunBC")) - JSON - List of Dict
#
# Debugger (active)
#################################################

#################################################
# Database Setup
#################################################
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/CCES_Ver61.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to the table
Cces = Base.classes.Cces_16

# engine = create_engine("sqlite:///db/CCES_Ver50.sqlite")
# conn = engine.connect()
# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)
# # Save reference to the table
# Cces = Base.classes.CCES_16
# # Create our session (link) from Python to the DB
# session = Session(engine)

#################################################
# Define Sample Names and Query Addresses
#################################################
# Gun Questions
# GunBackgroundChecks_16 = Cces.GunBackgroundChecks_16
# ProhibitPublication_16 = Cces.ProhibitPublication_16
# BanAssultWeapons_16 = Cces.BanAssultWeapons_16
# MakeCCPEasier_16 = Cces.MakeCCPEasier_16

# # Abortion Questions
# AlwaysAllowChoice_16 = Cces.AlwaysAllowChoice_16
# RapeIncestorHealth_16 = Cces.RapeIncestorHealth_16
# ProhibitMoreThan20Weeks_16 = Cces.ProhibitMoreThan20Weeks_16
# Employersdeclinebenefits_16 = Cces.Employersdeclinebenefits_16
# ProhibitFedFunds_16 = Cces.ProhibitFedFunds_16

# # Gay Marriage Question
# GayMarriage = Cces.GayMarriage

#################################################
# Homepage Route
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#################################################
# JSON - Column Names Route - Create a List of Names
#################################################

@app.route("/names")
def names():
    """Return a list of sample names."""

    # # Use Pandas to perform the sql query
    stmt = db.session.query(Cces).statement
    df = pd.read_sql_query(stmt, db.session.bind)

##################################################################

    # GunBackgroundChecks_16 = Cces.GunBackgroundChecks_16
    # ProhibitPublication_16 = Cces.ProhibitPublication_16
    # BanAssultWeapons_16 = Cces.BanAssultWeapons_16
    # MakeCCPEasier_16 = Cces.MakeCCPEasier_16
    # AlwaysAllowChoice_16 = Cces.AlwaysAllowChoice_16
    # RapeIncestorHealth_16 = Cces.RapeIncestorHealth_16
    # ProhibitMoreThan20Weeks_16 = Cces.ProhibitMoreThan20Weeks_16
    # Employersdeclinebenefits_16 = Cces.Employersdeclinebenefits_16
    # ProhibitFedFunds_16 = Cces.ProhibitFedFunds_16
    # GayMarriage = Cces.GayMarriage

    # dropDownList = [GunBackgroundChecks_16, ProhibitPublication_16, BanAssultWeapons_16, MakeCCPEasier_16, AlwaysAllowChoice_16,
    #                 RapeIncestorHealth_16, RapeIncestorHealth_16, ProhibitMoreThan20Weeks_16, Employersdeclinebenefits_16,
    #                 ProhibitFedFunds_16, GayMarriage]
    ###############################################################
    # Return a list of the column names (sample names - start with the 11th column since columns 0-7 are respondent profile, not survey responses)
    return jsonify(list(df.columns)[11:])
    # return jsonify(dropDownList)
#################################################
# JSON - Totals Route - returning 2, 4, or 6 results
#################################################

@app.route("/metadatatotals/GunBackgroundChecks_16")
def sample_metadatatotals():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    ApproveTemp = db.session.query(Cces).filter(Cces.GunBackgroundChecks_16 == "Support").count()
    TotalResults['Approve'] = ApproveTemp
    
    OpposeTemp = db.session.query(Cces).filter(Cces.GunBackgroundChecks_16 == "Oppose").count()
    TotalResults['Oppose'] = OpposeTemp

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - State Totals Route based on Dropdown
#################################################

@app.route("/metadata_states/<sample>")
def Metadata_States(sample):
    sample = str(sample)
    # Query to create two lists of tuples (state, number)
    StatesFor = db.session.query(Cces.StateName, func.count(Cces.sample)).\
                filter(Cces.sample == 'Support').\
                group_by(Cces.StateName).all()
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.sample)).\
                filter(Cces.sample == 'Oppose').\
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
@app.route("/metadata/GunBackgroundChecks_16")
def sample_metadata():


    StatesFor = db.session.query(Cces.StateName, func.count(Cces.GunBackgroundChecks_16)).filter(Cces.GunBackgroundChecks_16 == 'Support').group_by(Cces.StateName).all()
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.GunBackgroundChecks_16)).filter(Cces.GunBackgroundChecks_16 == 'Oppose').group_by(Cces.StateName).all()

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
    app.run(debug = True)
