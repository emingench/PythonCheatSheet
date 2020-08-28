dbbasics = ["alpha-b-circle-outline",
            ["my_var = 10", "#type integer variable defining"],
            ["my_var = 'Hello'", "#type string variable defining"],
            ["my_var = True", "#type boolean variable defining"],
            ['input("Please enter the string you want to be printed out: ")', '#User input'],
            ['user_says = input("Please enter the string you want to be printed out: ")',
             '#Saving the input to a variable'],
            ]
dbstrings = ['alphabetical',
             ['''
a = "Emin"
a.index("i")
           ''', '#Strings - indexing'],
             ['''
a = "Emin"
a.count("i")
           ''', '#Strings - character count'],
             ['''
a = "Emin"
a.find("i")
           ''', '#Strings - character find'],
             ['a.lower()', '#lowercase'],
             ['a.upper()', '#uppercase'],
             ['a.startswith("E")', '#Strings - checking whether the string starts with a character'],
             ['a.endswith("c")', '#Strings - checking whether the string ends with a character'],
             ['a.strip()', '#remove whitespaces'],
             ['a.strip("&")', '#remove certain character'],
             ['a.replace(" ", "") ', '#replace each space character with the absence of any character'],
             ['a.split(",")',
              '#Strings - splitting a string by specifying a delimiter; the result is a list. #the delimiter is a comma'],
             ['"_".join(a)',
              '#Strings - inserting a character in between every two characters of the string joining the characters by using a delimiter'],
             ["capitalize()", "#Capitalizes first letter of string."],
             ["lstrip()", "#Removes all leading whitespace in string."],
             ["rstrip()", "#Removes all trailing whitespace of string."],
             ["swapcase()", "#Inverts case for all letters in string."],
             ["title()",
              '#Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.'],
             ["isalnum()",
              "#Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise"],
             ["isalpha()",
              "#Returns true if string has at least 1 character and all characters are alphabetic and false otherwise."],
             ["isdigit()", "#Returns true if string contains only digits and false otherwise."],
             ['islower()',
              '#Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.'],
             ['isnumeric()', '#Returns true if a unicode string contains only numeric characters and false otherwise.'],
             ['isspace()', '#Returns true if string contains only whitespace characters and false otherwise.'],
             ['istitle()', '#Returns true if string is properly "titlecased" and false otherwise'],
             ['isupper()',
              '#Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.'],
             ["""

a = "Hello"
b = " World"
a + b

""", "#Strings - concatenating two or more strings"],
             ["'hello'*3 : hellohellohello ", '#Strings - repetition / multiplying a string'],
             ["""

a = "Emin"
"e" in a : true
"i" not in a : false

""", "#Strings - checking if a character is or is not part of a string"],
             ["'Hello, %s' % name : 'Hello, Bob' ", "#Strings - formatting v1"],
             ["'Hello, {}'.format(name): 'Hello, Bob'", "#Strings - formatting v2"],
             ["f'Hello, {name}': 'Hello, Bob'", "#Strings - formatting v3 f formating"],
             ['string1[4:13]',
              '#slice starting at index 4 up to, but NOT including, index 13; so index 12 represents the last element in the slice'],
             ['string1[6:]', '#slice starting at index 6 up to the end of the string'],
             ['string1[:]', '#returns the entire string'],
             ['string1[-1]', '#returns the last character in the string'],
             ['string1[-2]', '#returns the second to last character in the string'],
             ['string1[-5:]', '#returns the last 5 characters in the string'],
             ['string1[:-5] ', '#returns the string minus its last 5 characters'],
             ['string1[::2]', '] #adds a third element called step; skips every second character of the string'],
             ["string1[::-1]", "#returns string1's elements in reverse order"]
             ]
dbnumbers = ['numeric',
             ['num1 = 10 \n type(num1)', '#checking the type of this variable; integer '],
             ['num2 = 2.5  \n type(num2)', ' #checking the type of this variable; float  '],
             ['int(1.5)', '#result is 1 '],
             ['float(2)', ' #result is 2.0 '],
             ['abs(5)', '#the distance between the number in between parantheses and 0 '],
             ['abs(-5)', '#returns the same result as abs(5) '],
             ['max(1, 2, 3 ,5, 7)', '#returns the largest number '],
             ['min(1, 2, 3 ,5, 7)', '#returns the smallest number '],
             ['pow(3, 2)', '#another way of raising to a power '],
             ['(1 == 1) and (2 == 2)',
              '#result is True; AND means that both operands should be True in order to get the expression evaluated as True'],
             ['(1 == 1) or (2 == 2)',
              '#result is True; when using OR, it is enough if only one expression is True, in order to have True as the final result '],
             ['not(1 == 1)',
              ' #result is False; using the NOT operator means denying an expression, in this case denying a True expression '],
             ['not(1 == 2)',
              '#result is True; using the NOT operator means denying an expression, in this case denying a False expression'],
             ['None, 0, 0.0, 0L, 0j, empty string, empty list, empty tuple, empty dictionary',
              ' #these values always evaluate to False '],
             ['bool(None)', '#returns False; function that evaluates values and expressions '],
             ['bool(0)', ' #returns False; function that evaluates values and expressions '],
             ['bool(2)', ' #returns True; function that evaluates values and expressions '],
             ['bool("router")', ' #returns True; function that evaluates values and expressions ']

             ]
dblists = ['view-list',
           ['list1 = ["Emin", "New york", "Lion", 3, 10.1, -14]', '#creating a list '],
           ['len(list)', '#returns the number of elements in the list '],
           ['list1[0]', '#returns "Emin" which is the first element in the list (index 0) '],
           ['list1[0] = "HP"', '#replacing the first element in the list with another value '],
           ['list2 = [-11, 2, 12]', 'min(list2)  #returns the smallest element (value) in the list '],
           ['list2 = [-11, 2, 12]', 'max(list2)  #returns the largest element (value) in the list '],
           ['list1.append(19)', '#appending a new element(19) to the list '],
           ['del list1[4]', '#removing an element from the list by index'],
           ['list1.pop(0)', ' #removing an element from the list by index'],
           ['list1.remove("HP")', '#removing an element from the list by value '],
           ['list1.insert(2, "Nortel")', '#inserting an element at a particular index '],
           ['list1.extend(list2)', '#appending a list to another list '],
           ['list1.index(-11)', ' #returns the index of element -11 '],
           ['list1.count(10)', '#returns the number of times element 10 is in the list '],
           ['list2 = [9, 99, 999, 1, 25, 500]',
            'list2.sort() #sorts the list elements in ascending order; modifies the list in place '],
           ['list2.reverse()', '#sorts the list elements in descending order; modifies the list in place'],
           ['sorted(list2)',
            '#sorts the elements of a list in ascending order and creates a new list at the same time '],
           ['sorted(list2, reverse = True)',
            ' #sorts the elements of a list in descending order and creates a new list at the same time '],
           ['list1 + list2', ' #concatenating two lists '],
           ['list1 * 3', '#repetition of a list '],
           ['a_list[5:15]',
            ' #slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice '],
           ['a_list[5:]', '#slice starting at index 5 up to the end of the list'],
           ['a_list[:10]', '#slice starting at the beginning of the list up to, but NOT including, index 10 '],
           ['a_list[:]', '#returns the entire list '],
           ['a_list[-1]', '#returns the last element in the list '],
           ['a_list[-2]', '#returns the second to last element in the list '],
           ['a_list[-9:-1]', '#extracts a certain sublist using negative indexes '],
           ['a_list[-5:]', '#returns the last 5 elements in the list '],
           ['a_list[:-5]', '#returns the list minus its last 5 elements '],
           ['a_list[::2]', '#adds a third element called step; skips every second element of the list '],
           ['a_list[::-1]', " #returns a_list's elements in reverse order "]

           ]

dbsets = ['set-none',
          ['set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"}',
           '#creating a set #Sets - unordered collections of unique elements'],
          ['list1 = [11, 12, 13, 14, 15, 15, 15, 11] -> set1 = set(list1)',
           '#creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}'],
          ['string1 = "aaabcdeeefgg" set2 = set(string1)',
           "#creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e '}; remember that sets are UNORDERED collections of elements"],
          ['len(set1)', '#returns the number of elements in the set'],
          ['11 in set1', '#returns True; checking if a value is an element of a set'],
          ['10 not in set 1 ', '#returns True; checking if a value is an element of a set'],
          ['set1.add(16)', '#adding an element to a set'],
          ['set1.remove(16)', '#removing an element from a set'],
          ['fs1 = frozenset(list1) ',
           '#Frozensets - immutable sets. #The elements of a frozenset remain the same after creation.'],
          ['type(fs1)', "<class 'frozenset'> #the result"],
          ["fs1.add(10) : AttributeError: 'frozenset' object has no attribute 'add' ",
           "#proving that frozensets are indeed immutable"],
          ["fs1.remove(1)", "AttributeError: 'frozenset' object has no attribute 'remove"],
          ["fs1.pop(1)", "AttributeError: 'frozenset' object has no attribute 'pop"],
          ["fs1.clear(1)", "AttributeError: 'frozenset' object has no attribute 'clear"],
          ["set1.intersection(set2) ", "#returns the common elements of the two sets"],
          ["set1.difference(set2)", "#returns the elements that set1 has and set2 doesn't"],
          ["set1.union(set2)",
           "#unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation"],
          ["set1.pop() ",
           "#removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use"],
          ["set1.clear() ", "#clearing a set; the result is an empty set"]

          ]

dbtuples = ['format-list-text',
            ["my_tuple = ()",
             "#creating an empty tuple #Tuples - immutable lists (their contents cannot be changed by adding, removing or replacing elements)"],
            ["my_tuple = (9,) ", " #creating a tuple with a single element; DO NOT forget the comma"],
            ["my_tuple = (1, 2, 3, 4) len(my_tuple):4 ",
             "#Tuples - the same indexing & slicing rules apply as for lists"],
            ['tuple1 = ("Bob", "Marley", "27") \n (name, surname, age) = tuple1 ',
             "#Tuples - tuple assignment / packing and unpacki"],
            ["(a, b, c) = (1, 2, 3)", " #assigning values in a tuple to variables in another tuple"],
            ["min(tuple1)", "#returns min"],
            ["max(tuple1)", "#returns max"]
            ]

dbranges = ['diameter',
            ["r = range(10)",
             "#defining a range #Ranges - unlike in Python 2, where the range() function returned a list, in Python 3 it returns an iterator; cannot be sliced"],
            ["type(r)", "<class 'range'> #the result"],
            ["list(r) ", "#converting a range to a list : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #the result"],
            ["list(r)[2:5]", "#slicing a range by using the list() function first:  [2, 3, 4] #the result"]

            ]
dbdictionaries = ['notebook',
                  ["dict1 = {} ", "#Dictionaries - a dictionary is an unordered set of key-value pairs"],
                  ['dict1 = {"Name": "Bob", "Surname": "Marley", "Age": "27"}', ' #creating an empty dictionary '],
                  ['dict1["Age"] ', '#returns "27"; extracting a value for a specified key'],
                  ['dict1["Age"] = "35" ', "#modifies an existing key-value pair"],
                  ['dict1["Pet"] = "Dog"', ' #adds a new key-value pair to the dictionary'],
                  ['del dict1["Age"]', '#deleting a key-value pair from the dictionary'],
                  ['len(dict1)', '#returns the number of key-value pairs in the dictionary'],
                  ['"Name" in dict1 ', '#verifies if "Name" is a key in the dictionary'],
                  ['"Phone" not in dict1', '#verifies if "Phone" is not a key in the dictionary'],
                  ["dict1.keys()", "#returns a list having the keys in the dictionary as elements"],
                  ["dict1.values()", "#returns a list having the values in the dictionary as elements"],
                  ["dict1.items()",
                   " #returns a list of tuples, each tuple containing the key and value of each dictionary pair"],
                  ["str() ", "#converting to a string"],
                  ["int() ", "#converting to a integer"],
                  ["float() ", "#converting to a float"],
                  ["list() ", "#converting to a list"],
                  ["tuple() ", "#converting to a tuple"],
                  ["set() ", "#converting to a set"],
                  ["bin() ", "#converting to a binary representation"],
                  ["hex() ", "#converting to a hexadecimal representation"],
                  ["int(variable, 2)", "#converting from binary back to decimal"],
                  ["int(variable, 16)", "#converting from hexadecimal back to decimal"]
                  ]
dbconditionals = ['arrow-all',
                  ["",
                   '#If / Elif / Else conditionals - executing code based on one or more conditions being evaluated as True or False; the "elif" and "else" clauses are optional'],
                  ['x = 5 \n if x > 5: \n     print("x is greater than 5")',
                   '#if the "x > 5" expression is evaluated as True, the code indented under the "if" clause gets executed, otherwise the execution jumps to the "elif" clause...'],
                  ['elif x == 5: \n     print("x IS 5")',
                   '#...if the "x == 5" expression is evaluated as True, the code indented under the "elif" clause gets executed, otherwise the execution jumps to the "else" clause'],
                  ['else: \n     print("x is NOT greater than 5" ) ',
                   '#this covers all situations not covered by the "if" and "elif" clauses; the "else" clause, if present, is always the last clause in the code block']
                  ]
dbfor = ['arrow-decision',
         ["",
          '#For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional'],
         ["for element in ['Bob', 'Marley', '27']:\n     print(element)",
          '#interating over a sequence and executing the code indented under the "for" clause for each element in the sequence'],
         ['else:\n     print("The end of the list has been reached") ',
          '#the indented code below "else" will be executed when "for" has finished looping over the entire list'],
         ['Bob\nMarley\n27\nThe end of the list has been reached', '#result of the above "for" block'],
         ["",
          '#While / While Else loops - a while loop executes as long as an userspecified condition is evaluated as True; the "else" clause is optional'],
         [
             'x = 1\nwhile x <= 10:\n    print(x)\n    x += 1\nelse:\n    print("Out of the while loop. x is now greater than 10")',
             '#result of the above "while" block \n 1 2 3 4 5 6 7 8 9 10\nOut of the while loop. x is now greater than 10']
         ]
dbbreak = ['stop-circle-outline',
           [
               'list1 = [4, 5, 6]\nlist2 = [10, 20, 30]\nfor i in list1:\n    for j in list2:\n        \n            if j == 20:\n                break\n           print(i * j)\n       print("Outside the nested loop)"\n#result of the above block: 40\nOutside the nested loop\n50\nOutside the nested loop\n60\nOutside the nested loop',
               '''#stops the execution here, ignores the print statement below and completely quits THIS "for" loop; however, it doesn't quit the outer "for" loop, too!'''],
           [
               'list1 = [4, 5, 6]\nlist2 = [10, 20, 30]\nfor i in list1:\n    for j in list2:\n        \n            if j == 20:\n                continue\n           print(i * j)\n       print("Outside the nested loop)"\n#result of the above block: 40\n120\nOutside the nested loop\n50\n150\nOutside the nested loop\n60\n180\nOutside the nested loop',
               '''#ignores the rest of the code below for the current iteration, then goes up to the top of the loop (inner "for") and starts the next iteration'''],
           ["for i in range(10):\n    pass",
            '#pass is the equivalent of "do nothing"; it is actually a placeholder for when you just want to write a piece of code that you will treat later']
           ]
dbtry = ['play',
         [
             '''#Try / Except / Else / Finally - handling an exception when it occurs and telling Python to keep executing the rest of the lines of code in the program''',
             'try:\n     print(4/0)'],
         ['except ZeroDivisionError:\n    print("Division Error!")',
          '#specifying what exception types Python should expect as a consequence of running the code inside the "try" block and how to handle them'],
         ['else:\n    print("No exceptions raised by the try block!")',
          '#executed if the code inside the "try" block raises NO exceptions'],
         ['finally:\n    print("I don\'t care if an exception was raised or not!")',
          '#executed whether the code inside the "try" block raises an exception or not']

         ]
dbfunctions = ['function',
               [
                   'def my_first_function(x, y):\n    sum = x + y\n    return sum :#this statement is used to exit a function and return something when the function is called',
                   '#defining a function that takes two parameters'],
               ['my_first_function(1, 2)',
                '#calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3'],
               ['#calling a function and passing two POSITIONAL arguments, the values of 1 and 2; result is 3',
                '#calling a function and passing two KEYWORD arguments, the values of 1 and 2; result is 3'],
               ['my_first_function(1, y = 2)',
                '#calling a function and passing mixed types of arguments, the values of 1 and 2; result is 3; rule: positional arguments always before keyword arguments!'],
               ['def my_first_function(x, y, z = 3):',
                '#specifying a default parameter value in a function definition'],
               ['def my_first_function(x, *args)',
                '#specifying a variable number of positional parameters in a function definition; args is a tuple'],
               ['def my_first_function(x,**kwargs)',
                '#specifying a variable number of keyword parameters in a function definition; args is a tuple'],
               ['global my_var', '#"importing" a variable in the global namespace to the local namespace of a function']
               ]
dbmodules = ['view-module',
             ['import sys',
              '#importing the sys module; the import statements should be placed before any other code in your application'],
             ['from math import pi', '#importing only a variable (pi) from the math module'],
             ['from math import sin',
              '''#importing only a function (sin()) from the math module; there's no need to add the parantheses of the function when importing it'''],
             ['from math import *', '#importing all the names (variables and functions) from the math module'],
             ['C:\WINDOWS\system32> pip install openpyx ',
              '#Installing a non-default Python 3 module in Windows is done from the command line (e.g. the openpyxl module)', ],
             ['mihais-MacBook-Pro:~ mihai$ pip3 install openpyx',
              '#Installing a non-default Python 3 module in macOS is done from the terminal (e.g. the openpyxl module)']
             ]
dbfileoperations = ['file',
                    ['myfile = open("routers.txt", "r")',
                     '#"r" is the file access mode for reading and it is the default mode when opening a file'],
                    ['myfile.mode', '#checking the mode in which a file has been opened'],
                    ['myfile.read()', '#method that returns the entire content of a file in the form of a string'],
                    ['myfile.read(5)', '#returning only the first 5 characters (bytes) in the file'],
                    ['myfile.seek(0)', '#moving the cursor at the beginning of the file'],
                    ['myfile.tell()', '#checking the current position of the cursor inside the file'],
                    ['myfile.readline()', '#returns the file content one line a ta time, each time you use the method'],
                    ['myfile.readlines()', '#returns a list where each element is a line in the file'],
                    ['newfile = open("newfile.txt", "w")',
                     '#opens/creates a new file for writing; the "w" method also creates the file for writing if the file doesn’t exist and overrides the file if the file already exists; remember to close the file after writing to it to save the changes!'],
                    ['newfile.writelines(["bob", "mars", "HP", "\\n"])',
                     '#this method takes a sequence of strings as an argument and writes those strings to the file'],
                    ['newfile = open("newfile.txt", "a")', '#opening a file for appending'],
                    ['newfile = open("newfile.txt", "w+")',
                     '#opens a file for both writing and reading at the same time'],
                    ['newfile = open("newfile.txt", "x")',
                     '#opens for exclusive creation, failing if the file already exists'],
                    ['newfile.closed', '#checking if a file is closed'],
                    ['newfile.close()', '#closing a file'],
                    ['with open("python.txt", "w") as f:\n        f.write("Hello Python!\\n")',
                     '#using the with-as solution, the files gets closed automatically, without needing the close() method'],
                    ['f = open("D:\\\\test.txt", "r+")\nf.truncate()', '#this deletes all the content inside the file'],
                    ['f = open("D:\\test.txt", "r+")\nf.truncate(10)',
                     '#this will keep the first 10 characters in the file and delete the rest']
                    ]
dbregex = ['regex',
           ['a = re.match(pattern, string, optional flags)',
            '#general match syntax; "a" is called a match object if the pattern is found in the string, otherwise "a" will be None'],
           [
               'mystr ="You can learn any programming language, whether it is Python2,Python3, Perl, Java, javascript or PHP.\nimport re #importing the regular expressions module\na = re.match("You", mystr)"',
               '#checking if the characters "You" are indeed at the beginning of the string'],
           ['a.group()',
            '''#result is 'You'; Python returns the match it found in the string according to the pattern we provided'''],
           ['a = re.match("you", mystr, re.I)', '#re.I is a flag that ignores the case of the matched characters'],
           ['a = re.search(pattern, string, optional flags)',
            '''#general search syntax; searching for a pattern throughout the entire string; will return a match object if the pattern is found and None if it's not found'''],
           ['arp = "22.22.22.1 0 b4:a9:5a:ff:c8:45 VLAN#222 L"\na = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)',
            '''#result is '22.22.22.1'; 'r' means the pattern should be treated like a raw string; any pair of parentheses indicates the start and the end of a group; if a match is found for the pattern inside the parentheses, then the contents of that group can be extracted with the group() method applied to the match object; in regex syntax, a dot represents any character, except a new line character; the plus sign means that the previous expression, which in our case is just a dot,may repeat one or more times; the question mark matching as few characters as possible'''],
           ['a.groups()', '''#returns all matches found in a given string, in the form of a tuple, where each match is an element of that tuple
('22.22.22.1', '0', 'b4:a9:5a:ff:c8:45 VLAN#222', 'L')'''],
           ['a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)',
            '#returns a list where each element is a pattern that was matched inside the target string \n [\'22.22.22.1\'] #result of the above operation - a list with only one element, the IP address matched by the regex'],
           ['b = re.sub(r"\d", "7", arp)',
            '''#replaces all occurrences of the specified pattern in the target string with a string you enter as an argument \n '77.77.77.7 7 b7:a7:7a:ff:c7:77 VLAN#777 L 77.77.77.77' #result of the above operation''']
           ]
dbOOP = ['view-day',
         [
             'class MyRouter(object):#creating a class which inherts from the default "object" class\n         def __init__(self, routername, model, serialno, ios):#class constructor; initializing some variables and the method is called whenever you create a new instance of the class\n                  self.routername = routername #"self" is a reference to the current instance of the class \n                  self.model = model\n                  self.serialno = serialno\n                  self.ios = ios',
             ''],
         ['''    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)
         ''',
          '''router1 = MyRouter('R1', '2600', '123456', '12.4') #creating an object by simply calling the class name and entering the arguments required by the __init__ method in between parentheses'''],
         ['router1.model', "#accessing the object's attributes; result is '2600'"],
         ['router1.print_router("20150101")', '''#accessing a function (actually called method) from within the class
The router name is: R1
The router model is: 2600
The serial number of: 123456
The IOS version is: 12.4
The model and date combined: 260020150101'''],
         ['''getattr(router1, "ios") #getting the value of an attribute
setattr(router1, "ios", "12.1") #setting the value of an attribute
hasattr(router1, "ios") #checking if an object attribute exists
delattr(router1, "ios") #deleting an attribute''',
          'isinstance(router1, MyRouter) #verifying if an object is an instance of a particular class'],
         ['class MyNewRouter(MyRouter): #creating a new class (child) inheriting from the MyRouter parent class',
          'issubclass(MyNewRouter, MyRouter) #returns True or False; checking if a class is the child of another class']
         ]
dblistcomp = ['format-list-bulleted',
              ['''#Instead of...
list1 = []
for i in range(10):
j = i ** 2
list1.append(j)''', '''#...we can use a list comprehension
list2 = [x ** 2 for x in range(10)]
list3 = [x ** 2 for x in range(10) if x > 5] #with a conditional statament
set1 = {x ** 2 for x in range(10)} #set comprehension
dict1 = {x: x * 2 for x in range(10)} #dictionary comprehension''']
              ]
dblambda = ['lambda',
            ['a = lambda x, y: x * y\na(20, 10)\n#result is 200; calling the lambda function',
             '#defining a lambda function'],
            ['''#Instead of...
def myfunc(list):
    prod_list = []
    for x in range(10):
        for y in range(5):
            product = x * y
            prod_list.append(product)
    return prod_list + list''', '''#...we can use a lambda function, a list comprehension and concatenation on a single line of code
b = lambda list: [x * y for x in range(10) for y in range(5)] + list''']]
dbmap = ['select-all',
         [
             '#map() - takes a function and a sequence as arguments and applies the function to all the elements of the sequence, returning a list as the result',
             ''],
         ['''def product10(a):
    return a * 10

list1 = range(10)
map(product10, list1)''', '''#result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]; applying the product10() function to each element of list1
#or...
map((lambda a: a * 10), list1) #result is [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] as well'''],
         [
             '#filter() - takes a function and a sequence as arguments and extracts all the elements in the list for which the function returns True',
             'filter(lambda a: a > 5, list1) #result is [6, 7, 8, 9]']
         ]
dbiter = ['card-plus-outline',
          ['#Iterators - an object which allows a programmer to traverse through all the elements of a collection',' '],
          ['my_list = [1, 2, 3, 4, 5, 6, 7]\nmy_iter = iter(my_list) #iter() returns an interator object','next(my_iter) #in Python 2 and 3, it returns the elements of a sequence one by one; raises StopIteration when the sequence is exhausted'],
          ['''#Generators - special routines that can be used to control the iteration behavior of a loop; defined using the "def" keyword;
def my_gen(x, y): #creating a generator function
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y #yields the values one at a time; traversing a sequence up
to a certain point, getting the result and suspending the execution''',' '],
          ['my_object = my_gen(10, 5)','#creating a generator object\nnext(my_object) #manually yield the next element returned by the my_gen() function; raises StopIteration when the sequence is exhausted'],
          ['gen_exp = (x for x in range(5)) #creating a generator expression; similar to list comprehensions, but using parentheses instead of square brackets','next(gen_exp) #extracting each value in the list generated by range(5),one value at a time; raises StopIteration when the sequence is exhausted']
          ]
dbitertools = ['tools',
               ['#Itertools - built-in Python module for working with iterable data sets','import itertools '],
               ['''list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']''','''#chain() - takes several sequences and chains them together
chain(list1, list2)
list(chain(list1, list2)) #result is [1, 2, 3, 'a', 'b', 'c', 101, 102, 103, 'X', 'Y']'''],
               ['''#count() - returns an iterator that generates consecutive integers until you stop it, otherwise it will go on forever
for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break''','#result is printing the numbers between 10 and 50 inclusively, with a step of 2.5'],
               ['#cycle() - returns an iterator that simply repeats the value given as argument infinitely; you have to find a way to break out of the infinite loop','''a = range(11, 16)
for i in cycle(a):
    print(i) #use Ctrl+C to break out of the infinite loop'''],
               ['#filterfalse() - returns the elements for which the function you give as argument returns False','list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])) #in Python 2 the result is [5, 6, 7]; in Python 3 there is no ifilter() like in Python 2, just filter() and filterfalse()'],
               ['#islice() - performs slicing; we can specify a starting point of the slice, an end point and a step','list(islice(range(10), 2, 9, 2)) #result is [2, 4, 6, 8]']

               ]
dbdecor = ['attachment',
           ['''#Decorators - functions that take another function as a parameter and extend its functionality and behavior without modifying it''','''def my_decorator(target_function):
    def function_wrapper():
        return "Python is the " + target_function() + " programming language!"
    return function_wrapper

@my_decorator
def target_function():
    return "coolest"

target_function() #returns 'Python is the coolest programming language!''']]

db = {
    "Basics": dbbasics,
    "Strings": dbstrings,
    "Numbers and Booleans": dbnumbers,
    "Lists": dblists,
    "Sets and Frozensets": dbsets,
    "Tuples": dbtuples,
    "Ranges": dbranges,
    "Dictionaries&Conversions": dbdictionaries,
    "Conditionals": dbconditionals,
    "For and While Loops": dbfor,
    "Break / Continue / Pass": dbbreak,
    "Try / Except / Else / Finally ": dbtry,
    "Functions": dbfunctions,
    "Modules": dbmodules,
    "File Operations": dbfileoperations,
    "Regular Expressions": dbregex,
    "Basics of OOP": dbOOP,
    "List comprehensions": dblistcomp,
    "Lambda functions": dblambda,
    "map() and filter()": dbmap,
    "Iterators and Generators": dbiter,
    "itertools": dbitertools,
    "Decorators": dbdecor
}
