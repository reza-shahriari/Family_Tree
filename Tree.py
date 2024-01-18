from Person import Person

class FamilyTree():
    def __init__ (self, grandfather_name,grandfather_birthday,grandfather_deathday=None):
        self.root = Person(grandfather_name,grandfather_birthday,None,grandfather_deathday)
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
        if self.root.name == person_name and self.root.birth_day == person_birthday:
            return self.root
        else:
            print("Not a root!")
            print(self.root)
            print(self.root.name)
            print(self.root.birth_day)
        qeue = []
        root = self.root if root is None else root
        qeue.append(root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                if c.name == person_name and c.birth_day == person_birthday:
                    return c
                qeue.append(c)
        return 'person with name: ' + person_name , 'and birthday: ' + str(person_birthday) , ' not found in ', root.name,'\'s child'
    
    def AddPerson (self,parent_name,parent_birthday,child_name,child_birthday,child_deathday=None):
        """Gets tow persons by name and birthday then add child   
        input: 
            parent_name,parent_birthday,child_name,child_birthday,child_deathday=None
        return:
            text if successful or not 
        """
        parent = self.FindPerson(parent_name,parent_birthday)
        if type(parent) != str:
            child = Person(child_name,child_birthday,parent,child_deathday)
            parent.AddChild(child)
            self.All[child_name] = {child_birthday : child }
            return (child_name+" Successfully added")
        return parent          
    
    def RemovePerson (self,person_name,person_birthday):
        """Gets a person by name and birthday and removes it from family tree (if it exists)   
        input: 
            person_name,person_birthday
        return:
            None 
        """
        print('Removing a person will remove all his children')
        a = input("you sure you want to remove?"+ "/n(Yes|No)")
        if not (a.lower() == 'yes' or a.lower() == 'y'):
            print('not removing so!')
            return
        p = self.FindPerson(person_name,person_birthday)
        print("person_name: ", p.name)
        if p is not None:
            child_list = []
            child_list.append(p)
            qeue = []
            qeue.append(p)
            while len(qeue) > 0:
                q = qeue.pop()
                for c in q.children:
                    child_list.append(c)
                    qeue.append(c)
            for c in child_list:
                name = c.name
                birthday = c.birth_day
                parent = c.parent
                parent.children.remove(c)
                del self.All[name][birthday] 
                if not len(self.All[name]):
                    del self.All[name] 
                print(self.All)              
                del c
        return        
    
    def GetAllPersons(self):
        res = []
        for k,v in self.All.items():
            opt = []
            for val in v.keys():
                opt.append(k + "_" + str(val))
            res.extend(opt)
        return res
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
            print(k.name)
            for c in k.children:
                qeue.append(c)
            size +=1
        print('size: ' +str(size))
        return size
     
    def CheckIsParent(self,parent_name,parent_birthday,child_name,child_birthday):
        """Gets tow persons by name and birthday then find if some on is chile of another one
            not only his child but also child of his child and so on!
        input: 
            parent_name,parent_birthday,child_name,child_birthday
        return:
            None 
        """
        parent = self.FindPerson(parent_name,parent_birthday)
        if parent is None:
            return False
        child = self.FindChild(child_name,child_birthday,root = parent)
        if child is None:    
            print(parent_name ,'is not father of ',child_name)
            return False
        else:
            print(parent_name ,' is father of ',child_name)
            return True
    
    def FindAllParents(self,person_name,person_birthday):
        """Gets a person by name and birthday then find all parents of that person
            input: 
                person_name, person_birthday
            return:
                parant_list 
        """
        c = self.FindPerson(person_name, person_birthday)
        parent_list = []
        if c is not None:
            m = c.parent
            while m != self.root:
                parent_list.append(m)
                m = m.parent
            parent_list.append(m)
        return parent_list
            
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
        parent1_list = self.FindAllParents(person1_name, person1_birthday)
        parent2_list = self.FindAllParents(person2_name, person2_birthday)
        i = -1
        while parent1_list[i] == parent2_list[i] and (abs(i)-1) < min(len(parent1_list), len(parent2_list)):
            i-=1
        return parent1_list[i]
    
    def FindFarestBorn(self,person_name, person_birthday):
        """Gets a person by name and birthday then find farest born of him
            input: 
                person_name, person_birthday
            return:
                farest born
        """
        p = self.FindPerson(person_name,person_birthday)
        farest_born = p
        if p is not None:
            qeue = []
            qeue.append(p)
            while len(qeue) > 0:
                k = qeue.pop()
                for c in k.children:
                    qeue.append(c)
                if k.level > farest_born.level:
                    fraset_born = k
        if farest_born == p:
            print("No child!")
        else:
            return farest_born
    
    def FindFarestRelations():
        pass
    
    def FindRelation(name1, name2):
        """Gets tow persons by name and find relationships between them
        input: 
            name1,name2
        return:
            relationship 
        """
        pass
    
