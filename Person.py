import numpy as np


class Person():
    """person object for Family Tree 
    -----------
    Attributes:
    ----------
    name : str
        The name of the person.
    birth_year : int
        The year the person was born.
    parent: Person
        parent of the person
    death_year : int
        The year the person died. None if the person is still alive.
    hashed_name : str
        Just saving the name in hashed form for security.
    children : List of 'Person' Object
        The person's children. None if no child. 
    """
    kind = 'person'
    all_persons = []
    def __init__(self,name,birth_day,parent,death_day = None):
        self.name = name
        self.birth_day = birth_day
        self.death_day = death_day
        self.hashed_name = self.Hash(name)
        self.parent = parent
        if parent is not None:
            self.level = parent.level + 1
        else:
            self.level = 1
        
        self.children = []
        Person.all_persons.append(self)        
    def AddChild(self,child):
        """add a person to this person's children.
        input: 
            child : Person 
        return:
            None
        """
        self.children.append(child)
    def __del__(self):
        Person.all_persons.remove(self)
    def Hash(self,name):
        return ' '            
    