import random
class name_generator():
    def __init__(self):
        with open ('names/female.txt','r') as f:
            l = f.readlines()
        names = []
        for i in l:
            names.append(i.split(' ')[0])
        with open ('names/male.txt','r') as f:
            l = f.readlines()
        for i in l:
            names.append(i.split(' ')[0])
        self.names = names
    def generate(self):
        return random.choice(self.names)