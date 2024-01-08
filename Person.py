import numpy as np


class person():
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
    def __init__(self,name,gender,birth_day,death_day = None,mother=None,father=None,children=''):
        self.name = name
        self.birth_day = birth_day
        self.death_day = death_day
        self.hashed_name = self.Hash(name)
        self.mother = mother
        self.father = father
        self.children = []
        self.gender = gender
        for i in children.strip().split(","):
            if len(i):
                self.children.append(person(i.split(" ")[0],i.split(" ")[1],i.split(" ")[2]))
                if self.gender == "male":
                    self.children[-1].father = self
                else:
                    self.children[-1].mother = self
    def AddChild(self, name,gender,birth_day,death_day = None,mother=None,father=None):
        """add a person to this person's children.
        input: 
            child informations (name,gender,birth_day,death_day = None,mother = None,father = None)
        return:
            None
        """
        if self.gender == 'male':
            father = self
        else:
            mother = self
        self.children.append(person(name,gender,birth_day,death_day,mother,father))
        
    def FindParent(name1, name2):
        """Gets tow persons by name and find if one is child of other one
        input: 
            name1,name2
        return:
            True if name1 is child of name2 (or vice versa) and False otherwise
        """
        pass
    
    def FindLeastCommonSubsumer(name1, name2):
        pass
     
    def FindRelation(name1, name2):
        """Gets tow persons by name and find relationships between them
        input: 
            name1,name2
        return:
            relationship 
        """
        pass
    
    def FindFarestBorn(name1):
        pass
    
    def FindFarestRelations():
        pass
    
    def Hash(self):
        return ' '