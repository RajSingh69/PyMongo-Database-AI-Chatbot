# PyMongo-Database-AI-Chatbot
A data storage system for the 'DARK CITY' AI chatbot using the MongoDB database storage system.

# HOW TO START THE CODE

When everything is all set up:
	Python is installed
	IDE is installed
	All packages are installed
	
	Code developer has been contacted for missing .env file. This file is not uploaded as it contains VERY sensitive information.
  
  Press run like normal. :)

# Software needed to run this script

Python - This is the language the database is coded in (regarding the interaction). Use most recent version.
IDE - This is for easier viewing and additional coding if needed

# Packages used to run this project

os - Used with the operating system and allows for extra commands.
pprint - pprint (pretty print) is used for printing data in a nicer way
pymongo - The python addition for MongoDB
MongoClient - Needed to access the mongoDb client and database creation / addition services
datetime - Used for getting the current date and time
dotenv - Used for creating and accessing .env files (used for data storage)

# Commands to install the needed packages

pip install pymongo
pip install pymongo[srv]
pip install python-dotenv OR python3 -m pip install python-dotenv
pip install datetime
pip install pprint

# Project heirachy explained.

1) The code starts off by installing the dependencies needed.
2) It then loads in and integrates pyMongo.
3) Lists all database names.
4) Stores variable links for database.
5) Create and access the database and the collection.
6) (In Development) Validation for database
7) (Automatically) Enter a new user with the required information.

# How to access the database

Due to security concerns, I have created a separate document on how to access the database.
This document will be sent to those individuals who have clearance to access the database and it's contents.
