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


#mutation, aliasing, cloning-
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


###Dictionaries
-key:value pairs
-order isn't important
- in fact, there is no particular order to dictionaries
storing new data:
e.g.
 ```
a_dictionary['key'] = 'value'
```
- you can return all the keys and values that belong to a particular dictionary like so:
```
grades.keys() #returns all keys of dictionary grades
grades.values() #returns all values of dictionary grades
```

####Values
-any type
-can be duplicates
- dictionary values can be lists, even other dictionaries

####Keys
-must be unique
-immutable type(int, float, string, tuple, bool)
-need an abject that is hashable, but think of it as immutable as all immutable types are hashable
- careful with float type!
- they need to be immutable because 


###dictionary example
1. create a frequency dictionary mapping str:int
2. find word that occurs the most and how many times
3. find the words that occur at least X times

``` 
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics: 
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
         if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
            else:
                done = True
       return result

print(words_often(beatles, 5))
 ```

###Fibonacci Recursion
```
fib(n) = fib(n-1) + fib(n-2)
```
vs. fibonacci with a dictionary
``` 
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

```
takes a lot longer to calculate it recursively.

#### Global Variables
beware- global variables can break the scoping of variables by function call
allows for side effects of changing values in ways that affect other computation

tracking efficiency with global variables:
allows us to track the number of calls
```
global numFibCalls
numFibCalls += 1
if n ==1:
    return 1
elif n == 2:
   return 2
else return fib(n-1) + fib(n-2)

```
initialize numFibCalls = 0
when running the program, print numFibCalls to see how many times the program ran (measure of efficiency)


