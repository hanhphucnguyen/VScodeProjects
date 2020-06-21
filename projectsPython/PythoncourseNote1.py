#Power
z = 3**3
#square root
z = 3**0.5

#check string length
i = len('hello')

#string slicing
s= 'hello'
a = s[1:]   #ello  # Grab everything from 1 index
b = s[:3]   #hel   # Grab everything UP TO the 3rd index
c = s[:]           # Everything
d = s[-1]   #o     # Last letter (one index behind 0 so it loops back around)
e = s[:-1]  #hell  # Grab everything but the last letter
f = s[::2]  #hlo   # Grab everything, but go in step sizes of 2
g = s[::-1]        # Reverse string
letter = 'z'
h = letter*10

#built-in string method
s = 'Hello World'
r = s.upper()
r = s.lower()
u = s.split()    # ["Hello","World"] Split a string by blank space (default)
r = s.split('W') # ["Hello ","orld"]
s.count('llo')   # find substring and count

# ---------------------------------------------------------------------------
#List
my_list = ['A string',23,100.232,'o']
a = my_list[1:]              # Grab index 1 and everything past it
b = my_list[:3]              # Grab everything UP TO index 3
c = my_list + ['new item']
d = my_list*2
my_list.append('append me!') # Append
my_list.pop(0)               # Pop off the 0 indexed, default will takes off last index (-1)
popped_item = my_list.pop()  # Get the popped element
newList = [1,2,3,4,5]
newList.reverse()            # Reverse order (this is permanent!)
newList.sort()               # Sort
# Use .count to count the number of times a value appears
u = newList.count(1)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix] #[1,4,7]

#---------------------------------------------------------------------------
#Dictionary
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
#Can call methods on that value
i = my_dict['key3'][0].upper()

d = {}
d['animal'] = 'Dog'
d['answer'] = 42

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}
# Keep calling the keys
d['key1']['nestkey']['subnestkey']
# Methods
a = d.keys()
b = d.values()
c = d.items()

#------------------------------------------------------------------------
#Tuples
t = (1,2)
# Use .index to enter a value and return the index
u = t.index(1)
# Use .count to count the number of times a value appears
u = t.count(1)
#Because of immutability, tuples can't grow. Once a tuple is made we can not add to it.

#------------------------------------------------------------------------
#Sets
x = set()
# We add to sets with the add() method
x.add(1)
# Create a list with repeats
l = [1,1,2,2,3,4,5,6,1,1]
# Cast as set to get unique values
s = set(l)
