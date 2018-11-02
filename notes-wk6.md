# Algorithmic Complexity :
* some programs are more efficient than others- growing data sets 
* lots of potential implementations (recursion, iteration, etc.)
* but only a couple possible algorithms

## How do we evaluate algorithmic efficiency?
* option 1: evaluate a program' runtime
    * problem: inconsistent from computer to computer
* option 2: Count the operations
    * assume all steps take constant time
        * mathematical operations
        * comparisons
        * assignments
        * accessing objects in memory
            * Pros: depends on algorithm and independent of the computer
        * BUT
            * Cons: dependent on implementation
* Must be able to evaluate in terms of input size - How do we decide which input to look at?
    * could be an integer, length of a list, or multiple paramenters- you need to chose between
* Best case - minimum run-time over all possible inputs of a given size, len(L)
* worst case- maximum run-time 

## Orders of Growth:
* goal: evaluate a program's efficiency when input is very big
* express growth of program's runtime as program grows
* identify largest factors in runtime - which parts of the program will take the longest?

*Big oh- measures upper bound on the asymptotic growth* 


### Example categories:
* O(n^c) - polynomial
* O(n) -  linear - e.g. searching list in sequence to see if element is present. add characters of a string
* O(n*log(n)) - 
* O(log(n)) - reduce size by input by constant value each iteration
* O(c^n) - exponential


# Searching and Sorting Algorithms:
* methods for finding an item or group of items with specific properties within a collection of items

## Linear Search- brute force
bisection - requires sorting, divide the list into useful and less useful parts
```
def search(L, e): 
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
```

## Bogo Sort/ Stupid Sort:
* random assigment fo list elements, check if they are in order
* if not, random suffles
```
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
```
best case: O(n) where n is len(L)
worst case: unbounded

## Bubble sort:
* compare consecutive pairs of elements
* swap elements in pair souch that smaller if first
* when reaching end of the list, start over again
* stop when no more swaps have been made
* complexity is O(n^2) - quadratic

```
def bubble_sort(L):
    swap = False
    while not swap
        swap = True
        for j in range (1, len(L)):
            if L[j-1] > L[j]
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
```
## Selection Sort:
*  one element is compared with all others
* element is kept until it is compared with an element that is smaller. if it is compared with a smaller element, this smaller element now takes its place
```
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
    for i in range(suffixSt, len(L)):
        if L[i] < L[suffixSt]:
            L[suffixSt], L[i] = L[i], L[suffixSt]
    suffixSt += 1
```

## Merge Sort:
* splits list into smaller lists of 2 elements, then merges this list into larger list and orders these two lists.
```
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
       middle = len(L)//2
        left = merge_sort(L[:middle])
```
