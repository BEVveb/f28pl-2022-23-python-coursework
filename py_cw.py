# Bogdan Egorov                 <--- so we know who you are
# H00418676               <--- so we know who you are
# Dubai               <--- Edinburgh, Dubai, or Malaysia 
# F28PL Coursework 1, Python         <--- leave this line unchanged 

# Deadline is Wednesday 26 October 2022 at 15:30, local time for your campus (Edinburgh / Dubai / Malaysia).

# It is not your marker's role to debug basic syntax errors.
# Therefore, if your script won't compile then it might not be marked.
# In other words: if `python3 py_cw.py` won't execute, then your marker is not obliged to mark your answers. 

# To do this coursework, FORK, THEN CLONE the gitlab project.

# If you do it the other way around, then you'll have cloned *my* project (which you can't `git push` to), rather than cloned *your fork* of the project (which you can `git push` to).  
# Any questions, don't guess: ask.

# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.

# The test file test_cw.py is not exhaustive. 
# Just because your answer passes it does not mean it's correct.
# You would do well to consider where errors might be lurking and to add these to test_cw.py.   
# You are not marked directly on the quality of additional tests, however your marker may be
# able to assign marks for understanding as demonstrated in any tests you may write, 
# even if the code itself isn't quite right. 

# This coursework is live exam material so KEEP YOUR ANSWERS PRIVATE.  

# Before submitting this coursework please complete the Student authorship declaration here:
#   https://canvas.hw.ac.uk/courses/20804/assignments/102574 
 

# Do not delete the text from here ... 
################################################################################
# Question 1   


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
* tocomplex and 
* fromcomplex 
that map the pair (x1,y1) to the complex number x1+(y1)j and vice versa. 
You may use the python methods real and imag without comment, but not complex -- use j directly instead.
"""
# ... to here

# Check: have you read the question?  Have you read the link above to see how complex number addition and multiplication work?   


# Your answer here (Yes I did)

#####################################
# Question 1a


def cadd(c1, c2):
    x = c1[0] + c2[0] # adds first elements of both complex numbers
    y = c1[1] + c2[1] # adds second elements of both complex numbers
    return (x, y) # returns sum of first and second elements in brackets

def cmult(c1,c2):
    x = (c1[0] * c2[0]) - (c1[1] * c2[1]) # performs multiplication of complex numbers based on formula from:
    y = (c1[0] * c2[1]) + (c1[1] * c2[0]) # http://www.mathsisfun.com/algebra/complex-number-multiply.html
    return (x, y) # returns sum of first and second elements in brackets

#####################################
# Question 1b


def tocomplex(x1, y1):
    return x1 + (y1 * 1j) # returns real number + real number multiplied by complex, to make one complex

def fromcomplex(c):
    return (c.real, c.imag) # c.real returns int of real number; c.imag returns int of imaginary number


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions 
* seqandi and 
* seqxori 
that implement pointwise AND (https://en.wikipedia.org/wiki/Logical_conjunction) and XOR (https://en.wikipedia.org/wiki/Exclusive_or) of boolean sequences.
For instance
 seqandi([True,True,False],[True,False,True])
should compute
 [True, False, False]
and
 seqxori([True,True,False],[True,False,True])
should compute
 [False, True, True]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqandr and seqxorr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
Call them seqandlc and seqxorlc.
"""

#####################################
# Question 2a


def seqandi(l1, l2):
    temp = [] # temp list to store results of logic gates
    for i in range(0, len(l1)):
        if l1[i] == True and l2[i] == True: # if both values of the list are true
            temp.append(True) # append 'True' to the temp list
        else:
            temp.append(False) # else append 'False' to the temp list
    return temp # return temp list


def seqxori(l1, l2):
    temp = [] # temp list to store result of logic gates
    for i in range(0, len(l1)):
        if l1[i] != l2[i]: # if elements from both lists don't equal to each other
            temp.append(True) # append 'True' to the temp list
        else:
            temp.append(False) # else append 'False' to the temp list
    return temp # return temp list


#####################################
# Question 2b


def seqandr(l1, l2):
    if not (l1 and l2): # if both lists are empty
        return [] # returns empty list
    else:
        x = l1.pop(0) # pops the current first element of l1
        y = l2.pop(0) # pops the current first element of l2
        return [x and y] + seqandr(l1,l2) # returns result for AND gate, within a list, and recurses to repeat the process
    

def seqxorr(l1, l2):
    if not (l1 and l2): # if both lists are empty
        return [] # return empty list
    else:
        x = l1.pop(0) # pops the current first element of l1
        y = l2.pop(0) # pops the current first element of l2
        return [x != y] + seqxorr(l1,l2) # returns result for XOR gate, within a list, and recurses to repeat the process


#####################################
# Question 2c


def seqandlc(l1,l2):
    temp = [x == True and y == True for x,y in zip(l1,l2)] # when x (for l1) and y (for l2) are 'True', 'True' is stored within temp list, else 'False' is stored. List is zipped to have elements from both list in same position [[True, True], ...]
    return temp

def seqxorlc(l1,l2):
    temp = [x != y for x,y in zip(l1,l2)] # when x (for l1) and y (for l2) are don't equal to each other, 'True' is stored within temp list, else 'False' is stored. List is zipped to have elements from both list in same position [[True, True], ...]
    return temp




# END ANSWER TO Question 2
################################################################################


###############################################################################
# Question 3


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
a. Mutable vs immutable types. Give at least two examples of each, with explanation.
b. Integer vs float types.
c. Assignment = vs equality == vs identity is.
d. The computational effects of a call to list on an element of range type, as in
 list(range(5**5**5)).
e. Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""
"""
ANSWER:

Python data representatives are the key to building any type of modules within the language itself. First one that we
may focus on are the mutable and immutable types. Mutables are the dynamic data structures in which variables may change 
or new variables may be added. Examples of such may be lists and dictionaries. Immutable data types are static variables 
which cannot be changed after a value was assigned to them, examples being 'int', 'bool' and ext.

When discussing numerical data representtatives, often the most usable way to assign or calculate such values would be 
with usage of 'int' or 'float'. Even though both perform the same task, both show it in a different way. First major difference
is that 'int' only represents the whole value of a numerical data, whereas 'float', in addition to whole values, may represent
the decimal points of such value inclusively. However, when working with large numbers, 'int' performs better and shows all
of the final values according to the right answer, whereas 'float' will struggle with such matter, often either giving an error
or a shortened final value. The reason for the innacuracy of 'float' is due to it being hard for the computer to perform 
large decimal point calculations using base 2, thus it seeks shortcuts or overall decides to deny the task.

When it comes to the assignment or checking of variables in python, there are 3 different possibilites for such task, with
their own differences. If we decide to use '=' in Python, such notation would represent the assignment of a value to a variable
(ex. x = 5, which means that now the value of x is 5). If we go for the '==' notation in Python, such would represent equality,
which checks if one variable/value is equal to another (ex. True == True, which checks if both sides of the equality are similar,
where in this case it is, so returns "True"). If we decide not to use equals sign, but instead write 'is' or 'is not', it will
be used to identify 2 variables/values, which checks if both given data point to the same object (x is x should return 'True')

Major in data representation is the computational effects that come with the execution. When, for example, executing a line of code,
such as "list(range(5**5**5))", Python will calculate the range of such value, but when it would come to list, it would give
an error stating that "int too large to convert", meaning that the compiler decided that it would take too much time and effort
to convert such a number.

Lastly, slices may be used in data representatives to show where to start and end the execution, and what to output to the user.
For example, "list(range(10**10)[10:10])" code has '[10:10]' within the brackets of list, indicating that after calculating the range,
values from 10 to 10 should be shown, where 10 is the stopping value. Since both of the values are the same, no value would be shown, 
but nevetheless, such action is still slicing. If the same square brackets where to be put outside of the brackets, no slicing would be done.

"""


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4

"""
Recall that `map(f, l)` applies a function pointwise to a list, so that 
   map(f, [x, y, z]) 
computes 
   [f(x), f(y), f(z)]
Call a *datum* something that is either an integer, or a list of data (datums).
Write a generalised mapping function `supermap` that applyies `f` pointwise to any integers inside a datum. 

So for example:
* supermap(f, -5) should return 'f(-5)'
* supermap(f, []) should return '[]'
* supermap(f, [5, [5]) should return '[f(5), [f(5)]]'. 

You may find it useful to consider `isinstance` or the following code fragment
   type(5) == int 

An answer that guts the question (e.g. by calling a supermap-like function in a Python library) may score no marks.
"""


def supermap(f, dat):
    if isinstance(dat, list): # if the data type is a list
        return [supermap(f, x) for x in dat] # return the supermap function done on the x element within the dat list
    else:
        return f(dat) # return the function done on the data of not type list
            
# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5


"""
An encoding f of numbers in lists is as follows:
* f(0) = [] (0 maps to the empty list)
* f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.

This is an implementation of one possible encoding of the natural numbers in sets:
   https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers
"""


def fenc(i):
    if i == 0: # if the given number is 0
        return [] # return an empty list/1 square bracket
    else:
        return [fenc(i - 1), [fenc(i-1)]] # return recursion of the function done within the list, and the same function done within a nested list


def fdec(l):
    total = 0
    for i in range (len(l)):
        if type(l) == list:
            for x in l:
                if type(x) == list:
                    total += 1
    return total


# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
Implement a generator `love` such that if we assign
 x = love()
then repeated calls to
 next(x)
return the strings 
 I love you 
 You love that I love you
 I love that you love that I love you
 You love that I love that you love that I love you
 I love that you love that I love that you love that I love you
 ...
For full marks, your answer should respect correct capitalisation, as above.

Note that this question is not asking you to program an endless loop that prints these values; your answer should be a generator that yields these values.
"""


def love():
    ILU = "I love you" 
    ILT = "I love that "
    YLT = "You love that "
    l_YLT = "you love that "
    # Predetermined texts for generation
    x = ILU # Assign first output as "I love you"
    yield x # yield the first text

    while True: # a continuous loop to generate text
        y = YLT + x # "You love that" is added each time to current 'x' text
        yield y
        x = ILT + l_YLT + x # x here adds "I love that" and adds "you love that" with changed capitilisation (to meet the requirements) to pre-existing x text
        yield x

# END ANSWER TO Question 6
################################################################################


#################################################################################
# Question 7

"""
Consider functions that remove all instances of an integer `i` from a list of integers `l`, implemented in three distinct ways:

1. `removeall_oo` repeatedly applies the list .remove method until there are no instances of `i` left (you may use other programming constructs, such as counting the number of integers in `l`, or using exception raisers and handles).  
2. `removeall_ft` uses `import functools` and `filter`.  
3. `removeall_rd` uses `import functools` and `reduce` (but not filter). 

So for example, 
   removeall_oo(0, [0, 0, 1])
should return
   [1]
and
   removeall_oo(0, [0, 0])
should return
   []
"""
import functools
def removeall_oo(i, l):
    while l.count(i): # counts how many times the value of 'i' appears within the list
        l.remove(i) # each time 'i' appears, it is removed from the list
    return l

def removeall_ft(i, l):
    return list(filter(lambda x: x % 2 != i, l))

def removeall_rd(i, l):
    from functools import reduce
    temp = [] # temp list to store values
    n = reduce(lambda x, y: x + y, l) # reduces the list to add all 1's together
    for j in range (0, n): # for the amount of 1's within the list, loop to append 1 into the temp list
        temp.append(1)
    return temp # return temp list


# END ANSWER TO Question 7
################################################################################


##########################################################
# Question 8

"""
The *Sudan* function is documented here:
   https://en.wikipedia.org/wiki/Sudan_function
Implement the Sudan function as a Python function `sudan(n, x, y)` by orienting the equalities and making recursive calls as appropriate.

Be careful: even `sudan(2,2,2)` freezes up my machine.
"""

def sudan(n, x, y):
    if n == 0: # if the amount of recursions is 0
        return x + y #adds the values of x and y together
    elif y == 0: # when the y value is 0
        return x # always return the original value of x
    else: # return the sudan mathematical function. Code below is formula given in the wiki page(https://en.wikipedia.org/wiki/Sudan_function), converted into code
        return sudan(n-1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y) # Fn+1(x, y+1) but changed to '-1' to not run function forever



# END ANSWER TO Question 8
################################################################################



###############################################################################
# Question 9 

"""
Write a brief but comprehensive essay that:
1. Surveys the modern uses and applications of Python.
2. Speculates on what it is about Python that has led to its popularity.
3. Speculates on the evolution of Python into the future.  

Your essay should not be long.  

For full marks your answer should demonstrate both factual and technical understanding of the programming languages landscape in general, and of Python's role --- technically, economically, and socially --- within it.
"""

"""
ANSWER:
The modern uses and application of Python are commonly seen in such areas such as Web Development (used in Pyramid), 
Game Development(was used in Battlefield 2 and includes tools such as Pygame), Software Development, Machine Learning and AI(tools such as NumPy), 
Desktop GUI(Toolkits such as PyGUI), Operating Systems (Ubuntu) and so forth.

Pythons popularity arises from its most common feature of simplifying all of the work via visualisation, support 
programming langugage, testing, large amount of toolkits and so forth.

With all of the glory that is given to Python, and how it is mostly used as common ground for educating newcomers
into coding[1], it is fair to say that Python will stay for a long time. As time goes, the evolution of this language
might lean towards producing more toolkits, simplifications and data structures for programmers to use whilst coding.

[1] = https://www.simplilearn.com/best-programming-languages-start-learning-today-article#:~:text=JavaScript%20and%20Python%2C%20two%20of,languages%20to%20learn%20for%20beginners.
P.S - Link above is used to prove the point mentioned
"""

"""
Here's a very brief example answer to Q9 above where "Python" is replaced by "Eggs".  Enjoy:

A chicken is cheap to keep, can produce an egg a day, and eggs come prepackaged and naturally resist spoilage.  For instance, eggs come out of a chicken with a natural antibacterial coating on their shells so that they can be stored at room temperature, which keeps transport costs low --- in the US eggs are washed, which stops them smelling of chickens' bottoms but removes this coating, which is why US eggs require refrigeration and UK eggs don't. 
[note now this combines *factual* and *technical* elements; an awareness of the egg as a thing, but also of supply chain economics, food safety, and a nice factoid which really proves I went beyond the first page of Google results -mjg] 

Eggs are nutritious, tasty, and filling.  They are easy to cook and are culturally well-established in the UK.  A proper superfood, in fact.  

Eggs do have dangers: when improperly handled they can carry salmonella.  More information at [hyperlink].  Eggs can crack, and then spoil quickly.  Occasionally eggs go invisibly bad, or the embryo incubates prematurely (nowadays, sophisticated scanning machines eliminate these from the food chain). 

Eggs also have applications in vaccine development, and unfortunately also in biological warfare as incubators for germs, and [more stuff here -mjg].

For the future, [stuff about vegans, changes in food preferences, vat-grown protein, environmental costs of keeping chickens, etc etc].

[I could keep this up for pages, I won't: we've gone beyond the shell of an answer, we've cracked it, and if we allow our enthusiasm to egg us on then it would over-egg the pudding and we'd get egg on our faces for writing a not-eggsactly-concise answer:  we stuffed enough eggs in this basket and should stop, before the reader finds it eggscrutiating.   
Now your turn please, with "Python" instead of "Egg".  Make me proud.  -mjg]
""" 

# END ANSWER TO Question 9 
###############################################################################


###############################################################################
# Question 10

"""
a. Explain in words the difference between 
   ([],[],[]) 
and 
   [[]]*3.
b. Explain in words what x points to in memory after we execute the following two commands:
     x = []
     x.append(x)
"""

"""
a) ([],[],[]) is a tuple, with a collection of objects, which are lists. [[]]*3(== [[],[],[]]) is a list, with a
   collection of nested lists.

b) After executing the following program, the x list is embedded inside of itself(outputs "[[...]]"). Since lists 
   have points to each object within the list, x would point to itself within memory.
"""

# END ANSWER TO Question 10 
###############################################################################

###############################################################################
# Question 11

"""
Python has infinite precision integer arithmetic.

Write your own infinite precision "sum", "product", and "to the power of" functions, that represent numbers as lists of digits between 0 and 9 with least significant digit first. 
Thus: 0 is represented as the empty list [], and 10 is represented as [0,1]. 
You may assume that numbers are non-negative (no need for negative numbers, or for subtraction).
Do NOT gut the question by mapping to python's native integers, performing the arithmetic there, and mapping back!
You may use earlier functions in the definitions of later ones. 

Add your own tests to the `test_cw.py` file.
"""

# map an integer n to its representation as a string of digits.
# no need to error-check for the case that n is negative
# e.g. iint(12) == [2,1]
def iint(n):
    if n == 0:
        return [] # If the given value is 0, return empty list
    else:
        temp = [] # temporary array to hold data
        m = str(n) # m is assigned as string of n for future usage
        while len(m) != 0: # takes the total length of the given number and loops until the length is 0. str is used in this case to allow the computer to see the amount of integers overall
            temp.append(int(m[-1])) # appends to the list the last integer of the value, and converts it into 'int' form
            m = m[0:len(m) - 1] # removes the last integer, that has just been appended, from the value
        return temp #returns the value in infinite form

# map the string-of-digit representation back to integers
# e.g. pint(iint(12)) == 12 
def pint(I):
    if I == []: # If given value is [], return 0
        return 0
    else:
        m = "" # created to easily add all integers into one value
        while len(I) != 0: # takes the total length of the list and stops looping once the length is 0
            m = m + str(I[-1]) # takes the last integer from the list, converts it into string, and adds it with existing string value. Each time a new integer is added it will add together with previous integer into one
            I = I[0:len(I) - 1] # removes the last integer, that was just added into the overall value, from the list
        return int(m) # returns the 'int' form of the final string value

# add two infinite integers
# e.g. iadd([5], [5]) = [0,1]
def iadd(I,J):
    if I == [] and J == []: # If both values are 0, return []
        return []
    else:
        temp = [] # temporary list to store final value
        r = 0 # value to stole remainder from addition
        if len(I) > len(J): # used to control if the value in list I is bigger than in list J. This will allow for no errors to happen while calculating
            for i in range (len(I)): # since the value in list I is larger, uses its length as the amount of times the addition will happen
                if i < len(J): # checks to see if list J has any integers or not, if does adds the position of i for both lists, and in case 'n' is more than 10, adds remainder of 1, else 0.
                    n = I[i] + J[i] + r
                else: # in case list J is originally empty, or when the length of list J finishes, yet list I still has some values left
                    n = I[i] + r # adds integers from list I to 'n'. In case there's remainder from previous calculation, adds it as well.
                if n > 9: # used for times when both added values are greater than 9
                    n = n - 10 # subtracted by 10, since max value in 'infinite integer' can be 9 
                    temp.append(n) # appends the final value to temp list
                    r = 1 
                else:
                    temp.append(n) # if n value fits boundary of 'infinite integers', instantly appends
            return temp # returns final value
        else: # in case both I and J equal to each other, or when J is of larger amount than I
            for j in range (len(J)): # from this point on repeats similar actions as mentioned above, but with J as priority instead of I
                if j < len(I):
                    n = I[j] + J[j] + r
                else:
                    n = J[j] + r
                if n > 9:
                    n = n - 10
                    temp.append(n)
                    r = 1
                else:
                    temp.append(n)
            return temp

# multiply two infinite integers
# e.g. imult([], [5]) = []
def imult(I,J):
    if I == [] or J == []: # If either of the numbers 0, always return []
        return []
    else:
        temp = I # holds original value of list I
        for i in range (pint(J) - 1): # loops for the range of the int value of list J, subtracts 1 to fit multiplication range required (assuming pint(J) = 3, since 'i' starts at 0, has to be done from 0-2, thus subtract 1)
            temp = iadd(temp, I) # temp is used for storage of the value after 1 addition (using iadd) is done, to then add new temp value with original list I value
        return temp # returns final value

# raise I to the power of J
def ipow(I,J):
    if I == []: # If the base number is 0, always return empty bracket
        return []
    elif J == []: # If 'to the power of' value is 0, always return 1
        return [1, 0]
    else:
        temp = I # holds original value of list I
        for i in range (pint(J) - 1): # similar logic as in 'imult'
            temp = imult(temp, I) # similar logic as in 'imult', but instead of 'iadd' uses 'imult'
        return temp # returns final value

# END ANSWER TO Question 11 
###############################################################################


###############################################################################
# Question 12

"""
Recall from Question 4 the notion of a *datum*.

a. Write a command `abstractsize` which inputs a datum and returns an integer measure of how much memory it occupies (cf. Question 10).
Note this measure should be in an abstract unit in which each integer occupies one unit of memory and each pair of square brackets occupies one unit of memory, modulo sharing, so that (for example) `[5,5]` has measure 3 --- one for the square brackets, and one for the two integer payloads.  (Do not try to return actual memory usage in bytes, since this will depend on implementation and on the size of the integer payload!) 
b. Write a command `compress` which inputs a datum, and outputs a datum that represents it and minimises abstract size.  Your code should be clear and well-commented with an explanation (if required) of the algorithm you use.

We're not looking for precise bytecounts and certainly not looking for speed or optimal performance.  Marks will be awarded for elegance, clear commenting, and understanding of the issues involved. 
"""

def abstractize(datum):
    total = 0 # original abstract memory size
    if len(datum) != 0: # if given a datum with at least 1 integer/square bracket
        total += 1 # instantly adds 1 for the square brackets used for datum
        for x in datum: # itirates for each element in datum
            if isinstance(x, list): # if given element is a list
                total += abstractize(x) # recursively repeats above process, until an integer is found, adding +1 for each time recursion was used
            else: # if given element is not a list
                total += 1 # just adds 1 to the total, representing an integer found
        return total #returns the final abstract size
    else:
        return 1 # returns 1 if an empty datum is given

def compress(datum):
    temp = []
    if len(datum) != 0: # if given a datum with at least 1 integer/square bracket
        for x in datum: # itirates for each element in datum
            if isinstance(x, list): # if given element is a list
                n = compress(x) # recursively repeats process of ignoring lists until integer is found
                for value in n: # itirates for the integer found within the list
                    temp.append(value) # appends the found integer into the temporary list
            else:
                temp.append(x) # if no square brackets are around integer, returns its original form
        return temp # returns compressed datum
    else:
        return datum # returns the original datum if no extra square brackets were found
# END ANSWER TO Question 12 
###############################################################################

###############################################################################
# Question 13 (bonus question) 

"""
The code below to define `equals23` takes up five lines and 83 characters, by my count. 
It is also ugly, redundant, and indirect.
Rewrite it, so that it is clean, compact, direct --- and takes up one line and 23 characters.
"""

def equals23(x):return x==23


# END ANSWER TO Question 13 
###############################################################################
