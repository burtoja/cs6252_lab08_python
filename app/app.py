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


@app.route('/name/<string:name>', methods=['GET'])
def get_name_details(name):
    all_names = names.get_all()
    for entry in all_names :
        if entry['name'] == name:
            return jsonify(entry), 200
    return jsonify({'message': 'Error! Name not found'}), 404 


@app.route('/name', methods=['POST'])
def add_names():
    request_data = request.get_json()
    for name_entry in request_data['names'] :
        if 'name' in name_entry :                           #check to see if the name key is in this JSON 
            if names.get(name_entry['name']) == None :      #name is not present in dictionary so need to add it
                result = names.add(name_entry) 
                name_db.write_names(result) 
                return jsonify(result), 201
            else :                                           #name is present in dictionary so no changes made
                return jsonify({'message': 'Error! Name already exists.  No changes made.'}), 400
        else :
            return jsonify({'message': 'Error! Missing name in sent data'}), 400 

    
@app.route('/name', methods=['PUT'])
def update_names():
    request_data = request.get_json()
    for name_entry in request_data['names'] :
        if 'name' in name_entry :                           #check to see if the name key is in this JSON 
            if names.get(name_entry['name']) == None :      #name is not present in dictionary so need to add it
                result = names.add(name_entry) 
                name_db.write_names(result) 
                return jsonify(result), 201
            else :                                           #name is present in dictionary so needs info update
                if 'gender' in name_entry :
                    gender = name_entry['gender'] 
                else :
                    gender = names.get(name_entry['name'])['gender']
                if 'ranking' in name_entry :
                    ranking = name_entry['ranking']
                else :
                    ranking = names.get(name_entry['name'])['ranking']
                names.delete(name_entry['name'])    
                new_entry = {'name': name_entry['name'], 'gender': gender, 'ranking': ranking}
                result = names.add(new_entry)
                name_db.write_names(result)
                return jsonify(result), 200
        else :
            return jsonify({'message': 'Error! Missing name in sent data'}), 400 


@app.route('/name/<string:name>', methods=['DELETE'])
def delete_name(name):        
        name_info = names.get(name)
        if name_info == None :
            return jsonify({'message': 'Error! Name not found'}), 404 
        else:
            names.delete(name) 
            return jsonify(name_info), 200
        
