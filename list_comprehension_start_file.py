'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.

old_list = [1,2,3,4,5]
new_list = []

for i in old_list:
    if i >3:
        j=i*i
        new_list.append(j)
print(new_list)


# [expression iteration condition]
new_list = [i*i for i in old_list if i>3]
print(new_list)

#1) creating a simple list of 10 numbers using  Range()

x = [i for i in range(10)]
print(x)

#2) creating  a list that evaluates an expression

squares = [x**2 for x in range(10)]
print(squares)


#3) creating a list from another list

list1 = [3,4,5]
multiplied = [item *3 for item in list1]
print(multiplied)

#4) using list comprehension for string manipulation

# printout word with first letter is being upper case

listOfWords = ["The", "Force", "will","be","with","you","Always"]

word_type =[ item[0] for item in listOfWords if item[0] == item[0].upper()]

print(word_type)

#5) Let's show how easy you can convert lower case ? upper case letters.

output = [x.lower() for x in ["A", "B","C"]]
print(output)

#6) Creating a list based on a condition

# create a list of squre of all even numbers between 1 and 10 

output = [x*x for x in range(1,11) if x % 2 == 0]
print(output)

#7) Extracting numbers only from a string and putting it in a list

string = "Hello 12345 World"
numbers = [ int(x)for x in string if x.isdigit() ]
print(numbers)

letters = [ x for x in string if x.isalpha()]
print(letters)

words = [x for x in string.split(" ") if x.isalpha()]
print(words)

#8) 
'''
In this example, we can see how to get 
specific lines out from a text file

'''

infile = open( 'test.txt','r')

result = [ i.rstrip("\n") for i in infile if "line3" in i]

print(result)

#9) Using function in list comprehension

def double(x):
    return x*2

result = [ double(x) for x in range(10)]
print(result)

#10) adding an IF condition to the above

result = [ double(x) for x in range(10) if x % 2 ==1]
print(result)

#11) you can add more argument (using multiple iterations and lists):

output = [x+y for x in [10,50] for y in [20,40] if x+y > 70]
print(output)

## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = [int(x) for x in numbers if x > 0]
print(newlist)


## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

newlist = [int(len(x)) for x in words if x != 'the']
print(newlist)

## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

newlist = [x.upper() for x,y in dict.items()  if y < 5000]
print(newlist)


## Find all the numbers from 1 to 1000 that have a 4 in them

newlist = [x for x in range(1,1001) if '4' in str(x)]
print(newlist)

## count how many times the word 'the' appears in the text file - 'sometext.txt'

infile = open('sometext.txt', 'r')

outfile = infile.read()

words = outfile.split()

newlist = len([x for x in words  if x == 'the'])
print(newlist)


## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'

numbers = [ int(x)for x in phrase if x.isdigit() ]
print(numbers)





