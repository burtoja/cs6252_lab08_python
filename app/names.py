'''
Created on Feb 20, 2020

@author: CS6252
'''
class Names:
    """
    Maintains a list of names
    
    The data ember self.names is a list of dictionaries.
    Each dictionary contains the key "name" which must have
    a unique value among all dictionaries.
    """
    
    def __init__(self, names):
        self.names = names
    
        
    def get_all(self):
        """
        returns the list of dictionaries representing names
        """
        return self.names
    
    
    def get(self, name):
        """
        Returns the dictionary with key-0vaue pair ("name", name)
        
        Returns None if the dictionary with the specified name is not 
        contained in  this list of names; otherwise, retruns the 
        dictionary with the specified name
        """
        for name_object in self.names:
            if name_object['name'] == name:
                return name_object
        return None 
    
    
    def add(self, new_name_object):
        """
        Adds a new dictionary representing a name
        
        Returns None if the specified dictionary does not contain 
        the kay "name" or if the key "name" is mapped to  aname that 
        is already included in this name list; otherwise, returns the 
        added dictionary representing a name
        """
        if not 'name' in new_name_object:
            return None
        
        new_name = new_name_object['name']
        if self.get(new_name) != None:
            return None
        
        self.names.append(new_name_object)
        return new_name_object
    
    
    def delete(self, name):
        """
        Deletes the dictionary with the key-value pair ("name", name)
        
        Returns None if the dictionary with the specified name is not 
        contained in this list of names; otherwise, retruns the deleted 
        dictionary 
        """
        remove_name_object = None
        for name_object in self.names:
            if name_object['name'] == name:
                remove_name_object = name_object
        
        if remove_name_object == None:
            return None
        
        self.names.remove(remove_name_object)
        return remove_name_object
    
