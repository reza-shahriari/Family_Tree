class person():
    def __init__(self,name,mother,father,children):
        self.name = name
        self.hashed_name = self.hash(name)
        self.mother = mother
        self.father = father
        self.children = []
        for i in children.strip().split(","):
            if len(i):
                self.children.append(i)

    def hash(self):
        return ' '