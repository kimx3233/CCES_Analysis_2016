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
from sqlalchemy import and_, or_, not_
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
import folium

states = ('db/statecoords.json')

votesFor = ('db/VotesFor.csv')

app = Flask(__name__)

##################################################################################################
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
#
# Debugger (active)
##################################################################################################

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

#################################################
# Homepage Route
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#################################################
# Team Page Route
#################################################

@app.route("/teamtufte")
def teamindex():
    """Return the homepage."""
    return render_template("team.html")
#################################################
# Homepage Route
#################################################

@app.route("/aboutcces")
def ccesindex():
    """Return the homepage."""
    return render_template("cces.html")
#################################################
# JSON - Column Names Route - Create a List of Names
#################################################

@app.route("/names")
def names():
    """Return a list of sample names."""

    # # Use Pandas to perform the sql query
    stmt = db.session.query(Cces).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.columns)[11:])
#################################################
# JSON - GeoJson
#################################################

@app.route("/geojson")
def geojson():
    """Return a geojson of state boundries"""
    with open('db/statecoords.json') as json_data:
        d = json.load(json_data)
        print(d)

    return jsonify(d)   
#################################################
# JSON - State Approve Percentages in JSON
#################################################

@app.route("/ApprovePerc")
def approvePerc():
    """Return a geojson of state boundries"""
    with open('db/StateApprovePerc.json') as json_data:
        d1 = json.load(json_data)
        print(d1)

    return jsonify(d1)   
##################################################################################################
# JSON - METADATA TOTALS ROUTES
##################################################################################################
#################################################
# JSON - METADATA TOTALS GunBackgroundChecks_16
#################################################
@app.route("/metadatatotalsGunBackgroundChecks_16")
def sample_metadatatotals1():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.GunBackgroundChecks_16 == "Support").count()    
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.GunBackgroundChecks_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS ProhibitPublication_16
#################################################
@app.route("/metadatatotalsProhibitPublication_16")
def sample_metadatatotals2():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.ProhibitPublication_16 == "Support").count()   
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.ProhibitPublication_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS BanAssultWeapons_16
#################################################
@app.route("/metadatatotalsBanAssultWeapons_16")
def sample_metadatatotals3():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.BanAssultWeapons_16 == "Support").count()    
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.BanAssultWeapons_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS MakeCCPEasier_16
#################################################
@app.route("/metadatatotalsMakeCCPEasier_16")
def sample_metadatatotals4():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.MakeCCPEasier_16 == "Support").count()   
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.MakeCCPEasier_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS AlwaysAllowChoice_16
#################################################
@app.route("/metadatatotalsAlwaysAllowChoice_16")
def sample_metadatatotals5():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.AlwaysAllowChoice_16 == "Support").count()    
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.AlwaysAllowChoice_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS RapeIncestorHealth_16
#################################################
@app.route("/metadatatotalsRapeIncestorHealth_16")
def sample_metadatatotals6():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.RapeIncestorHealth_16 == "Support").count()   
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.RapeIncestorHealth_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS ProhibitMoreThan20Weeks_16
#################################################
@app.route("/metadatatotalsProhibitMoreThan20Weeks_16")
def sample_metadatatotals7():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.ProhibitMoreThan20Weeks_16 == "Support").count()    
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.ProhibitMoreThan20Weeks_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS Employersdeclinebenefits_16
#################################################
@app.route("/metadatatotalsEmployersdeclinebenefits_16")
def sample_metadatatotals8():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.Employersdeclinebenefits_16 == "Support").count()   
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.Employersdeclinebenefits_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS ProhibitFedFunds_16
#################################################
@app.route("/metadatatotalsProhibitFedFunds_16")
def sample_metadatatotals9():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.ProhibitFedFunds_16 == "Support").count()   
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.ProhibitFedFunds_16 == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)

#################################################
# JSON - METADATA TOTALS GayMarriage
#################################################
@app.route("/metadatatotalsGayMarriage")
def sample_metadatatotals10():
    """Return the totals for a given sample"""

    TotalResults = {}
    
    TotalResults['Approve'] = db.session.query(Cces).filter(Cces.GayMarriage == "Support").count()    
    TotalResults['Oppose'] = db.session.query(Cces).filter(Cces.GayMarriage == "Oppose").count()

    print(TotalResults)
    return jsonify(TotalResults)
###################################################################################################################################################
###################################################################################################################################################

##################################################################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES GunBackgroundChecks_16
##################################################################################################
@app.route("/metadata_statesGunBackgroundChecks_16")

def Metadata_States1():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.GunBackgroundChecks_16), Cces.StateAbb).\
                filter(Cces.GunBackgroundChecks_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GunBackgroundChecks_16)).\
                filter(and_(Cces.GunBackgroundChecks_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GunBackgroundChecks_16)).\
                filter(and_(Cces.GunBackgroundChecks_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.GunBackgroundChecks_16)).\
                filter(Cces.GunBackgroundChecks_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GunBackgroundChecks_16)).\
                filter(and_(Cces.GunBackgroundChecks_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GunBackgroundChecks_16)).\
                filter(and_(Cces.GunBackgroundChecks_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES ProhibitPublication_16
#########################################################
@app.route("/metadata_statesProhibitPublication_16")
def Metadata_States2():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.ProhibitPublication_16), Cces.StateAbb).\
                filter(Cces.ProhibitPublication_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitPublication_16)).\
                filter(and_(Cces.ProhibitPublication_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitPublication_16)).\
                filter(and_(Cces.ProhibitPublication_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.ProhibitPublication_16)).\
                filter(Cces.ProhibitPublication_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitPublication_16)).\
                filter(and_(Cces.ProhibitPublication_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitPublication_16)).\
                filter(and_(Cces.ProhibitPublication_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)
    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES BanAssultWeapons_16
#########################################################
@app.route("/metadata_statesBanAssultWeapons_16")
def Metadata_States3():

    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.BanAssultWeapons_16), Cces.StateAbb).\
                filter(Cces.BanAssultWeapons_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.BanAssultWeapons_16)).\
                filter(and_(Cces.BanAssultWeapons_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.BanAssultWeapons_16)).\
                filter(and_(Cces.BanAssultWeapons_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.BanAssultWeapons_16)).\
                filter(Cces.BanAssultWeapons_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.BanAssultWeapons_16)).\
                filter(and_(Cces.BanAssultWeapons_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.BanAssultWeapons_16)).\
                filter(and_(Cces.BanAssultWeapons_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES MakeCCPEasier_16
#########################################################
@app.route("/metadata_statesMakeCCPEasier_16")
def Metadata_States4():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.MakeCCPEasier_16), Cces.StateAbb).\
                filter(Cces.MakeCCPEasier_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.MakeCCPEasier_16)).\
                filter(and_(Cces.MakeCCPEasier_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.MakeCCPEasier_16)).\
                filter(and_(Cces.MakeCCPEasier_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.MakeCCPEasier_16)).\
                filter(Cces.MakeCCPEasier_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.MakeCCPEasier_16)).\
                filter(and_(Cces.MakeCCPEasier_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.MakeCCPEasier_16)).\
                filter(and_(Cces.MakeCCPEasier_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES AlwaysAllowChoice_16
#########################################################
@app.route("/metadata_statesAlwaysAllowChoice_16")
def Metadata_States5():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.AlwaysAllowChoice_16), Cces.StateAbb).\
                filter(Cces.AlwaysAllowChoice_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.AlwaysAllowChoice_16)).\
                filter(and_(Cces.AlwaysAllowChoice_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.AlwaysAllowChoice_16)).\
                filter(and_(Cces.AlwaysAllowChoice_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.AlwaysAllowChoice_16)).\
                filter(Cces.AlwaysAllowChoice_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.AlwaysAllowChoice_16)).\
                filter(and_(Cces.AlwaysAllowChoice_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.AlwaysAllowChoice_16)).\
                filter(and_(Cces.AlwaysAllowChoice_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES RapeIncestorHealth_16
#########################################################
@app.route("/metadata_statesRapeIncestorHealth_16")
def Metadata_States6():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.RapeIncestorHealth_16), Cces.StateAbb).\
                filter(Cces.RapeIncestorHealth_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.RapeIncestorHealth_16)).\
                filter(and_(Cces.RapeIncestorHealth_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.RapeIncestorHealth_16)).\
                filter(and_(Cces.RapeIncestorHealth_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.RapeIncestorHealth_16)).\
                filter(Cces.RapeIncestorHealth_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.RapeIncestorHealth_16)).\
                filter(and_(Cces.RapeIncestorHealth_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.RapeIncestorHealth_16)).\
                filter(and_(Cces.RapeIncestorHealth_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES ProhibitMoreThan20Weeks_16
#########################################################
@app.route("/metadata_statesProhibitMoreThan20Weeks_16")
def Metadata_States7():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.ProhibitMoreThan20Weeks_16), Cces.StateAbb).\
                filter(Cces.ProhibitMoreThan20Weeks_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitMoreThan20Weeks_16)).\
                filter(and_(Cces.ProhibitMoreThan20Weeks_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitMoreThan20Weeks_16)).\
                filter(and_(Cces.ProhibitMoreThan20Weeks_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.ProhibitMoreThan20Weeks_16)).\
                filter(Cces.ProhibitMoreThan20Weeks_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitMoreThan20Weeks_16)).\
                filter(and_(Cces.ProhibitMoreThan20Weeks_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitMoreThan20Weeks_16)).\
                filter(and_(Cces.ProhibitMoreThan20Weeks_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES Employersdeclinebenefits_16
#########################################################
@app.route("/metadata_statesEmployersdeclinebenefits_16")
def Metadata_States8():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.Employersdeclinebenefits_16), Cces.StateAbb).\
                filter(Cces.Employersdeclinebenefits_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.Employersdeclinebenefits_16)).\
                filter(and_(Cces.Employersdeclinebenefits_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.Employersdeclinebenefits_16)).\
                filter(and_(Cces.Employersdeclinebenefits_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.Employersdeclinebenefits_16)).\
                filter(Cces.Employersdeclinebenefits_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.Employersdeclinebenefits_16)).\
                filter(and_(Cces.Employersdeclinebenefits_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.Employersdeclinebenefits_16)).\
                filter(and_(Cces.Employersdeclinebenefits_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES ProhibitFedFunds_16
#########################################################
@app.route("/metadata_statesProhibitFedFunds_16")
def Metadata_States9():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.ProhibitFedFunds_16), Cces.StateAbb).\
                filter(Cces.ProhibitFedFunds_16 == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitFedFunds_16)).\
                filter(and_(Cces.ProhibitFedFunds_16 == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitFedFunds_16)).\
                filter(and_(Cces.ProhibitFedFunds_16 == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.ProhibitFedFunds_16)).\
                filter(Cces.ProhibitFedFunds_16 == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitFedFunds_16)).\
                filter(and_(Cces.ProhibitFedFunds_16 == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.ProhibitFedFunds_16)).\
                filter(and_(Cces.ProhibitFedFunds_16 == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)

#########################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES GayMarriage
#########################################################
@app.route("/metadata_statesGayMarriage")
def Metadata_States10():
    
    # Query to create two lists of tuples (state, number)
    #S1 [4] i
    StatesFor = db.session.query(Cces.StateName, Cces.Latitude, Cces.Longitude, func.count(Cces.GayMarriage), Cces.StateAbb).\
                filter(Cces.GayMarriage == 'Support').\
                group_by(Cces.StateName).all()
    #S2 [1] m
    StatesForM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GayMarriage)).\
                filter(and_(Cces.GayMarriage == 'Support'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #S3 [1] f
    StatesForF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GayMarriage)).\
                filter(and_(Cces.GayMarriage == 'Support'),(Cces.gender == 'female')).group_by(Cces.StateName).all()
    #O1 [1] j
    StatesNot = db.session.query(Cces.StateName, func.count(Cces.GayMarriage)).\
                filter(Cces.GayMarriage == 'Oppose').\
                group_by(Cces.StateName).all()
    #O2 [1] n
    StatesNotM = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GayMarriage)).\
                filter(and_(Cces.GayMarriage == 'Oppose'),(Cces.gender == 'male')).group_by(Cces.StateName).all()
    #O3 [1] g
    StatesNotF = db.session.query(Cces.StateName, Cces.gender, func.count(Cces.GayMarriage)).\
                filter(and_(Cces.GayMarriage == 'Oppose'),(Cces.gender == 'female')).group_by(Cces.StateName).all()

    # List that will hold final dictionaries - to be jsonified
    States_Results = []
    
    for i, m, f, j, n, g in zip(StatesFor, StatesForM, StatesForF, StatesNot, StatesNotM, StatesNotF):
        
        #Determine if the state is more in support or oppose
        if i[1] > j[1]:
            tempoverall = 'Support'
        else:
            tempoverall = 'Oppose'
        
        # Return Percentages rather than just raw data
        totalVotes = i[3] + j[1]

        # Build dictionary
        tempfile = {}
        tempfile['state'] = {
            'StateName' : i[0],
            'Lat' : i[1],
            'Long' : i[2],
            'StateAbb' : i[4]
        }
        tempfile['voteTotal'] = {
            'Support' : i[3],
            'Oppose' : j[1],
            'TotalVotes' : totalVotes,
            'Support_%' : float(format(i[3] / totalVotes, '.2f')),
            'Oppose_%' : float(format(j[1] / totalVotes, '.2f')),
            'Overall' : tempoverall
        }
        tempfile['genderVote'] = {
            'MaleSupport' : m[2],
            'FemaleSupport' : f[2],
            'MaleOppose' : n[2],
            'FemaleOppose' : g[2],
            'MaleTotal' : (m[2] + n[2]),
            'FemaleTotal' : (f[2] + g[2])
        }
        tempfile['genderVotePerc'] = {
            'MaleSupport' : float(format(m[2] / totalVotes, '.2f')),
            'FemaleSupport' : float(format(f[2] / totalVotes, '.2f')),
            'MaleOppose' : float(format(n[2] / totalVotes, '.2f')),
            'FemaleOppose' : float(format(g[2] / totalVotes, '.2f')),
        }
        States_Results.append(tempfile)

    print(States_Results)
    return jsonify(States_Results)


##################################################################################################
# JSON - METADATA STATE GROUP_BY TOTALS ROUTES - NOT WORKING - BUT WITH SAMPLE VARIABLE
##################################################################################################

@app.route("/metadata_states/<sample>")
def Metadata_States(sample):
    
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
# Debugger
#################################################

if __name__ == "__main__":
    app.run(debug = True)
