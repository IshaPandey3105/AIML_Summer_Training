# ----------------------------------------------------------
# Module in Python
# ----------------------------------------------------------
# A module is a file that contains a collection of related functions, classes, and variables.
# It can be used to organize code, reuse code, and make it easier to maintain and update
# Modules are imported into a Python program using the import statement.

# ----------------------------------------------------------
# Types of Modules
# ----------------------------------------------------------
# 1. Built-in Modules
# 2. User-defined Modules
# 3. Third-party Modules

# ----------------------------------------------------------
# 1. Built-in Modules: 
# ----------------------------------------------------------
# These are modules that are part of the Python standard library.
# They are available by default and do not need to be installed separately.
# Examples of built-in modules include math, random, and time.

# ----------------------------------------------------------
# ✅1. math Module — for Mathematical Operations
# ----------------------------------------------------------
import math
print(math.pi)               # 3.1415...
print(math.sqrt(16))         # Square root => 4.0
print(math.pow(2, 3))        # Power => 8.0
print(math.factorial(5))     # 120
print(math.floor(2.9))       # 2 (rounds down)
print(math.ceil(2.1))        # 3 (rounds up)

# ----------------------------------------------------------
# ✅2. random Module — for Random Numbers
# ----------------------------------------------------------
import random
print(random.random())  # Random float in [0.0, 1.0)
print(random.randint(1, 10))  # Random integer in [1, 10)
print(random.choice([1, 2, 3, 4, 5]))  # Random element from a list
print(random.choice(['AI', 'ML', 'DL']))  # Random choice

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)                 # Shuffles the list in-place
print(list1)

# ----------------------------------------------------------
# ✅3. datetime Module — for Date and Time
# ----------------------------------------------------------
import datetime
today = datetime.date.today()
print("Today:", today)

now = datetime.datetime.now()
print("Current time:", now)

birthday = datetime.date(2005, 5, 10)
age = today.year - birthday.year
print("Age:", age)

# ----------------------------------------------------------
# ✅4. time Module — for Delays, Time Tracking
# ----------------------------------------------------------
import time
print("Wait for 1 seconds...")
time.sleep(1)
print("Done waiting!")

# ----------------------------------------------------------
# ✅5. sys Module — System-specific Parameters
# ----------------------------------------------------------
import sys
print("Python version:", sys.version)
print("Command line args:", sys.argv)  

# ----------------------------------------------------------
# ✅6. statistics Module — for Data Stats
# ----------------------------------------------------------
import statistics
data = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Stdev:", statistics.stdev(data))

# ----------------------------------------------------------
# ✅7. calendar Module — For Monthly/Yearly Calendars
# ----------------------------------------------------------
import calendar
print(calendar.month(2025, 6))      # Calendar of June 2025
print(calendar.isleap(2024))       # True (leap year)

# ----------------------------------------------------------
# 2. user-defined Modules:
# ----------------------------------------------------------
# It is just a .py file created by you that contains variables, functions, or classes — which you can import into other Python files.

import MyModule  # Importing a module
n = input("Enter name : ")
print(MyModule.greet(n)) 
print("Square of 5:", MyModule.square(5))
print("Value of pi:", MyModule.pi) 

print("##################")
import os            # os is a built-in module use to interact with the operating system and give the information about the system.
print(os.getcwd())

import sys           # sys is a built-in module use to interact with the Python interpreter and give the information about the Python interpreter.
print(sys.path)   # escape sequence are \n ,\t
sys.path.append(r"D:\dev_py\modules")
print(sys.path)     # append path to sys.path


# ----------------------------------------------------------
# 3. Third-party Modules (External Modules)
# ----------------------------------------------------------
# You install these using pip.
# 👉 Example:

# numpy – for numerical operations

# pandas – for data analysis

# matplotlib – for data visualization 

# sklearn - for machine learning

# pytorch - for deep learning

# seabon - for data visualization

# tensorflow - for deep learning

# keras - for deep learning

# # ----------------------------------------------------------
# 3. Third-party Modules (External Modules)
# ----------------------------------------------------------
# You install these using pip.
# 👉 Example:

# numpy – for numerical operations

# pandas – for data analysis

# matplotlib – for data visualization 

# sklearn - for machine learning

# pytorch - for deep learning

# seabon - for data visualization

# tensorflow - for deep learning

# keras - for deep learning
# ----------------------------------------------------------
# 3. Third-party Modules (External Modules)
# ----------------------------------------------------------
# You install these using pip.
# 👉 Example:

# numpy – for numerical operations

# pandas – for data analysis

# matplotlib – for data visualization 

# sklearn - for machine learning

# pytorch - for deep learning

# seabon - for data visualization

# tensorflow - for deep learning

# keras - for deep learning# ----------------------------------------------------------
# 3. Third-party Modules (External Modules)
# ----------------------------------------------------------
# You install these using pip.
# 👉 Example:

# 🔢 Numerical & Scientific Computing
# numpy – for numerical operations
# scipy – for scientific computations

# 📊 Data Handling & Analysis
# pandas – for data manipulation
# dask – for parallel data processing

# 📈 Data Visualization
# matplotlib – for basic 2D plotting
# seaborn – for statistical data visualization

# 🤖 Machine Learning
# sklearn – for traditional ML algorithms
# xgboost – for gradient boosting

# 🧠 Deep Learning
# tensorflow – deep learning framework by Google
# pytorch – deep learning framework by Facebook
# keras – deep learning framework by Google

# 💬 Natural Language Processing (NLP)
# nltk – natural language toolkit
# transformers – pretrained models like BERT, GPT (by HuggingFace)

# 🧹 Data Cleaning
# missingno – for visualizing missing data
# fuzzywuzzy – for fuzzy string matching

# 🌐 Web Development
# flask – lightweight web framework
# django – full-featured web framework