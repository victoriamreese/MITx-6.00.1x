# Object Oriented Programming
every instance of an object has a type, an internal data representation (primitive or composite) and a set of procedures for interaction with the object

### instances
a particular primitive

OOP - everything in python is an object and has a type
objects are a data abstraction that capture:
- internal representation through data attributes
- interface for interacting with object through methods / procedures 


- we can create new instances of objects and delete them
- every object type has an internal representation - we don't really need to worry about this.
- this internal representation should not be mettled with

### creating the class includes:
- defining the class name
- defining the class attributes
- for example, someone wrote code to implement a list class

### using the class involves:
- creating new instances of objects
- doing operations on the instances

## Advantages of Object Oriented Programming:
- bundle data into packages together with procedures that work on them through well-defined interfaces (abstraction!)
- divide-and-conquer development : implement and test behavior of each class separately.
- increases modularity reduces complexity
- classes make it easy to reuse code
- many Python modules define new classes - each class has a separate environment.
- no problems with naming collision because there are a lot of different scopes
- inheritance allows subclasses to redefine or extend a selected subset of a superclass' behavior .

### Class Instances
define our own type
e.g.
```
class Coordinate(object):
    <define attributes here>
```
- similar to def, indent code to indicate which statements are part of the class definition
- the word object means that the Coordinate is a Python object and inherits all its attributes
- coordinate is a subclass of object.
- object is a superclass of coordinate

## What are attributes?
- data and procedures that belong the the class
- data attributes
- think of data as other objects that make up the class
- for example, a coordinate is made up of two numbers

## procedural attributes (methods)
- think of methods as functions that only work with a particular class
- for example, you can define a distance between two coordinate objects but there is no meaning to a distance between two list objects.
- these methods are specific to the class in which they are defined. 

first have to define how to create in instance of object- use a special method called __init__

### the __init__ script explains to the program how to create instances of a class:
```
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

- special method to create an instance is __ double underscore
- self refers to an instance of the class
- in the above example, there are two data attributes, x and y, for every Coordinate object.

- use dot method to access an attribute of an instance
- classes are like data frames with particular attribute variables

### __str__ method
use the __str__ method to define an informative representation
use the isinstance() method to check if an object is a Coordinate
lots of other methods 

## Hierarchies
classes can inherit properties from each other. Parent classes have child classes and child classes can override the properties of the parent class

```
 e.g. Parent Class/Superclass
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str___(self):

         return "animal:"+str(self.name)+":"+str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal) 
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self, name, age)
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.freinds
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

```
### sub-sub class:
```
class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
```

- methods defined at lower levels of inheritance (e.g. child classes) take precedent over higher classes. - when a mehtod is not defined at a lower class, the program looks for a higher

OOP Extended example
You create a class using a constructor, then create instances through which you call the class and use its methods.

Simplest class:
```
class Snake:
    pass
```
- attributes act as containers for data and functions. 
- functions of a class are called methods.
- when you define methods, the first argument is the self keyword. 
- the self keyword refers to the newly created class. it is replaced with the instance name when
- referencing the class through an instance. 
- characteristics of instances of a class do not need to match the master class. for example, an attribute set as "True" within a class can be changed to false in an instance of that class.

e.g.
```
x.isTrue = False
x.isTrue
False 
```

```
import datetime

Person(object): #object is an class has standard methods / behaviors associated with them
    def __init__(self, name):  
# init method refers to the newly created object.
# this is where object attributes are initialized.
# the arguments of the __init__ method need only include parameters used in the definitions of the initialization attributes, not the names. so here, we only need name, we don't need birthday or lastName. These attributes can be altered in instances of the class.
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1] #split around spaces and extract the last name 
    
    def setBirthday(self, month, day, year): #method arguments - self is first, followed by arguments needed for method
        self.birthday = datetime.date(year,month,day) #returns representation of todays date

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other): 
        if self.lastName == other.lastName:
        return self.name < other.name
    return self.lastName < other.lastName
    
    def __str__(self):
        return self.name
```
- from this class we can create instances

- using inheritance - add another kind of person

```
class MITPerson(Person):
    nextIdNum = ()

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.number

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)
```
 
## when calling the subclass MITPerson, the program reads __init of this class first. 

- must only use methods appropriate for the objects passed to them. 

```
class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self) + m  "Dude," + utterance)

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj, Grad)
```

- substitution . important behaviors of superclass should be supported by all subclasses.
above, we can create a subclass called Student in which both US and Grad will reside. this makes sense - because the two classes share many attributes.

### Inherited Methods
leverage methods in the hierarchy, but keep modules isolated. 

```
class Progessor(MITPerson):
    def __ini__(self, name, departmnet):
        MITPerson.__ini__(self, name)
```

