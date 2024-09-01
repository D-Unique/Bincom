from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
import config

# create a Flask Instance
app = Flask(__name__)

#add database


app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)



#create tables

class announced_lga_results(db.Model):

    __tablename__ = 'announced_lga_results'

    result_id = db.Column( db.Integer, primary_key=True , autoincrement=True)

    lga_name=  db.Column( db.String(50), nullable=False)

    party_abbreviation = db.Column(db.String(4), nullable=False)

    party_score = db.Column(db.Integer,   nullable=False)

    entered_by_user = db.Column(db.String(50), nullable=False)

    date_entered = db.Column(db.DateTime, nullable=True) 

    user_ip_address = db.Column(db.String(50), nullable=False) 


class announced_pu_results(db.Model):
    __tablename__ = 'announced_pu_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)



class announced_state_results(db.Model):
    __tablename__ = 'announced_state_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.String(30), nullable=True)
    user_ip_address = db.Column(db.String(50), nullable=False)



class announced_ward_results(db.Model):
    __tablename__ = 'announced_ward_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ward_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.String(30), nullable=True)
    user_ip_address = db.Column(db.String(50), nullable=False)


class lga(db.Model):
    __tablename__ = 'lga'

    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lga_id = db.Column(db.Integer, nullable=False)
    lga_name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    lga_description = db.Column(db.Text)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.String(30), nullable=True)
    user_ip_address = db.Column(db.String(50), nullable=False)



class polling_unit(db.Model):
    __tablename__ = 'polling_unit'

    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    polling_unit_id = db.Column(db.Integer, nullable=False)
    ward_id = db.Column(db.Integer, nullable=False)
    lga_id = db.Column(db.Integer, nullable=False)
    uniquewardid = db.Column(db.Integer)
    polling_unit_number = db.Column(db.String(50))
    polling_unit_name = db.Column(db.String(50))
    polling_unit_description = db.Column(db.Text)
    lat = db.Column(db.String(255))
    long = db.Column(db.String(255))
    entered_by_user = db.Column(db.String(50))
    date_entered = db.Column(db.String(30))
    user_ip_address = db.Column(db.String(50))


class party(db.Model):
    __tablename__ = 'party'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    partyid = db.Column(db.String(11), nullable=False)
    partyname = db.Column(db.String(11), nullable=False)


class states(db.Model):
    __tablename__ = 'states'

    state_id = db.Column(db.Integer, primary_key=True)
    state_name = db.Column(db.String(50), nullable=False)

class ward(db.Model):
    __tablename__ = 'ward'

    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ward_id = db.Column(db.Integer, nullable=False)
    ward_name = db.Column(db.String(50), nullable=False)
    lga_id = db.Column(db.Integer, nullable=False)
    ward_description = db.Column(db.Text)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.String(30), default=None)
    user_ip_address = db.Column(db.String(50), nullable=False)



with app.app_context():
    db.create_all()
    print('Done')
