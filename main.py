import os
import json

# 1. "Functions and constants":
settings_file_dir = "./files/" # set files location CONST
settings_file_name = "settings.json"

def ask_settings(saved_settings): #  Function: set user data in a dictionary for the json
  name = ""
  age = ""

  if "name" not in saved_settings:
    name = str(input("Hi, whay is your name?\n"))
  else:
    name = saved_settings.get("name")

  if "age" not in saved_settings:
    age = str(input("Hi, whay is your age?\n"))
  else:
    age = saved_settings.get("age")

  saved_settings = {"name":name, "age":age}

  return saved_settings 
#END Function

# 2. Is my seetings file ok?

if not (os.path.exists(settings_file_dir)): # Checking files folder
  os.mkdir(settings_file_dir) 
# END Checking files folder

if(os.path.exists(settings_file_dir + settings_file_name)): # Checking settings file
  with open(settings_file_dir + settings_file_name, 'r+', encoding="utf-8") as f:
    try:   # loading settings
      saved_settings = json.load(f)
    except: # if loading fails, ignore json and use an emty one
      print("error with file: " + settings_file_name + ". FILE RESETED!!")
      saved_settings = {}

  with open(settings_file_dir + settings_file_name, 'w', encoding="utf-8") as f:
    settings = ask_settings(saved_settings) # setting user data IF NOT OK
    json.dump(settings, f) # saving user data                        
# END Checking settings file

else: # Creating settings file since it doesn't exist
  with open(settings_file_dir + settings_file_name, 'w', encoding="utf-8") as f:
    saved_settings = {} # emty json
    settings = ask_settings(saved_settings) # setting user data
    json.dump(settings, f) # saving user data

# My settings file is ok!

# 3. Greeting to the User
print("Hey " + settings.get("name") + ". Welcome to the TO-DO program")

# 4. Checking the task file
# 5. main -> Showing the menu

# if if if if if if

# 6. say gooobye