class Parrot:
    species = 'bird'
    name = 'my parrot'
    age = 10

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for i in iterable:
            self.items_list.append(i)

    __update = update

class MappingSubClass(Mapping):

    def update(self, key, value):
        for item in zip(key, value):
            self.items_list.append(item)

class Employee:
    pass

    def name(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print('{} {}'.format(self.fname, self.lname))





if __name__ == '__main__':
##    par1 = Parrot('Blue', 20, 'mammal')
##    print(par1.name, par1.age)
##    print(par1.species)
##    print(par1.__class__.name)
##    print(par1.__class__.age)
##    print(par1.__class__.species)
##    print(Parrot.species)
##    print(Parrot.__init__)
    
##def main():
##    par1 = Parrot('Blu', 10)
##    print(par1.name, par1.age)
##    
##main()
##    mappingobject = MappingSubClass({'mk', 45})
##    print(mappingobject.items_list)
##    print(isinstance(mappingobject, Mapping))
##    print(isinstance(mappingobject, MappingSubClass))
##    print(issubclass(MappingSubClass, Mapping))
##    print(Mapping.__dict__['update'])
    emp = Employee()
    print(emp.name('k', 'm'))
    
