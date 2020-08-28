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
dbtry = ['play']
dbfunctions = ['function']
dbmodules = ['view-module']
dbfileoperations = ['file']
dbregex = ['regex']
dbOOP = ['view-day']
dblistcomp = ['format-list-bulleted']
dblambda = ['lambda']
dbmap = ['select-all']
dbiter = ['card-plus-outline']
dbitertools = ['tools']
dbdecor = ['attachment']

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
