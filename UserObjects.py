#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[21]:


class User:
    def __init__(self, name, timezone, is_enabled, language):
        self.name = name
        self.timezone = timezone
        self.is_enabled = is_enabled
        self.language = language
        
    
    
    def introduce_self(self):
        print('My name is ',self.name)
        
    def show_language(self):
        print('My language is ',self.language)
        
    def change_timezone(self, timezone):
        self.timezone = timezone
        print('Timezone changed to: ',)
        
    def disable(self):
        self.is_enabled = False
    
    def enable(self):
        self.is_enabled = True
        
    def change_to_Spanish(self):
        self.language = "Spanish"
        
    def English(self):
        self.language = "English"


# In[31]:


aashish = User("Aashish Nair", "EST", "True", "English")


# In[29]:


pickle_class = open('Aashish.pkl', 'wb')
pickle.dump(aashish, pickle_class)
pickle_class.close()


# In[30]:


pickle_in = open('Aashish.pkl', 'rb')
aashish = pickle.load(pickle_in)


# In[ ]:




