#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1.Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. Finally print the list of the Employee objects.

# In[2]:


import json
Employee = {"Employee Details":[
    
    {"name" :"Aditya","DOB" :"28/06/2000","Height" :"5.8 ft","city":"hyderabad","state":"telangana"},
    {"name" :"Alex","DOB" :"08/06/1998","Height" :"6.0 ft","city":"Albany Park","state":"chicago"},
    {"name" :"Bhavs","DOB" :"24/06/2000","Height" :"5.3 ft","city":"Kansas City","state":"missouri"},
    {"name" :"Madhu","DOB" :"18/09/2000","Height" :"5.4 ft","city":"khammam","state":"telangana"},
    {"name" :"prag","DOB" :"04/04/1999","Height" :"5.0 ft","city":"hyderabad","state":"telangana"},
    ]}

with open("employee.json","w") as f:
    json.dump(Employee,f,indent=3)
    
print("Data stored Successfully") 

with open("employee.json","r") as f:
    x=json.load(f)
x


# 

# 2.Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

# In[3]:


import json
states_capitals={"Telangana":"Hyderabad","Punjab":"Chandigarh","goa":"Panaji","uttar pradesh":"Lucknow","west bengal":"Kolkata","Sikkim":"Gangtok","Rajasthan":"Jaipur"}

with open("State_capitals.json","w") as f:
    json.dump(states_capitals,f,indent=3)
print("JSON FILE SUCCESSFULL.") 


# # Assignment 2

# 1.Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:
# 
# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least        two methods of its own.
# 
# 🔴 d. Create objects and implement the above functionalities.

# In[5]:


class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color
        
    def description(self):
        print("Dog name is:" ,self.name)
        print("Dog age is:",self.age)
        
    def get_info(self):
        print("Dog coat_color is:",self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self,name,age,coat_color,energy_level,favourite_food):
        super().__init__(name,age,coat_color)
        self.energy_level = energy_level
        self.favourite_food = favourite_food
        
    def energy(self):
        print("Dog energy level is:", self.energy_level)
        
    def food(self):
        print("Dog favourite food is:", self. favourite_food)

class Bulldog(Dog): 
    def __init__(self,name,age,coat_color,fav_activity,lazy_level):
        super().__init__(name,age,coat_color)
        self.fav_activity = fav_activity
        self.lazy_level = lazy_level
        
    def activity(self):
        print("Dog fav activity is:", self.fav_activity)
        
    def laziness(self):
        print("Dog lazy level is:", self.lazy_level)
        
D1 = JackRussellTerrier("Rocket",4,"white & tan","cooked chicken","Shell")
D1.description()
D1.get_info()
D1.energy()
D1.food()

print("---------------------------------------------------------------")

D2 = Bulldog("Rockcy",3,"Piebald","swimming","Low")
D2.description()
D2.get_info()
D2.activity()
D2.laziness()       


# In[ ]:





# In[ ]:




