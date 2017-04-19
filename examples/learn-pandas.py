# ==============================================================================
# title       	: learn-pandas
# description 	:
# author      	: Julien Reynier
# date        	: 02.04.17
# version     	:
# IDE         	: PyCharm Community Edition
# ==============================================================================
# http://pandas.pydata.org/pandas-docs/stable/10min.html
# http://pandas.pydata.org/pandas-docs/stable/tutorials.html

# SCRIPTS FROM 10 MINUTES TO PANDAS

# IMPORTS:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CREATE OBJECT
s = pd.Series([1, 2, 3, np.nan, 6, 8])
s

dates = pd.date_range('20170101', periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

df2
df2.dtypes

# VIEW DATA INSIDE
df.head()  # default n is 5
df.tail(3)

df.index  # we defined the index at df creation in that case

df.describe()  # some summary statistics about the data frame


# SIMPLE OPERATIONS
df.T  # dataframe transpose

df.sort_index(axis=1, ascending=False)

df.sort_values(by='B')

# SELECTION INDEXING SLICING OPERATIONS
# I quote:
# "we recommend the optimized pandas data access methods, .at, .iat, .loc,
# .iloc and .ix."
# SIMPLE SELECTION
df['A']

df[2::-1]
df['20170103':'20170101':-1]

# SELECTION BY LABEL
df.loc[[dates[0], dates[4], dates[1]]]

df.loc[:,['A','B']]

