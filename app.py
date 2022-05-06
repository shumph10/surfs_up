#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import sqlalchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import flask dependencies
from flask import Flask, jsonify

#create the engine
engine = create_engine("sqlite:///hawaii.sqlite")

#relect the db into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#save references to a table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session 
session = Session(engine)


#close the session

#set up flask - create the application and name it
app = Flask(__name__)
##ex of how to export the app.py files into a python file names example.py - name would need to be set to example
# import app

# print("example __name__ = %s", __name__)

# if __name__ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported")
    ##when you run the script with python app.py the __name__ variable will be set to __main__
        ## --indicates that we are not using any other file to run this code??

#define routes (has to be after the app is created)
@app.route("/")
#def a function with f strings in the return statement to ref all other routes
    #lets ppl know where to go to access other routes available
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end

    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    #calc the date one year ago from the most recent date in the db
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #write a query to get the date and precip for the prev year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    #create a dictionary to hold return w/ date as key and precip as value
    precip = {date: prcp for date, prcp in precipitation}
    #return a jsonified version of the dictionary created
    return jsonify(precip)

    #naming convention /api/v1.0/ is followed by the name of the route
        #signifies that this is version 1 of our app
        #update that line for future versions of the app
@app.route("/api/v1.0/stations")
#define a stations funct
def stations():
     #write a query to get all the stations in the db
    results = session.query(Station.station).all()
    #start by unraveling our results into a 1D array - use functionnp.ravel() to do so with results as the parameter
    stations = list(np.ravel(results))
    #return a jsonified list of arrayed results
    return jsonify(stations=stations)
    #need to add stations=station to return our list formatted as a json
    #making data=data makes jsonify treat the arguments as a dictionary of values
    ##kinda like doing df[df[]] to get the values in the correct format??

@app.route("/api/v1.0/tobs")
def temp_montly():
    #calc date a year ago from the last in the db
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query the primary station for all temp observations for the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    #unravel the results into a 1D array and convert the array into a list
    temps = list(np.ravel(results))
    #return the jsonified list
    return jsonify(temps=temps)

#make a route to report the min, average, and max temps
    #need to provide both a starting and ending date
#create starting route
@app.route("/api/v1.0/temp/<start>")

#create ending route
@app.route("/api/v1.0/temp/<start>/<end>")
#def a funct to put statistics code in
    #add start and end parameter - set both to none for now
def stats(start=None, end=None):
    #create a query to select min, ave, and max temp from db
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    #add an if-not statement to the code to det a starting and ending date
        #will help query our db using the list we made
        #then unravel results into a 1D array then jsonify them
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    #now calc the temp avg min and max with the start and end dates
    #use the sel list which is the data points we need to collect

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)




# if __name__ =="__main__"
#     app.run(port= "5000", debug = True)
session.close()