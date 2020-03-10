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
    return json.dumps({"names": all_names}), 200

@app.route('/names', methods=['POST'])
def add_names():
    request_data = request.get_json()
    for name_entry in request_data['names'] :
        result = names.add(name_entry)
        print('NAME LIST RETURN VALUE = {}'.format(result))
        name_db.write_names(result)
    return jsonify(result)
    
@app.route('/name/<string:name>')
def get_name_details(name):
    all_names = names.get_all()
    for entry in all_names :
        if entry['name'] == name:
            return jsonify(entry), 200
    return jsonify({'message': 'name not found'}), 404 

