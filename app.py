from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime 
from create import connection
import config

# create a Flask Instance
app = Flask(__name__)
app.url_map.strict_slashes = False


app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)



#database model

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


class announced_pu_results(db.Model):
    __tablename__ = 'announced_pu_results'

    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False)
    user_ip_address = db.Column(db.String(50), nullable=False)











# create a route decorator
@app.route('/')
def index():
    try:
        session = connection()
        cursor = session.get_cursor()

        # Execute the SQL query
        cursor.execute('USE bincomphptest;')
        cursor.execute("SELECT polling_unit_name, party_score FROM announced_pu_results INNER JOIN polling_unit ON polling_unit_uniqueid = uniqueid")
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        part = results[:6]
        pu = []
        lis = []
        for name, scor in part:
             lis.append(scor)
             pu.append(name)
             poll = pu[0]
             total = sum(lis)
             dic = f"Polling Unit Name: {poll}\nResult: {total}"

        return render_template('index.html', display=dic)
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/solution2')
def solution2():
    try:
        session = connection()
        cursor = session.get_cursor()

        # Execute the SQL query
        cursor.execute('USE bincomphptest;')
        cursor.execute("SELECT lga_name, party_score FROM lga INNER JOIN announced_pu_results  ON   uniqueid = polling_unit_uniqueid;")
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        
        #manipulation result
        lga = []
        for name, scor in results:
             if name in lga:
                continue
        else:
               lga.append(name)
            
        osn = []
        NdoE = []
        NdoW = [] 
        ope=[]
        isok = [] 
        sape= [] 
        udu=[]
        oso=[]
        ugs =[]
        ukw =[]
        uvw =[]
        bom =[]
        was =[]
        wan=[]
        bur= []
        wsw=[]
        for name, scor in results:
            if name == 'isoko South':
                isok.append(scor)
            elif name == 'Ndokwa East':
                NdoW.append(scor)
            elif name == 'Ndokwa West':
                NdoE.append(scor)
            elif name == 'Okpe':
                ope.append(scor)
            elif name == 'Sapele':
                sape.append(scor)
            elif name == 'Udu':
                udu.append(scor)
            elif name == 'Oshimili - South':
                oso.append(scor)
            elif name == 'Oshimili - North':
                osn.append(scor)
            elif name == 'Ughelli South':
                ugs.append(scor)
            elif name == 'Ukwuani':
                ukw.append(scor)
            elif name == 'Uvwie':
                uvw.append(scor)
            elif name == 'Bomadi':
                bom.append(scor)
            elif name == 'Warri North':
                wan.append(scor)
            elif name == 'Warri South':
                was.append(scor)
            elif name == 'Burutu':
                bur.append(scor)
            else:
                name = 'Warri South West'  
                wsw.append(scor)

        dic = {
        'Oshimili_North':sum(osn),
        'Ndokwa_East' :sum(NdoE),
        'Ndokwa_West' : sum(NdoW),
        'Okpe' :sum(ope),
        'isoko_South' : sum(isok),
        'sapele' : sum(sape),
        'Udu' : sum(udu),
        'Oshimili_South' : sum(oso),
        'Ughelli_South' : sum(ugs),
        'Ukwuani' : sum(ukw),
        'Uvwie' : sum(uvw),
        'Bomadi' : sum(bom),
        'Warri_South' : sum(was),
        'Warri_North' :sum(wan),
        'Burutu' : sum(bur),
        'Warri_South_West' :sum(wsw)
        }

        sort_tuple = sorted(dic.items())


        sort_data = {}
        for key, value in sort_tuple:
            sort_data[key] = value
        
        return render_template('question2.html', display=sort_data)
    except Exception as e:
        return f"An error occurred: {e}"




@app.route('/solution3')
def solution3():
    try:
        session = connection()
        cursor = session.get_cursor()

        # Execute the SQL query
        cursor.execute('USE bincomphptest;')
        cursor.execute(" SELECT partyname FROM party;")
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
    
        result = [item[0] for item in results]
        
        return render_template('question3.html', display=result)
    except Exception as e:
        return f"An error occurred: {e}"



if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)


