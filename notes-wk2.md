#Tuples Lists and Mutability

##tuples- 
an ordered sequence of elements, can mix elements 
format: (1, 2, 3, 4, 5)
can be indexed 
can be concatenated 
immutable

convenient for swapping variables
e.g. (x, y) = (y, x)
output includes comma - this denotes that it is a single value in a tuple
 thinking about a tuple 

##lists- 
*mutable
*can be indexed
*can be concatenated 
 ####note: three ways to iterate
*for n in range(list):
we iterate through indices
*for i in list: 
we iterate through values 
*for n, i in enumerate(list):  
 
 this one allows us to create a counter and also to iterate through the values in the list.
#list operations -
*.append
*.split(element) divides a list into two strings at the element specified
*.pop() removes the last list element
*.join --> unites list elements into a string.
*del(L[index]) 
*.remove(element) ---> removes only first instance of element
*.list()---> converts string to a list
*sorted(L)--> returns a sorted list 
*L.sort() -->replaces list L with a sorted version of itself. 
#mutation, aliasing, cloning
mutability can be problematic - bad side effects
####aliases: 
warm = list
hot = warm
*hot is an alias of hot
*when you change one, you change the other

####cloning:
cool = list
chill = [:]
*creates a copy of the list cool
*they are separate and changing one does not change the other

creating lists of lists from a starting list
chilled = [cool]

*be careful of mutating a list while you loop through it. better practice is to clone the list through which you want to iterate, and to loop through the clone first.*

 #Functions as Objects
*functions are "first class objects"
*elements of data structures can appear in expressions
*particularly useful when using functions as arguments

*you can use a function as the parameter of a function!

e.g.
```def applyToEach(L, f)
for i in range (len(L):
    L[i] = f(L[i])```


###Map
*map allows us to apply something to a list
*map(method, [list])
e.g.
```for elt in ,ap(abs, [1, -2, 3, -4])
    for elt in map(min, L1, L2): 
    print(elt)``` 
  