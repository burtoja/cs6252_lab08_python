'''
Created on Feb 20, 2020

@author: CS6252
'''
import json

class NameDB:
    """
    NameDB provides methods to read and write to names.json
    
    File names.json is a JSON file representing a dictionary 
    with the single key "names" that is mapped to a name list.
    The name list is a list of dictionaries where each dictionary 
    contains the key "name" that is mapped to a unique name in the
    name list.
    """
    def read_names(self):
        """
        Reads and returns all name entries from file names.json
        
        Precondition: none
        Postcondition: none
        Returns None if the names.json cannot be read; otherwise, 
        returns a list of names where each name is a dictionary 
        containing at least the key "name" that is mapped to a 
        unique name in the list of names
        """ 
        try:
            with open ('names.json') as names_json :
                name_list = []
                name_data = json.load(names_json)
                for name_entry in name_data['names'] :
                    name_list.append(name_entry)
                    print('NAME LIST: {}'.format(name_list))                
                return name_list
        except:
            return None
    
    
    def write_names(self, name_object_list):
        """
        write the given list of names to names.json
        
        Precondition: name_object_list is a list of dictionaries, 
        each dictionary contains the key "name" that is mapped to 
        a unique name in the list of name dictionaries.
        Postcondition: names.json contains the JSON representation of
        the name_object_list, where the list is wrapped in a 
        dictionary entry with key "names"
        """
        with open('names.json') as names_json:
            data = json.load(names_json)
            temp = data['names']
            temp.append(name_object_list)
        with open('names.json', 'w') as names_json: 
            json.dump(data, names_json)
            