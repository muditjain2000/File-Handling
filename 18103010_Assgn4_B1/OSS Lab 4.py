#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np;
import matplotlib.pyplot as plt;


# In[35]:


X=np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.show()


# In[36]:


# Create a figure of size 8x6 inches, 80 dots per inch 
plt.figure(figsize=(8, 6), dpi=80)
# Create a new subplot from a grid of 1x1 
plt.subplot(1, 1, 1) 
# Plot cosine with a blue continuous line of width 1 (pixels) 
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-") 
# Plot sine with a green continuous line of width 1 (pixels) 
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-") 
# Set x limits 
plt.xlim(-4.0, 4.0) 
# Set x ticks 
plt.xticks(np.linspace(-4, 4, 9, endpoint=True)) 
# Set y limits 
plt.ylim(-1.0, 1.0) 
# Set y ticks 
plt.yticks(np.linspace(-1, 1, 5, endpoint=True)) 
# Save figure using 72 dots per inch 
plt.savefig("exercise_2.png", dpi=72) 


# In[37]:


plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine") 
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine") 
plt.legend(loc='upper left') 


# In[28]:


n = 256 
X = np.linspace(-np.pi, np.pi, n, endpoint=True) 
Y = np.sin(2 * X) 
plt.plot(X, Y + 1, color='blue', alpha=1.00) 
plt.plot(X, Y - 1, color='blue', alpha=1.00) 


# In[29]:


n = 1024 
X = np.random.normal(0,1,n) 
Y = np.random.normal(0,1,n) 
plt.scatter(X,Y) 


# In[30]:


n = 12 
X = np.arange(n) 
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) 
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white') 
plt.show() 
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) 
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white') 
plt.show()


# In[40]:


X = [-np.pi, -np.pi/4, -np.pi/2, 0, np.pi/4, np.pi/2, np.pi]
T = np.tan(X)
CT = 1 / np.tan(X)
S = 1 / np.cos(X)
CS = 1 / np.sin(X)

plt.plot(X, T, color="blue", linewidth=2.5, linestyle="-", label="tan")
plt.plot(X, CT, color="red", linewidth=2.5, linestyle="-", label="cot")
plt.plot(X, S, color="green", linewidth=2.5, linestyle="-", label="sec") 
plt.plot(X, CS, color="yellow", linewidth=2.5, linestyle="-", label="cosec") 
plt.legend(loc='upper left')


# In[ ]:




