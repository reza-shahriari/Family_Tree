from Person import Person
from collections import deque
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
        qeue = deque()
        root = self.root if root is None else root
        qeue.append(root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                if c.name == person_name and c.birth_day == person_birthday:
                    return c
                qeue.append(c)
        return 'person with name: ' + person_name + 'and birthday: ' + str(person_birthday) + ' not found in '+ root.name+'\'s child'
    
    def AddPerson (self,parent_name,parent_birthday,child_name,child_birthday,child_deathday=None):
        """Gets tow persons by name and birthday then add child   
        input: 
            parent_name,parent_birthday,child_name,child_birthday,child_deathday=None
        return:
            text if successful or not 
        """
        parent = self.FindPerson(parent_name,parent_birthday)
        if type(parent) != str:
            child = Person(child_name,int(child_birthday),parent,child_deathday)
            parent.AddChild(child)
            if not self.All.get(child_name):
                self.All[child_name] = {int(child_birthday) : child }
            else:
                self.All[child_name][int(child_birthday)]=  child 
            return (child_name+" Successfully added")
        return parent          
    
    def RemovePerson (self,person_name,person_birthday):
        """Gets a person by name and birthday and removes it from family tree (if it exists)   
        input: 
            person_name,person_birthday
        return:
            None 
        """
        person = self.FindPerson(person_name,person_birthday)
        print(type(person))
        if type(person) != str :
            child_list = []
            child_list.append(person)
            qeue = deque()
            qeue.append(person)
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
                del c
            return (person_name+' Successfully Removed')
        return person        
    
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
        res =0
        for _,v in self.All.items():
            res += len(v.values())
        return 'Size of family tree is ' + str(res)
     
    def CheckIsParent(self,parent_name,parent_birthday,child_name,child_birthday):
        """Gets tow persons by name and birthday then find if some on is chile of another one
            not only his child but also child of his child and so on!
        input: 
            parent_name,parent_birthday,child_name,child_birthday
        return:
            None 
        """
        
        #Check if child is parent :|
        if child_name == parent_name and child_birthday == parent_birthday:
            return "How can a person be his own parent? :|"
        
        #Check if child is the root
        if child_name == self.root.name and child_birthday == self.root.birth_day:
            return parent_name +' is not father of ' + child_name
        
        parent = self.FindPerson(parent_name,parent_birthday)
        if type(parent) ==str:
            return parent
        child = self.FindPerson(child_name,child_birthday,root = parent)
        if type(child) == str:    
            return parent_name +' is not father of ' + child_name
        else:
            return parent_name + ' is father of '+ child_name

    def FindAllParents(self,person):
        """Gets a person by name and birthday then find all parents of that person
            input: 
                person_name, person_birthday
            return:
                parant_list 
        """
        parent_list = []
        m = person.parent
        parent_list.append(person)
        while m is not None and m != self.root :
            parent_list.append(m)
            m = m.parent
        if m is not None:    
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
        if type(person1) ==str:
            return person1
        if type(person2) ==str:
            return person2
        parent1_list = self.FindAllParents(person1)
        parent2_list = self.FindAllParents(person2)
        # print('Parent list 1')
        # for i in parent1_list:
        #     print(i.name)
        # print('parent list 2')
        # for i in parent2_list:
        #     print(i.name)
        i = -1
        lca_name = ''
        m = min(len(parent1_list), len(parent2_list))

        while (abs(i)) <= m  and parent1_list[i] == parent2_list[i] :
            lca_name = parent1_list[i].name
            i-=1
        if lca_name != '':
            return 'Lowest common ancestor of'+ person1_name+' and '+person2_name+' is ' + lca_name
        else:
            return "No common ancestor found!"
    
    def FindFarestBorn(self,person_name, person_birthday):
        """Gets a person by name and birthday then find farest born of him
            input: 
                person_name, person_birthday
            return:
                farest born
        """
        p = self.FindPerson(person_name,person_birthday)
        farest_born = p
        if type(p) != str:
            qeue = []
            qeue.append(p)
            while len(qeue) > 0:
                k = qeue.pop()
                for c in k.children:
                    qeue.append(c)
                if k.level > farest_born.level:
                    farest_born = k
            if farest_born == p:
                return ("No child!")
            else:
                return p.name +'\'s farest born is '+farest_born.name
        else:
            return p
    
    def FindFarestRelations(self):
        """Find farest relations in Family tree
        input:
            Nothing
        return:
            longest path in the Family tree and its length
        """
        def Find_distance(u):
            all_persons = []
            for k,v in self.All.items():
                for val in v.values():
                    all_persons.append(val)
                    
            visited = {}
            distance = {}
            for i in all_persons:
                visited[i] = False
                distance[i] = -1
                
            distance[u] = 0
            queue = deque()
            queue.append(u)
            visited[u] = True
            while len(queue) > 0:
                person = queue.popleft()
                if person.parent is not None:
                    if not visited[person.parent]:
                        visited[person.parent] = True
                        distance[person.parent] = distance[person]+1
                        queue.append(person.parent)
                        
                for i in person.children:
                    if not visited[i]:
                        visited[i] = True
                        distance[i] = distance[person]+1
                        queue.append(i)

            max_dis = 0
            for i in all_persons:
                if distance[i] > max_dis:
                    max_dis = distance[i]
                    far_person = i
            return far_person, max_dis
        
        p1,d = Find_distance(self.root)
        p2,d = Find_distance(p1)
        return 'Farest realation is between '+p1.name + ' and ' + p2.name + ' and its: ' + str(d -1) + ' persons between them' 
    
    def FindRelation(name1, name2):
        """Gets tow persons by name and find relationships between them
        input: 
            name1,name2
        return:
            relationship 
        """
        pass
    
