#Packages is where we collect similar python modules
#in folders so we can import them together and categorize
#This is how we build projects, for example : 

# project_root/
#   main.py
#   others/
#     __init__.py
#     Binary_Search.py

#main.py is where everything takes the start from
#It contains the necessary stuff to run the application
#and it calls everything that needs to be run in the application

#__init__.py is just an initializing module for each package
#In modern Python (3.3+), 
#a folder can sometimes act like a package without it (namespace packages).
#This is how you import a package : 

import package.Binary_Search as b

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b.binary_search(s, 9, 0, len(s) - 1))

#Use __import__ for 1 line imports : 
#__import__(name, globals=None, locals=None, fromlist=(), level=0)
print(__import__("package.Binary_Search", fromlist=["*"]).binary_search(s, 9, 0, len(s) - 1))

print(__import__("1").Class().class_attribute)