import numpy as np


class Person():
    """person object for Family Tree 
    -----------
    Attributes:
    ----------
    name : str
        The name of the person.
    gender : str
        The person is women or men.
    birth_year : int
        The year the person was born.
    death_year : int
        The year the person died. None if the person is still alive.
    hashed_name : str
        Just saving the name in hashed form for security.
    mother : 'Person' object
        The person's mother. None if not known.
    father : 'Person' object
        The person's father. None if not known.
    children : List of 'Person' Object
        The person's children. None if no child. 
    """
    kind = 'person'
    def __init__(self,name,birth_day,father,death_day = None,children=''):
        self.name = name
        self.birth_day = birth_day
        self.death_day = death_day
        self.hashed_name = self.Hash(name)
        self.father = father
        self.children = []
        for i in children.strip().split(","):
            if len(i):
                self.children.append(Person(i.split(" ")[0],i.split(" ")[1],i.split(" ")[2]))
                self.children[-1].father = self
                
    def AddChild(self, name,birth_day,death_day = None):
        """add a person to this person's children.
        input: 
            child informations (name,birth_day,death_day = None)
        return:
            None
        """
        self.children.append(Person(name,birth_day,self,death_day,))
                
    