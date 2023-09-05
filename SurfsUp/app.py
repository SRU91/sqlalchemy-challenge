# Import the dependencies.
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func, and_
from sqlalchemy.orm import Session


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start<br/>"
        f"/api/v1.0/&lt;start/end<br/>"
    )

def precipitation():
    session = Session(engine)
    session.close()

def station():
    session = Session(engine)
    session.close()

def tobs():
    session = Session(engine)
    session.close()

def start():
    session = Session(engine)
    session.close()

def start_end():
    session = Session(engine)
    session.close()

if __name__ == '__main__':
    app.run(debug=True)