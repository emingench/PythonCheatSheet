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