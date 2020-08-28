dbbasics=["alpha-b-circle-outline",
        ["my_var = 10","#type integer variable defining"],
        ["my_var = 'Hello'","#type string variable defining"],
        ["my_var = True", "#type boolean variable defining"],
        ['input("Please enter the string you want to be printed out: ")','#User input'],
        ['user_says = input("Please enter the string you want to be printed out: ")','#Saving the input to a variable'],
          ]
dbstrings=['alphabetical',
['''
a = "Emin"
a.index("i")
           ''','#Strings - indexing'],
['''
a = "Emin"
a.count("i")
           ''','#Strings - character count'],
['''
a = "Emin"
a.find("i")
           ''','#Strings - character find'],
['a.lower()','#lowercase'],
['a.upper()','#uppercase'],
['a.startswith("E")','#Strings - checking whether the string starts with a character'],
['a.endswith("c")','#Strings - checking whether the string ends with a character'],
['a.strip()','#remove whitespaces'],
['a.strip("&")','#remove certain character'],
['a.replace(" ", "") ','#replace each space character with the absence of any character'],
['a.split(",")','#Strings - splitting a string by specifying a delimiter; the result is a list. #the delimiter is a comma'],
['"_".join(a)','#Strings - inserting a character in between every two characters of the string joining the characters by using a delimiter'],
["capitalize()","#Capitalizes first letter of string."],
["lstrip()","#Removes all leading whitespace in string."],
["rstrip()","#Removes all trailing whitespace of string."],
["swapcase()","#Inverts case for all letters in string."],
["title()",'#Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.'],
["isalnum()","#Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise"],
["isalpha()","#Returns true if string has at least 1 character and all characters are alphabetic and false otherwise."],
["isdigit()","#Returns true if string contains only digits and false otherwise."],
['islower()','#Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.'],
['isnumeric()','#Returns true if a unicode string contains only numeric characters and false otherwise.'],
['isspace()','#Returns true if string contains only whitespace characters and false otherwise.'],
['istitle()','#Returns true if string is properly "titlecased" and false otherwise'],
['isupper()','#Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.'],
["""

a = "Hello"
b = " World"
a + b

""","#Strings - concatenating two or more strings"],
["'hello'*3 : hellohellohello ",'#Strings - repetition / multiplying a string'],
["""

a = "Emin"
"e" in a : true
"i" not in a : false

""","#Strings - checking if a character is or is not part of a string"],
["'Hello, %s' % name : 'Hello, Bob' ","#Strings - formatting v1"],
["'Hello, {}'.format(name): 'Hello, Bob'","#Strings - formatting v2"],
["f'Hello, {name}': 'Hello, Bob'","#Strings - formatting v3 f formating"],
['string1[4:13]','#slice starting at index 4 up to, but NOT including, index 13; so index 12 represents the last element in the slice'],
['string1[6:]','#slice starting at index 6 up to the end of the string'],
['string1[:]', '#returns the entire string'],
['string1[-1]', '#returns the last character in the string'],
['string1[-2]', '#returns the second to last character in the string'],
['string1[-5:]', '#returns the last 5 characters in the string'],
['string1[:-5] ', '#returns the string minus its last 5 characters'],
['string1[::2]','] #adds a third element called step; skips every second character of the string'],
["string1[::-1]", "#returns string1's elements in reverse order"]
   ]
dbnumbers=['numeric',
['num1 = 10 \n type(num1)','#checking the type of this variable; integer '],
['num2 = 2.5  \n type(num2)',' #checking the type of this variable; float  '],
['int(1.5)','#result is 1 '],
['float(2)',' #result is 2.0 '],
['abs(5)','#the distance between the number in between parantheses and 0 '],
['abs(-5)','#returns the same result as abs(5) '],
['max(1, 2, 3 ,5, 7)','#returns the largest number '],
['min(1, 2, 3 ,5, 7)','#returns the smallest number '],
['pow(3, 2)','#another way of raising to a power '],
['(1 == 1) and (2 == 2)','#result is True; AND means that both operands should be True in order to get the expression evaluated as True'],
['(1 == 1) or (2 == 2)', '#result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result '],
['not(1 == 1)',' #result is False; using the NOT operator means denying an expression, in this case denying a True expression '],
['not(1 == 2)','#result is True; using the NOT operator means denying an expression, in this case denying a False expression'],
['None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary',' #these values always evaluate to False '],
['bool(None)','#returns False; function that evaluates values and expressions '],
['bool(0)',' #returns False; function that evaluates values and expressions '],
['bool(2)',' #returns True; function that evaluates values and expressions '],
['bool("router")',' #returns True; function that evaluates values and expressions ']

           ]
dblists=['view-list',
['list1 = ["Emin", "New york", "Cow", 3, 10.1, -14]','#creating a list '],
['len(list)','#returns the number of elements in the list '],
['list1[0]','#returns "Emin" which is the first element in the list (index 0) '],
['list1[0] = "HP"','#replacing the first element in the list with another value '],
['list2 = [-11, 2, 12]','min(list2)  #returns the smallest element (value) in the list '],
['list2 = [-11, 2, 12]','max(list2)  #returns the largest element (value) in the list '],
['list1.append(19)','#appending a new element(19) to the list '],
['del list1[4]','#removing an element from the list by index'],
['list1.pop(0)',' #removing an element from the list by index'],
['list1.remove("HP")','#removing an element from the list by value '],
['list1.insert(2, "Nortel")','#inserting an element at a particular index '],
['list1.extend(list2)','#appending a list to another list '],
['list1.index(-11)',' #returns the index of element -11 '],
['list1.count(10)','#returns the number of times element 10 is in the list '],
['list2 = [9, 99, 999, 1, 25, 500]','list2.sort() #sorts the list elements in ascending order; modifies the list in place '],
['list2.reverse()','#sorts the list elements in descending order; modifies the list in place'],
['sorted(list2)','#sorts the elements of a list in ascending order and creates a new list at the same time '],
['sorted(list2, reverse = True)',' #sorts the elements of a list in descending order and creates a new list at the same time '],
['list1 + list2',' #concatenating two lists '],
['list1 * 3','#repetition of a list '],
['a_list[5:15]',' #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice '],
['a_list[5:]','#slice starting at index 5 up to the end of the list'],
['a_list[:10]','#slice starting at the beginning of the list up to, but NOT including, index 10 '],
['a_list[:]','#returns the entire list '],
['a_list[-1]','#returns the last element in the list '],
['a_list[-2]','#returns the second to last element in the list '],
['a_list[-9:-1]','#extracts a certain sublist using negative indexes '],
['a_list[-5:]','#returns the last 5 elements in the list '],
['a_list[:-5]','#returns the list minus its last 5 elements '],
['a_list[::2]','#adds a third element called step; skips every second element of the list '],
['a_list[::-1]'," #returns a_list's elements in reverse order "]

         ]

dbsets=['set-none']
dbtuples=['format-list-text']
dbranges=['diameter']
dbdictionaries=['notebook']
dbconditionals=['arrow-all']
dbfor=['arrow-decision']
dbif=['arrow-decision-outline']
dbbreak=['stop-circle-outline']
dbtry=['play']
dbfunctions=['function']
dbmodules=['view-module']
dbfileoperations=['file']
dbregex=['regex']
dbOOP=['view-day']
dblistcomp=['format-list-bulleted']
dblambda=['lambda']
dbmap=['select-all']
dbiter=['card-plus-outline']
dbitertools=['tools']
dbdecor=['attachment']



db = {
"Basics":dbbasics ,
"Strings":dbstrings ,
"Numbers and Booleans":dbnumbers,
"Lists":dblists,
"Sets and Frozensets":dbsets,
"Tuples":dbtuples,
"Ranges":dbranges,
"Dictionaries. Conversions between data types":dbdictionaries,
"Conditionals":dbconditionals,
"For and While Loops":dbfor,
"If / For / While Nesting": dbif,
"Break / Continue / Pass": dbbreak,
"Try / Except / Else / Finally ": dbtry,
"Functions": dbfunctions,
"Modules": dbmodules,
"File Operations": dbfileoperations,
"Regular Expressions": dbregex,
"Basics of OOP. Classes and Objects": dbOOP,
"List comprehensions" : dblistcomp,
"Lambda functions": dblambda,
"map() and filter()": dbmap,
"Basics of Iterators and Generators": dbiter,
"itertools": dbitertools,
"Basics of Decorators": dbdecor
}