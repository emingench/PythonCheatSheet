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
dbnumbers=['numeric']
dblists=['view-list']
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