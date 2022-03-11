#!/usr/bin/env python
# coding: utf-8

# In[12]:


def count_str(str_in):
    up_count = 0
    low_count = 0
    space_count = 0
    for i in str_in:  
        if i.isupper():
            up_count += 1
        elif i.islower():
            low_count += 1
        elif i == " ":
            space_count += 1
        
        else:
            continue
    return up_count,low_count
up_count,low_count = count_str("Hello World")
print("(‘Uppercase:{} ".format(up_count)+"',"+"‘Lowercase:{}".format(low_count)+"')")


# In[ ]:




