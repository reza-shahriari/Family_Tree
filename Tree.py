from Person import Person
from collections import deque
class FamilyTree():
    def __init__ (self, grandfather_name,grandfather_birthday,grandfather_deathday=None):
        self.root = Person(grandfather_name,grandfather_birthday,None,grandfather_deathday)
        self.size = 1
        
    
    def FindPerson (self, person_name, person_birthday,root = None):
        """Gets a person by name and birthday and tell us if it exists   
        input: 
            person_name,person_birthday
        return:
            person or str msg if no person 
        """
        hashed = Person.Hash(person_name, person_birthday)
        if self.root.hashed_name == hashed:
            return self.root
        if root is None:
            if Person.all_persons.get(hashed,False):
                return Person.all_persons[hashed]
            return 'person with name: ' + person_name + 'and birthday: ' + str(person_birthday) + ' not found in The tree'
        qeue = deque()
        root = self.root if root is None else root
        qeue.append(root)
        while len(qeue) > 0:
            k = qeue.pop()
            for c in k.children:
                if c.hashed_name == hashed:
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
            self.size += 1
            return (child_name+" Successfully added")
        return parent          
    
    def RemovePerson (self,person_name,person_birthday):
        """Gets a person by name and birthday and removes it from family tree (if it exists)   
        input: 
            person_name,person_birthday
        return:
            str msg (success or not found) 
        """
        person = self.FindPerson(person_name,person_birthday)
        if person == self.root:
            for c in Person.all_persons.values():
                del c
            self.size = 0 
            while len(list(Person.all_persons.keys())):
                del Person.all_persons[list(Person.all_persons.keys())[-1]]
            return (person_name+' Successfully Removed')
        elif type(person) != str :
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
                parent = c.parent
                parent.children.remove(c)
                self.size -= 1             
                del Person.all_persons[c.hashed_name]
                del c
            return (person_name+' Successfully Removed')
        return person        
    
    def GetAllPersons(self):
        
        all_persons = list(Person.all_persons.values())
        res = []
        for prs in all_persons:
            opt = prs.name + '_' + str(prs.birth_day)
            res.append(opt)
        return res
    
    def GetSize(self):
        """returning size of family tree   
        input: 
            None
        return:
            size 
        """
        return 'Size of family tree is ' + str(self.size),self.size
     
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
            return parent_name +' is not parent of ' + child_name
        
        parent = self.FindPerson(parent_name,parent_birthday)
        if type(parent) ==str:
            return parent
        child = self.FindPerson(child_name,child_birthday,root = parent)
        if type(child) == str:    
            return parent_name +' is not parent of ' + child_name
        else:
            return parent_name + ' is parent of '+ child_name

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
        i = -1
        lca_name = ''
        m = min(len(parent1_list), len(parent2_list))

        while (abs(i)) <= m  and parent1_list[i] == parent2_list[i] :
            lca_name = parent1_list[i].name
            i-=1
        if lca_name != '':
            return 'Lowest common ancestor of '+ person1_name+' and '+person2_name+' is ' + lca_name
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
            longest path in the Family tree and its length :str
        """
        def Find_distance(u):
            all_persons = list(Person.all_persons.values())
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
        s1 = self.FindRelation(p1.name,p1.birth_day,p2.name,p2.birth_day)
        
        return '\tFarest realation is between '+p1.name + ' and ' + p2.name + ' and its: ' + str(d -1) + ' persons between them\n'+s1[0],s1[1] 
    
    def FindRelation(self,person1_name, person1_birthday ,person2_name, person2_birthday):
        """Gets tow persons by name and birthday then find realation between them
        input: 
            person1_name, person1_birthday ,person2_name, person2_birthday
        return:
            realation: str 
        """  
        global res,path
        path = []
        res = ''    
        person1 = self.FindPerson(person1_name, person1_birthday)
        person2 = self.FindPerson(person2_name, person2_birthday)
        if type(person1) ==str:
            return person1
        if type(person2) ==str:
            return person2

        all_persons = list(Person.all_persons.values()) 
        visited = {}
        for i in all_persons:
            visited[i] = False
        def printPath(stack,):
            global res,path
            for i in stack:
                path.append(i)
            res = ''
            for i in range(len(stack) - 1):
                res += stack[i].name +  " -> "
            res += stack[-1].name
        def Find_path(vis, x, y,stack,name_stack):
            stack.append(x)
            if (x == y):
                printPath(name_stack)
                return 
            vis[x] = True
            j = x.parent
            if j is not None and vis[j] == False:
                name_stack.append(j)
                Find_path(vis, j, y, stack,name_stack)
            for j in x.children:
                if (vis[j] == False):
                    name_stack.append(j)                    
                    Find_path(vis, j,y,stack,name_stack)
            if stack: del stack[-1]
            if name_stack: del name_stack[-1]
        
        Find_path(visited,person1,person2,[],[person1])
        
        return res, path
    
    def VisualizeTree(self):
        """create cordinates for persons to visualize them
        input:
            Nothing
        return:
            cordinates, size of image
        """
        global max_in_lvl_dict
        
        all_persons = list(Person.all_persons.values())
        print("all_persons: ", all_persons)
        tree_heigth = 0
        max_in_lvl_dict = {}
        image_for_person = {}
        HEIGHT_PER_PERSON = 100
        WIDTH_PER_PERSON = 100
        #its to slow algorithm but it works!
        def number_of_children(person,):
            global max_in_lvl_dict
            max_in_lvl_dict[person] = 1
            for c in person.children:
                number_of_children(c)
                max_in_lvl_dict[person]+= max_in_lvl_dict[c]
        number_of_children(self.root)
        for i in all_persons:
            tree_heigth = max(tree_heigth,i.level)
        im_height = HEIGHT_PER_PERSON * tree_heigth
        im_width = WIDTH_PER_PERSON * max_in_lvl_dict[self.root]
        image_for_person[self.root] = [0,im_width, im_height]
        cordinate_for_person = {}
        qeue = deque()
        qeue.append(self.root)
        while len(qeue) > 0:
            p = qeue.pop()
            t_now = image_for_person[p][0]
            for c in p.children:
                print(type(c))
                w = int(image_for_person[p][1] * max_in_lvl_dict[c]/max_in_lvl_dict[p])
                image_for_person[c] = [t_now,w+t_now,int(image_for_person[p][2]) - WIDTH_PER_PERSON]
                t_now += int(image_for_person[p][1] * (max_in_lvl_dict[c])/max_in_lvl_dict[p]) 
                qeue.append(c)
        max_h = 0
        max_w = 0
        for i in all_persons:
            h = int(im_height - image_for_person[i][2]+50)
            max_h = max(max_h,h)
            w = int((image_for_person[i][0]+image_for_person[i][1])/2)
            max_w = max(max_w,w)
            cordinate_for_person[i] = (w,h)
        max_w += WIDTH_PER_PERSON
        im_width = max_w
        max_h += HEIGHT_PER_PERSON
        im_height = max_h
        cordinate_for_person[self.root] = (int(im_width/2),50)

        return im_height  , im_width ,cordinate_for_person   
        
            
        