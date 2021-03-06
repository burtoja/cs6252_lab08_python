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


@app.route('/name/<name>', methods=['GET'])
def get_name_details(name):
    all_names = names.get_all()
    for entry in all_names :
        if entry['name'] == name:
            return jsonify(entry), 200
    return jsonify({'message': 'Error! Name not found'}), 404 


@app.route('/name', methods=['POST'])
def add_names():
    post_request_data = request.get_json()
    if 'name' in post_request_data :                           
        if names.get(post_request_data['name']) == None :     
            result = names.add(post_request_data) 
            name_db.write_names(result) 
            return jsonify(result), 201
        else :                                           
            return jsonify({'message': 'Error! Name already exists.  No changes made.'}), 400
    else :
        return jsonify({'message': 'Error! Missing name in sent data'}), 400 

    
@app.route('/name', methods=['PUT'])
def update_names():
    post_request_data = request.get_json()
    if 'name' in post_request_data :                           
        local_entry = names.get(post_request_data['name'])        
        if local_entry == None :                             
            local_result = names.add(post_request_data) 
            name_db.write_names(local_result) 
            return jsonify(local_result), 201
        else :                                          
            post_keys = []
            for post_key in post_request_data :
                post_keys.append(post_key)
            for local_key in local_entry :
                if local_key not in post_keys :
                    post_request_data.update( {local_key : local_entry[local_key]} )
            names.delete(post_request_data['name'])  
            local_result = names.add(post_request_data)
            name_db.write_names(post_request_data)
            return jsonify(post_request_data), 200
    else :
        return jsonify({'message': 'Error! Missing name in sent data'}), 400 


@app.route('/name/<name>', methods=['DELETE'])
def delete_name(name):        
        name_info = names.get(name)
        if name_info == None :
            return jsonify({'message': 'Error! Name not found'}), 404 
        else:
            names.delete(name) 
            return jsonify(name_info), 200
        
        
        
        