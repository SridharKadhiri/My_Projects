#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data1 = pd.read_csv(r"C:\Users\94407\Downloads\customer_details.csv")
data2 =pd.read_csv(r"C:\Users\94407\Downloads\customer_policy_details.csv")


# In[3]:


data1.columns= ["customer_id" ,
           "Gender","age",
           "driving licence present",
           "region code",
           "previously insured",
           "vehicle age",
           "vehicle damage"]
data2.columns = ["customer_id",
                 "annual premium (in Rs)",
                 "sales channel code",
                 "vintage" ,
                 "response" ]


# ### --------------------------------------------------------------------------------------------------------------------------------------------------------
# ### 2. Checking and Cleaning Data Quality:
# 
# i. Null values
# 
# Generate a summary of count of all the null values column wise
# 
# Drop Null values for customer_id because central tendencies for id’s is not feasible.
# 
# Replace all null values for numeric columns by mean. 
# 
# Replace all null values for Categorical value by mode.

# In[4]:


df1 = pd.DataFrame(data = data1)
df2 = pd.DataFrame(data = data2)

df1.customer_id.isnull().sum()


# In[5]:


df1.describe()
# Generate a summary of count of all the null values column wise


# In[6]:


df2.describe()


# In[34]:


df1.head()


# In[36]:


print(df1.shape)
print(df2.shape)


# In[7]:


# df1.describe()
# df1.customer_id.isnull().sum()


df1.dropna(subset=["customer_id"],inplace = True)


# In[8]:


df1.isnull().sum()
# Drop Null values for customer_id because central tendencies for id’s is not feasible.


# In[9]:


df1.age.fillna(df1.age.mean(),inplace = True)
df1["driving licence present"].fillna(df1["driving licence present"].mean(),inplace = True)
df1["region code"].fillna(df1["region code"].mean(),inplace = True)
df1["previously insured"].fillna(df1["previously insured"].mean(),inplace = True)
df1.isnull().sum()
# Replace all null values for numeric columns by mean.


# In[10]:


df1["Gender"].fillna(df1["Gender"].mode()[0],inplace = True)
df1["vehicle age"].fillna(df1["vehicle age"].mode()[0],inplace = True)
df1["vehicle damage"].fillna(df1["vehicle damage"].mode()[0],inplace = True)
df1.isnull().sum()

## customers_details table is cleaned (numeric values are filled with their column averages and cotegorial 
## columns null values are filled with their mode values)


# In[11]:


#  Lets do the same with the customer policy details table also
print("The null values in customer policy table : \n",df2.isnull().sum())
# Drop Null values for customer_id because central tendencies for id’s is not feasible.
df2.dropna(subset=["customer_id"],inplace = True)
print("The null values in customer policy table : \n",df2.isnull().sum())


# In[12]:


# Replace all null values for numeric columns by mean.

df2["annual premium (in Rs)"].fillna(df2["annual premium (in Rs)"].mean(),inplace = True)


# In[13]:


df2.head()
print("The null values in customer policy table : \n",df2.isnull().sum())


# In[14]:


df2["sales channel code"].value_counts().count() # sales channel code column has 155 values == > categorial
df2["vintage"].value_counts().count() # vintage column has 290 values == > categorial
df2["response"].value_counts().count() # vintage column has 2 values == > categorial
#  So we replace the null values with the mode of the column
print("The null values in customer policy table : \n",df2.isnull().sum())


# In[15]:


df2["sales channel code"].fillna(df2["sales channel code"].mode()[0],inplace = True)
df2["vintage"].fillna(df2["vintage"].mode()[0],inplace = True)
df2["response"].fillna(df2["response"].mode()[0],inplace = True)
print("The null values in customer policy table : \n",df2.isnull().sum())


# Cleaning the data from both the tables has finished

# In[ ]:





# ii. Outliers
# 
# Generate a summary of count of all the outliers column wise
# Replace all outlier values for numeric columns by mean. 
# (Hint1: for outlier treatment use IQR method as follows:
# 
# For example: for a column X calculate Q1 = 25th percentile and Q3 = 75th percentile then IQR = Q3 – Q1 ) then to check outlier, anything lower than a Q1 – 1.5IQR or greater than Q3 + 1.5 IQR would be an outlier
# 
# Hint2: For getting percentile value, explore pd.describe() function)

# In[16]:


df1.describe()


# In[17]:


# q1_age,q3_age = np.percentile(df1.age,[25,75])
# print(q1_age,q3_age)
# q1_dlp ,q3_dlp = np.percentile(df1["driving licence present"],[25,75])
# # print(q1_dlp,q2_dlp)


# In[18]:


# iqr = q3_age -q1_age
# lower_iqr_range = q1_age -(1.5 * iqr)
# higher_iqr_range = q3_age +(1.5 * iqr)
# print(lower_iqr_range ,higher_iqr_range)# There are no -ve age in the age column


# In[19]:


# df1[df1.age > higher_iqr_range].age.sum() # there are 0 outliers in the age column


# In[20]:


def iqr_range(col):
    q1,q3 = np.percentile(col,[25,75]) 
#     print(q1,q3)
    iqr = q3-q1
    low_iqr_lvl = q1 -(1.5*iqr)
    high_iqr_lvl = q3 + (1.5*iqr)   
#     print("Higher IQR Range : " ,high_iqr_lvl )
#     print("Lower IQR Range : " ,low_iqr_lvl )
    return [low_iqr_lvl,high_iqr_lvl]
    
    

iqr_range(df1.age)
print("No. Outliers greater then in age column :\t",df1[df1["age"] > iqr_range(df1.age)[1] ].age.sum())
print("No. Outliers lesser then in age column :\t",df1[df1["age"] < iqr_range(df1.age)[0] ].age.sum())
# There are 0 outliers in Age column


# In[21]:


print(df1["vehicle age"].value_counts())
print(df1["driving licence present"].value_counts())
# I didnot implement iqr on other columns because allother columns are categorial type 


# lets find the number of outliers in the policy details table

# In[22]:


df2.describe()


# In[23]:


iqr_range(df2["annual premium (in Rs)"])


# In[24]:


print("No. Outliers greater then in annual premium (in Rs) column :\t",df2[df2["annual premium (in Rs)"] > iqr_range(df2["annual premium (in Rs)"])[1] ]["annual premium (in Rs)"].count())
print("No. Outliers lesser  then in annual premium (in Rs) column :\t",df2[df2["annual premium (in Rs)"] < iqr_range(df2["annual premium (in Rs)"])[0] ]["annual premium (in Rs)"].count())
# There are 0 outliers in Age column


# ### There are zero outliers in the customer detail (age column)
# ### but we get 10332 values in the policy details (annual premium (in Rs) column) 

# ### --------------------------------------------------------------------------------------------------------------------------------------------------------
# ### 3. Create a Master table for future use. Join the customer table and customer_policy table to get a master table using customer_id in both tables.
# 
# (Hint: use pd.merge() function)

# In[25]:


df1.head()


# In[26]:


df2.head()


# In[27]:


m_table = pd.merge(df1,df2,on= "customer_id")
m_table.head()


# In[ ]:





# In[ ]:





# ### --------------------------------------------------------------------------------------------------------------------------------------------------------
# ### 4. Company needs some important information from the master table to make decisions for future growth.They needs following information:
# 
#  i. Gender wise average annual premium
# 
# ii. Age wise average annual premium
# 
# iii. Is your data balanced between the genders?
# 
#           (Hint: Data is balanced if number of counts in each group is approximately same)
# 
# iv. Vehicle age wise average annual premium.

# In[28]:


# i. Gender wise average annual premium
m_table.groupby(by = ["Gender"])["annual premium (in Rs)"].mean()


# In[29]:


# ii. Age wise average annual premium
m_table.groupby(by = ["age"])["annual premium (in Rs)"].mean()


# In[30]:


# iii. Is your data balanced between the genders?
m_table.groupby(by = ["Gender"]).count()["customer_id"]

#  No The data is not balanced between the genders


# In[31]:


m_table.head()


# In[32]:


# iv. Vehicle age wise average annual premium.
m_table.groupby(by = "vehicle age")["annual premium (in Rs)"].mean()


# ### --------------------------------------------------------------------------------------------------------------------------------------------------------
# ### 5. Is there any relation between Person Age and annual premium?
# 
# Hint: use correlation function (Correlation describes the relationship between two variables). 
# 
# Correlation coefficient < -0.5           - Strong negative relationship
# 
# Correlation coefficient > 0.5            -  Strong positive relationship
# 
# 0.5 < Correlation coefficient < 0.5   - There is no relationship. 

# In[33]:


corr = m_table["age"].corr(m_table["annual premium (in Rs)"])
print(corr)


# Correlation coefficient  = 0.067715
# 
# #### correlation coefficient is between  -0.5 and 0.5 ==> No Relationship
# 
# Which is less than 0.5

# In[ ]:




