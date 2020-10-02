#!/usr/bin/env python
# coding: utf-8

# ### NumPy
# 
# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
# 
# - a powerful N-dimensional array object
# - sophisticated (broadcasting) functions
# - useful linear algebra, Fourier transform, and random number capabilities
# 
# Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.
# 
# NumPy is licensed under the BSD license, enabling reuse with few restrictions.

# ## Installation Guide
# 
# **It is strongly recommended that you install Python using the Anaconda distribution to make sure all underlying dependencies work with conda install. If you have already installed Anaconda, install NumPy by opening your terminal(for MAC Users) or ANACONDA Command Prompt(for Windows Users) and type the following command - **
#     
#     conda install numpy
#     
# **If you are unable to install ANACONDA due to restrictions, please refer to [Numpy's official documentation on installation steps.](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)**

# ## Using NumPy Package
# 
# Once NumPy Package is installed successfully, you can import it to the current Python session using the following code:

# ### Part 1 : Introduction to Numpy and its functions

# In[2]:


import numpy as np


# In[3]:


simple_list = [1,2,3]


# In[4]:


np.array(simple_list)


# In[5]:


list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]


# In[6]:


np.array(list_of_lists)


# In[7]:


# min is inclusive and max is not included
np.arange(0,10)


# In[8]:


# creating an arraay with a count of 5. However it will start with min and exclude max value 
np.arange(0,21,5)


# In[7]:


np.arange(0, 100, 5)


# In[11]:


# Uni dimensional array
ed = np.zeros(100)
ed


# In[12]:


# Two dimensional array
np.ones((4,5))


# In[13]:


np.linspace(0,20,10)


# In[14]:


np.arange(0, 20, 10)


# In[38]:


a = np.eye(5)
a


# In[18]:


# random number between 0 to 1 - uniform distribution
np.random.rand(3,2)


# In[41]:


# set of random numbers - normal distribution
a = np.random.randn(2,3)
a


# In[3]:


# 10 random numbers between min and max values
np.random.randint(5,20,10)


# In[5]:


np.random.randint(3,10)


# In[23]:


sample_array = np.arange(30)
sample_array


# In[79]:


np.random.randn(30).reshape(3,10).argmin()


# In[26]:


rand_array = np.random.randint(0,100,20)
rand_array


# In[27]:


sample_array.reshape(5,6)


# In[29]:


# Returns the location of minimum value
rand_array.argmin()


# In[33]:


# Returns the location of maximum value
rand_array.argmax()


# In[30]:


sample_array.shape


# In[34]:


# Row vector 
sample_array.reshape(1,30)


# In[35]:


# Colu
sample_array.reshape(30,1)


# In[36]:


sample_array.dtype


# In[39]:


a.T


# In[32]:





# ### Part 2 : How to select group of objects from a particular array

# In[42]:


a.T


# In[43]:


sample_array = np.arange(10,21)


# In[45]:


sample_array


# In[46]:


sample_array[8]


# In[49]:


sample_array[2:5]


# In[50]:


sample_array[[2,5]]


# In[51]:


# changing the value in the array
sample_array[1:2] = 100


# In[52]:


sample_array


# In[53]:


sample_array = np.arange(10,21)


# In[46]:


sample_array[0:7]


# In[54]:


sample_array = np.arange(10,21)
                        
sample_array


# Broadcasting and creating views in python

# In[56]:


subset_sample_array = sample_array[0:7]

subset_sample_array


# In[57]:


subset_sample_array[:]=1001


# In[58]:


subset_sample_array


# In[59]:


sample_array


# In[60]:


# For creating a duplicate copy, explicitly use the copy command
copy_sample_array = sample_array.copy()


# In[61]:


copy_sample_array


# In[62]:


copy_sample_array[:]=10
copy_sample_array


# In[63]:


sample_array


# ### Part 3 : Indexing a Matrix - Two dimensional arrays

# In[66]:


sample_matrix = np.array(([50,20,1,23], [24,23,21,32], [76,54,32,12], [98,6,4,3]))


# In[67]:


sample_matrix


# In[68]:


sample_matrix[0][3]


# In[69]:


sample_matrix[0,3]


# In[70]:


sample_matrix[3,:]


# In[18]:


sample_matrix[3]


# In[71]:


sample_matrix = np.array(([50,20,1,23,34], [24,23,21,32,34], [76,54,32,12,98], [98,6,4,3,67], [12,23,34,56,67]))


# In[72]:


sample_matrix


# In[73]:


sample_matrix[:,(1,3)]


# In[74]:


sample_matrix[:,(3,1)]


# ### Part 4: Selection techniques

# In[23]:


sample_array=np.arange(1,31)


# In[24]:


sample_array


# In[26]:


bool = sample_array < 10


# In[27]:


sample_array[bool]


# In[28]:


sample_array[sample_array <10]


# In[31]:


a=11


# In[32]:


sample_array[sample_array < a]


# In[33]:


sample_array + sample_array


# In[36]:


sample_array / sample_array


# In[37]:


10/sample_array


# In[38]:


sample_array + 1


# In[57]:


np.var(sample_array)


# In[52]:


array = np.random.randn(6,6)


# In[53]:


array


# In[58]:


np.std(array)


# In[59]:


np.mean(array)


# In[60]:


sports = np.array(['golf', 'cric', 'fball', 'cric', 'Cric', 'fooseball'])

np.unique(sports)


# ### Part 5: Input, Output options and Saving files

# In[63]:


sample_array


# In[65]:


simple_array = np.arange(0,20)


# In[66]:


simple_array


# In[67]:


np.save('sample_array', sample_array)


# In[68]:


np.savez('2_arrays.npz', a=sample_array, b=simple_array)


# In[69]:


np.load('sample_array.npy')


# In[70]:


archive = np.load('2_arrays.npz')


# In[72]:


archive['b']


# In[73]:


np.savetxt('text_file.txt', sample_array,delimiter=',')


# In[75]:


np.loadtxt('text_file.txt', delimiter=',')


# In[ ]:




