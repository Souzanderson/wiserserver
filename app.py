from flask import Flask 
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from beans.dbmongo import DbMongo
import hashlib
import json

import datetime
db = DbMongo(json.load(open('beans/config.json'))['urldb'],'wizer_education')
# db = DbMongo('localhost','wiser_education')

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "http://localhost:3000"}})

# ROTAS

@app.route("/") 
@cross_origin(origin='http://localhost:3000',headers=['Content- Type','Authorization'])
def home(): 
    return jsonify({"name":"API Wiser test", "version": "1.0.0"})



@app.route("/login", methods=['POST']) 
@cross_origin(origin='http://localhost:3000',headers=['Content- Type','Authorization'])
def login():
    try:
        js = request.get_json()
        resp = db.select('user',{"email": js['email']})
        if(hashlib.md5(str(js['email']+js['senha']).encode()).hexdigest()== resp[0]['hascode']):
            return jsonify({'sucess': 'Login permitido!'})
        else:
            return jsonify({'passerror': 'Password inválido!'})
    except Exception as e:
        print(e)
        return jsonify({"usererror": "Usuário inválido!"})
    
if __name__ == '__main__':
    app.run()