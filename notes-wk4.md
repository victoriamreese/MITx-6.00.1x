# Testing and Debugging
## Keep in mind:
* 1. always design code that supports testing and debugging
* 2. always write document constraints (docstrings) that explain the expected input and output
* 3. always document the assumptions you make about code design. what was the thinking process, the assumptions?

- get rid of static semantic errors (caught by python) first

### Defensive Programming
plans ahead to avoid and detect bugs before we run the code
* write specifications for functions
* modularize programs
* check conditions on inputs/outputs
### Testing/Validation
compare input/output pairs to specification
- it's not working!
- how can I break my program?
### Debugging
study events leading up to an error
- why is it not working?
- How can I fix my program?
### Make your code easy to test and debug!
- docstrings, good labeling
- modularity
- document assumptions behind the code design

## Steps of testing:
- prep: ensure code runs
- write test cases: inputs and desired outputs
### Unit Testing
- validate each part of the program
### Regresson Testing
- design tests for reintroduced errors that were fixed previously
### Integration testing
- after debugging the modules, you must ensure the overall programs runs well
* this three processes are cyclical and often must be repeated *


# Approaches to testing:
### Blackbox testing
- designed without looking at the code 
- can be done by someone other than the implementer (avoids bias)
- testing can be reused if implementation changes
- paths through specification

e.g. selecting cases:
    - boundaries ( low and high)
    - perfect square
    - less than 1
    - irrational square root 

### Glass Box Testing
- looking at the code itself and using it to guide the design of test cases
- called path-complete if every potential path through the code is tested at least once
- need to look for boundary conditions as well as path-complete conditions

## Bug classification
### overt bugs
- obvious indication something is wrong
- use defensive programming to ensure that if error is made, bug will fall into this category

### covert bugs
- code returns a wrong value

### persistent
- happens everytime

### intermittent
- depend on other factors - only happen some of the time 


-----------------------------
# Debugging

- use the tools - IDEs, Python Tutor, Print statements
- use bisection method - print statement halfway through the code

### Error messages - Easy
- index error - value referenced is outside the existing index
- type error - operand doesn't have correct type
- name error
-valueError- operand type is okay but the value is illegal
- syntax error - forgetting a parenthesis, quotation, 
- attribute error- attribut reference fails
- IO error -

### Logic Errors - Hard
- think before you write new code

### Debugging steps:
- study the problem
- use the scientific method (make hypothesis, test cases)

*make "bug" version and "fixed" version for direct comparison.*

### Debugging strategies:
- use print statements

- --------
# Exceptions:
- called exception because it is an "exception" to what you expect to happen from python's perspective
- use try:, except: control flow to determine what happens in situations when code does not run properly


### Type of exceptions
- IndexError: trying to access beyond list limits
- SyntaxError: python can't parse program
- NameError: local or global name is not found
- Attribute Error: attribute reference fails
- TypeError: operand doesn't have correct type
- ValueError: operand type is okay, but the value is illegal
- IOError: IO system reports malfunction( e.g. file not found)
- ZeroDivisionError: attempted division by zero
- KeyboardInterrupt: raised when user hits the interrupt key
### What to do when encountering an error:
 - fail silently: 
    - just continue, user gets no warning
- return an "error" value
python code can provide custom handlers for exceptions
- stop execution and signal error condition


```
try: #special keyword, signals python to run following code
    a = int(input("Tell me onw number:"))
    b = int(input("tell me another number:" ))
   print(a/b)
    print('okay')
except: #special keyword preceding code that runs if the "try" block fails
    print("Bug in user input.")
```
- write particular exception print statements for different types of exceptions
- except ValueError:

### other important keywords:
- else: body of this is executed when execution of associated try body completes with no exeptions
- finally: body of code will execute after all other blocks of code that should execute do
    


example exception usage:
```
while True:
    try:
        n = input("Please enter and integer: ")
        n = int(n)
        break
    except ValueError:
         print("Input not an integer; try again")
print("Correct input of an integer!")
```
- loop will run forever unless it is broken out of.
- custom exception : if a value error is thrown, a more descriptive message will print to the console.

Another example:
```
data = []  
file_name = input("Provide a name of a file of data" )

try:
    fh = open(file_name, 'r')
except IOerror:
    print('cannot open', file_name)
else: 
   for new in fh: 
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)
finally:
    fh.close()

gradesData = []
if data
    for student in data:
        try:
            name = student[0:-1]
            gradesData.append([student[0:2], [student[2]])
        except ValueError:
            gradesData.append(student[:], []) 
```


## Control Flow as exceptions:
e.g. raising an exception: raise <Exception name>("text to be printed")
```
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal lenght of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try :
           ratios.append(L1[index]/float(L2[index]))
        except:

```
- you can make your exceptions raise errors and also handle them in custom ways, like returning a value (e.g. return 0.0) 
- The key is thinking ahead- defensive programming
- take precautions and predict what the codes should do if and when different errors are raised.

# Assertions
```
def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)
```
- second parameter of assert statement is what will happen if the assertion is false
- assertions allow a programmer to control response to unexpected conditions
- ensures that execution halts

### where to use assertion?
- testing as a supplement
- check types of arguments or values
- check that invariants on data structures are met
- check constraints on return values

### useful tidbits:
clone a list as a new variable name:
y = x[:] - shallow copy