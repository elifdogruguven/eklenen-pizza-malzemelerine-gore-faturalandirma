#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("Welcome to Elif Pizza Deliveries!")
size = input("Which size pizza would you want? (S, M, or L) ")
sauce_preference = input("Would you hot sauce or tomato sauce? (H or T) ")
add_pepperoni = input("Would you want pepperoni? (Y or N) ")
extra_cheese = input("Would you want extra cheese? (Y or N) ")

bill = 0

if size == "S":
    bill = 20
    if sauce_preference == "H":
        bill += 1
    
    if add_pepperoni == "Y":
        bill += 1
    
    if extra_cheese == "Y":
        bill += 2
elif size == "M":
    bill = 25
    if sauce_preference == "H":
        bill += 1
        
    if add_pepperoni == "Y":
        bill += 1
    
    if extra_cheese == "Y":
        bill += 2
elif size == "L":
    bill = 30
    if sauce_preference == "H":
        bill += 1
        
    if add_pepperoni == "Y":
        bill += 2
    
    if extra_cheese == "Y":
        bill += 3

print("Your final bill is:",bill,"$")


# In[ ]:




