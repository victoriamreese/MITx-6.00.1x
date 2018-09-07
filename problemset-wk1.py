# counts the number of vowels in a given string "s"

vowel = ['a', 'e', 'i', 'o', 'u']

count = 0
for letter in s:
print(letter)
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
count += 1
print("Number of vowels: " + str(count))

# counts the number of times "bob" occurs in a given string "s"

bobcount = 0
n = 0
for i in range(0, len(s)):
three = s[n:n+3]
n += 1
if three == "bob":
bobcount += 1 

print("Number of times bob occurs is: " + str(bobcount))

# prints the longest substring in alphabetical order from string "s"

substring = ''
longest = '' 
for i in range(0, len(s)-1):
if not substring:
substring = s[i]
if s[i] < s[i+1] or s[i] == s[i+1]:
substring += str(s[i+1])
else:
if len(longest) < len(substring):
longest = substring
substring = ''
if i == len(s)-2 and len(substring) > len(longest):
longest = substring
break
print("Longest substring in alphabetical order is: " + str(longest))