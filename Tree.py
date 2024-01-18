from Person import Person

class FamilyTree():
    def __init__ (self, grandfather,):
        self.root = grandfather
        self.size = 1
        self.max_lvl = 1
        self.All = dict()
        self.All[self.root.name] = {self.root.birth_day  : self.root}
        
    
    def FindPerson (self, person_name, person_birthday,root = None):
        """Gets a person by name and birthday and tell us if it exists   
        input: 
            person_name,person_birthday
        return:
            None 
        """
        qeue = []
        root = self.root if root is None else root
        qeue.append(root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                if c.name == person_name and c.birth_day == person_birthday:
                    return c
                qeue.append(c)
        print('person with name: ' + person_name , 'and birthday: ' + person_birthday , ' not found in ', root.name,'\'s child')
        return None    
    
    def AddPerson (self,dad_name,dad_birthday,child_name,child_birthday,child_deathday=None):
        """Gets tow persons by name and birthday then add child   
        input: 
            dad_name,dad_birthday,child_name,child_birthday,child_deathday=None
        return:
            None 
        """
        dad = self.FindPerson(dad_name,dad_birthday)
        if dad != None:
            child = Person(child_name,child_birthday,dad,child_deathday)
            dad.AddChild(child)
            self.All[child_name] = {child_birthday : child }
        return           
    
    def RemovePerson (self,person_name,person_birthday):
        """Gets a person by name and birthday and removes it from family tree (if it exists)   
        input: 
            person_name,person_birthday
        return:
            None 
        """
        print('Removing a person will remove all his children')
        a = input("you sure you want to remove? /n(Yes|No)")
        if not (a.lower() == 'yes' or a.lower() == 'y'):
            print('not removing so!')
            return
        qeue = []
        qeue.append(self.root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                if c.name == person_name and c.birth_day == person_birthday:
                    k.children.remove(c)
                    print('successfully removed ')
                    return
                qeue.append(c)
        print('person with name: ' + person_name , 'and birthday: ' + person_birthday , ' not found!')
        return        
    
    def GetSize(self):
        """returning size of family tree   
        input: 
            None
        return:
            size 
        """
        qeue = []
        size = 0
        qeue.append(self.root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                qeue.append(c)
            size +=1
        print('size: ' + size)
        return size
     
    def FindParent(self,dad_name,dad_birthday,child_name,child_birthday):
        """Gets tow persons by name and birthday then find if some on is chile of another one
            not only his child but also child of his child and so on!
        input: 
            dad_name,dad_birthday,child_name,child_birthday
        return:
            None 
        """
        dad = self.FindPerson(dad_name,dad_birthday)
        if dad is None:
            return False
        child = self.FindChild(child_name,child_birthday,root = dad)
        if child is None:    
            print(dad_name ,'is not father of ',child_name)
            return False
        else:
            print(dad_name ,' is father of ',child_name)
            return True
    
    def FindLCA(self,person1_name, person1_birthday ,person2_name, person2_birthday):
        """Gets tow persons by name and birthday then find lowest common ancestor of them
        input: 
            person1_name, person1_birthday ,person2_name, person2_birthday
        return:
            None 
        """  
        person1 = self.FindPerson(person1_name, person1_birthday)
        person2 = self.FindPerson(person2_name, person2_birthday)
        if person1 is None or person2 is None:
            return
        dad1_list = []
        dad2_list = []
        
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
    