# Developer: Raj Singh Bhamra @ 01/08/22 2:45PM
# This script has been developed to act as a data storage system for the 'DARK CITY' AI chatbot using the MongoDB database storage system.
# This script currently links up with no local files (at creation). It will have external file impact when it is integrated into the chatbot.
# Libraries used: os, pprint, pymongo, MongoClient, dotenv, datetime
# Version: 7.0


import os
import pprint
from pymongo import MongoClient
import datetime
from dotenv import load_dotenv, find_dotenv


# This code block integrates pyMongo into this script.
# This links to the whole script as it enables the database strucutre to be used, aswell as data implementation and other features.
# Key word explanation:
         # MONGODB_PWD - This is the variable name that stores the database password. It can be found in the .env file
         # MongoClient - The main client system which MongoDB bases itself off around.
         # connection_string - The exact url needed to connect this script to the desired database.
# We are using it for 2 reasons. 1) To integrate the database structure for code usage. 2) For security, I have taken the security pin out of the connection string and stored (and will pass it in) through a
   # .env file. This means un-authorised users wil not be able to access the data / the database if they somehow do manage to get the connection string.


load_dotenv(find_dotenv())
db_password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://DarkCityUserOne:{db_password}@dark-city-ai-one.z9ykv.mongodb.net/test"
client = MongoClient(connection_string)


# This code block allows us to view existing information about our existing databases.
# Key word explanation:
         # dbs - A variable name for the command which lists all database names. 
# We are using it to check if the required database has been created.
# This is not necessary for actial data writing / reading. It can be used to show updates to number of databases, aswell as individual information if needed.


print()
print("Hello! Here are all the currently existing database collections: ") 
dbs = client.list_database_names()
print(dbs)


# This code block allows us to store variable links here.
# Key word explanation: NONE REQUIRED.
# We are using this to pass in outputs of the AI chatbot to variables which are stored in this database script.


first_name_input = "user"
sur_name_input = "userSurname"
wallet_address_input = 1234567890
password_input = "DARKCITY"
date_created_input = datetime.datetime.utcnow()
darkcity_status_input = "Sol Leader"

ie_domain_input = 5
co_domain_input = 6
tf_domain_input = 3
jp_domain_input = 8
ag_domain_input = 1
ho_domain_input = 3 

coins_preferance_input = 12
cups_preferenace_input = 12
wands_preferance_input = 12
swords_preferance_input = 12

times_loggedin_input = 0
spent_onsite_input = 0


# This code block allows us to access the database.
# This block links up to the whole script as it creates the database which will be used.
# Key word explanation: 
         # collections - Listing all the collections inside the database  
# We are using this as it creates the relevant parts of the database. It creates the "client" datavbase, aswell as the indiviual (data) collection we are currently storing data in.


databaseAccess = client["darkCityStorage"] #Name of the collection (database) you are accessing
collections = databaseAccess.list_collection_names 
print()
print("This is where we view our database information: ")
print(collections)


# This is a non-working attempt at a validation scheme.
# Currently, ths has no impact on the script.
# Key word explanation: NONE REQUIRED.
# If, in the future this works, this will affect the script by validating the data coming into the database, to make sure it is the right form, standard etc.
   # For now, validation can be done in Iniaki's AI code, it will give the same effect (theoretically).


AI_Storage_Validator = {
   "$jsonSchema": {
      "bsonType": "object",
      "required": ["First Name", "Wallet Address", "IE Domain", "CO Domain"],
      "properties": {
         "First Name": {
            "bsonType": "string",
            "description": "Must be a string and is required"
         }
      }
   }
}


# This code block allows us to automatically enter a new user with the required information.
# Key word explanation:
         # inserted_id - Displays the (computer generated) ID number of the user that has been added into the database.
         # insert_new_user() - A function called right at the end that allows the data to be stored and the method to end.
# We are using this so data can be stored into the database. This works by passing the variables (see above) and the respective data into this so it can be stored into the database collection.

def insert_new_user():
   collection = databaseAccess.darkCityArtificialIntelligenceStorage  #Get access from collection to database you are using
   new_user_document = {

        "First Name": first_name_input,
        "Surname": sur_name_input,
        "Wallet Address": wallet_address_input,
        "Password": password_input,
        "Date Account Created": date_created_input,
        "DARK CITY Status": darkcity_status_input,

        "IE Domain": ie_domain_input,
        "CO Domain": co_domain_input,
        "TF Domain": tf_domain_input,
        "JP Domain": jp_domain_input,
        "AG Domain": ag_domain_input,
        "HO Domain": ho_domain_input,

        "Coins Preferance": coins_preferance_input,
        "Cups Preferance": cups_preferenace_input,
        "Wands Preferance": wands_preferance_input,
        "Swords Preferance": swords_preferance_input,

        "Times Logged In": times_loggedin_input,
        "Time Spent On Site": spent_onsite_input,
   }

   inserted_id = collection.insert_one(new_user_document).inserted_id
   print()
   print(inserted_id)
insert_new_user()



