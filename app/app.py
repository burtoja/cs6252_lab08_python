'''
Created on Feb 20, 2020

@author: CS6252
'''
from flask import Flask, request, jsonify
from names import Names
from name_db import NameDB
import json

app = Flask(__name__)
name_db = NameDB()
names = Names(name_db.read_names())

@app.route('/names')
def get_names():
    all_names = names.get_all()
    print('========RAW ALL NAMES: {}'.format(all_names))
    return json.dumps({"names": all_names}), 200;

@app.route('/names', methods=['POST'])
def add_names():
    request_data = request.get_json()
    print('-------------POST REQUEST DATA: {} -----------------'.format(request_data['names']))
    print('*************VERIFY NAME SENT:  {} *****************'.format(request_data['names'][0]['name']))
    for name_entry in request_data['names'] :
        print('-------------LOOP DATA: {} -----------------'.format(name_entry))
        print('+++++++++++++PLEASE PRINT NAME: {}'.format(name_entry['name']))
        result = names.add(name_entry)
        print('NAME LIST RETURN VALUE = {}'.format(result))
        name_db.write_names(result)
    return jsonify(result)
    
    

