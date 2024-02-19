#!/usr/bin/env python
# coding: utf-8

# # **Homework**: Data Loading Workshop

# # 1. Use a generator
#
# Remember the concept of generator? Let's practice using them to futher our understanding of how they work.
#
# Let's define a generator and then run it as practice.
#
# **Answer the following questions:**
#
# - **Question 1: What is the sum of the outputs of the generator for limit = 5?**
# - **Question 2: What is the 13th number yielded**
#
# I suggest practicing these questions without GPT as the purpose is to further your learning.

# In[1]:


def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1


# Example usage:
limit = 5
generator = square_root_generator(limit)

for sqrt_value in generator:
    print(sqrt_value)

# ## Question 1: What is the sum of the outputs of the generator for limit = 5?
#
# - 10.234
# - 7.892
# - <font color='red'>**8.382**</font>
# - 9.123

# In[2]:


generator_with_limit_5 = square_root_generator(limit=5)

# This does not generate items on the fly but parses the generator expression to a list, which is not suitable for large datasets but gets the job done for this question
sum(list(generator_with_limit_5))  # Answer is 8.38

# ## Question 2: What is the 13th number yielded by the generator?
#
# - 4.236
# - <font color='red'>**3.605**</font>
# - 2.345
# - 5.678

# In[3]:


generator_with_limit_13 = square_root_generator(limit=13)

# This does not generate items on the fly but parses the generator expression to a list, which is not suitable for large datasets but gets the job done for this question
list(generator_with_limit_13)[-1]


#

# # 2. Append a generator to a table with existing data
#
#
# Below you have 2 generators. You will be tasked to load them to duckdb and answer some questions from the data
#
# 1. Load the first generator and calculate the sum of ages of all people. Make sure to only load it once.
# 2. Append the second generator to the same table as the first.
# 3. **After correctly appending the data, calculate the sum of all ages of people.**
#
#
#

# In[7]:


def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}


for person in people_1():
    print(person)


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
    print(person)

# ## Question 3. Append the 2 generators. After correctly appending the data, calculate the sum of all ages of people.
# - <font color='red'>**353**</font>
# - 365
# - 378
# - 390

# In[14]:


import dlt
import duckdb

people_pipeline = dlt.pipeline(destination='duckdb', dataset_name='gen_people')
info = people_pipeline.run(people_1(), table_name='people', write_disposition='replace')
print(info)

conn = duckdb.connect(f"{people_pipeline.pipeline_name}.duckdb")

print("\nSum of ages:")
sum_ages = conn.sql("SELECT SUM(Age) FROM gen_people.people").df()
display(sum_ages)

# In[15]:


info_2 = people_pipeline.run(people_2(), table_name='people', write_disposition='append')
print(info_2)

print("\nSum of ages:")
sum_ages = conn.sql("SELECT SUM(Age) FROM gen_people.people").df()
display(sum_ages)  # Age Sum is equal to 353 when appending the data

#

# # 3. Merge a generator
#
# Re-use the generators from Exercise 2.
#
# A table's primary key needs to be created from the start, so load your data to a new table with primary key ID.
#
# Load your first generator first, and then load the second one with merge. Since they have overlapping IDs, some of the records from the first load should be replaced by the ones from the second load.
#
# After loading, you should have a total of 8 records, and ID 3 should have age 33.
#
# Question: **Calculate the sum of ages of all the people loaded as described above.**
#

# # Solution: First make sure that the following modules are installed:

# In[ ]:


# Install the dependencies
get_ipython().run_line_magic('%capture', '')
get_ipython().system('pip install dlt[duckdb]')

# ## Question 4: Merge the 2 generators using the ID column. Calculate the sum of ages of all the people loaded as described above.
#
# - 215
# - <font color='red'>**266**</font>
# - 241
# - 258

# In[20]:


info = people_pipeline.run(people_1(), table_name='merged_people', write_disposition='replace', primary_key='ID')
print(info)

info_2 = people_pipeline.run(people_2(), table_name="merged_people", write_disposition="merge", primary_key='ID')
print(info_2)

print("\nTable:")
table = conn.sql("SELECT * FROM gen_people.merged_people").df()
display(table)

print("\nSum of ages:")
sum_ages = conn.sql("SELECT SUM(Age) FROM gen_people.merged_people").df()
display(sum_ages)  ## Age sum when merging data is equal to 266

# Questions? difficulties? We are here to help.
# - DTC data engineering course channel: https://datatalks-club.slack.com/archives/C01FABYF2RG
# - dlt's DTC cohort channel: https://dlthub-community.slack.com/archives/C06GAEX2VNX
