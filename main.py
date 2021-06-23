import os
import json
os.system("cls") #borrar consola

# ------------------------------------------------------

# 1. "Functions and constants":
files_dir = "./files/" # set files location CONST
settings_file = "settings.json"
tasks_file = "tasks.json"
backup_task_file = "task.txt"
saved_tasks = {}

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

def pending():
  pending_opt = ""
  while pending_opt != "0":
    print()
    print("\n-> 1. TO DO list\n") #print
    for task in saved_tasks:
      print(task + ". " + str(saved_tasks[task][0]) + ": " + str(saved_tasks[task][1]))
    print()
    print(settings.get("name") + "! Did you get it done? Anyways enter '0' when you finish here to go back to the  TO DO list menu")
    pending_opt = str(input())
    os.system("cls") #borrar consola
    if pending_opt in saved_tasks:
      tasking(pending_opt)

def tasking(task_id):
  tasking_opt = ""
  while tasking_opt != "0":
    print()
    print("\n-> " + task_id + ". " + str(saved_tasks[task_id][0]) + ": " + str(saved_tasks[task_id][1]) + "\n") #print
    print()
    print("Please enter the number of one task above or '0' to go back to principal menu")
    print("1. Complete")
    print("2. Delete")
    print("\n-> 0. Exit")
    tasking_opt = str(input())
    os.system("cls") #borrar consola
    if tasking_opt == "1":
      saved_tasks[task_id][1] = "done"
      tasking_opt = str(input("\n-> 0. Exit\n"))
    if tasking_opt == "2":
      del saved_tasks[task_id]
      tasking_opt = str(input("\n-> 0. Exit\n"))


# ------------------------------------------------------

# 2. Is my seetings file ok?

if not (os.path.exists(files_dir)): # Checking files folder
  os.mkdir(files_dir) 
# END Checking files folder

if(os.path.exists(files_dir + settings_file)): # Checking settings file
  with open(files_dir + settings_file, 'r+', encoding="utf-8") as f:
    try:   # loading settings
      saved_settings = json.load(f)
      # print(saved_settings)
    except: # if loading fails, ignore json and use an emty one
      print("error with file: " + settings_file + ". FILE RESETED!!")
      saved_settings = {}

  with open(files_dir + settings_file, 'w', encoding="utf-8") as f:
    settings = ask_settings(saved_settings) # setting user data IF NOT OK
    json.dump(settings, f) # saving user data                        
# END Checking settings file

else: # Creating settings file since it doesn't exist
  with open(files_dir + settings_file, 'w', encoding="utf-8") as f:
    saved_settings = {} # emty json
    settings = ask_settings(saved_settings) # setting user data
    json.dump(settings, f) # saving user data

# My settings file is ok!

# ------------------------------------------------------

# 3. Greeting to the User
print("\nHey " + settings.get("name") + ". Welcome to the TO-DO program")

# ------------------------------------------------------

# 4. Checking the task file

if(os.path.exists(files_dir + tasks_file)): # Checking tasks file
  with open(files_dir + tasks_file, 'r', encoding="utf-8") as f:
    # saved_tasks = json.load(f)
    # print(previous_task)
    try:   # loading tasks
      saved_tasks = json.load(f)
      # print(saved_tasks)
    except: # if loading fails, ignore json and use an emty one
      print("error with file: " + tasks_file + ". FILE RESETED!!. Check your previous task file in " + files_dir + backup_task_file)
      saved_tasks = {}
    previous_task = f.read()

  with open(files_dir + backup_task_file, 'w', encoding="utf-8") as f: #saving backup
    f.write(previous_task)

  with open(files_dir + tasks_file, 'w', encoding="utf-8") as f:
    json.dump(saved_tasks, f) # saving tasks file or emty json if loading fails

else: # Creating tasks file since it doesn't exist
  with open(files_dir + tasks_file, 'w', encoding="utf-8") as f:
    saved_tasks = {}
    json.dump(saved_tasks, f) # saving emty json
# END Checking tasks file

# ------------------------------------------------------

# 5. main -> Showing the main menu
general_opt = ""
while general_opt != "0":
  print()
  print("\nPlease enter the number from the options below:\n")
  print("1. TO DO list")
  print("2. DONE list")
  print("3. List all the tasks")
  print("\n-> 0. Exit")
  print()
  general_opt = str(input())
  if general_opt != "0":
    os.system("cls") #borrar consola
  if general_opt == "1":
    pending()

# if if if if if if

# ------------------------------------------------------

# 6. say gooobye

print("\nBye " + settings.get("name") + ". Doing things with you is always exciting ^.^\n")

# ------------------------------------------------------ FIN

#  {"Hacer la tarea de MinTic": "done", "Redactar la documentacion": "not done"}
# {"1": {"Hacer la tarea de MinTic": "done"}, "2": {"Redactar la documentacion": "not done"}}
# {"1": ["Hacer la tarea de MinTic", "done"], "2": ["Redactar la documentacion", "not done"]}