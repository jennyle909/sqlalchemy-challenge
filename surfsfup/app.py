# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#create dictionary to hold a key, value pair
prcp_dict = {'date':'prcp'}
#################################################
# Flask Routes
#################################################
# list all the available routes
@app.route('/')
def welcome():
    return(
        f"Welcome to the home page <br/"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0<start> <br/>"
        f"/api/v1.0/<start/<end>")
    
#convert query from precipitation analysis to a dict; then return JSON representation of dict
@app.route('/api/v1.0/precipitation')
def get_precipitation():
    session =Session(engine)
    results =session.query(Measurement.date).all
    session.close()
    return jsonify(prcp_dict)
        
@app.route('/api/v1.0/stations')
def get_stations():
    session =Session(engine)
    session.close()
    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def get_tobs ():
    session =Session(engine)
    session.close()
    return jsonify(tobs)

@app.route('/api/v1.0<start>')
def get_date_start():
    session =Session(engine)
    session.close()

@app.route('/api/v1.0/<start/<end>')
def get_date_end():
    session =Session(engine)
    session.close()

if __name__ == '__main__':
    app.run(debug=True)