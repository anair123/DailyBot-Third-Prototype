#!/usr/bin/env python
# coding: utf-8

# In[43]:


class User:
    def __init__(self, first_name, last_name, language):
        self.first_name = first_name
        self.last_name = last_name
        self.language = language
        
    
    
    def introduce_self(self):
        print('My name is ',self.name)
        
    def show_language(self):
        print('My language is ',self.language)

        
    def set_to_Spanish(self):
        self.language = "Spanish"
        
    def set_to_English(self):
        self.language = "English"


# In[44]:


#class DailyReport:
#    def __init__(self):


# In[45]:


#class Appointment:
#    def __init__(self, member, day, time):
#        self.member = member # a list of members
#        self.day = day # datetime variable
#        self.time = time # datetime variable
        
        


# In[46]:


aashish = User("Aashish", "Nair", "English")


# In[ ]:




