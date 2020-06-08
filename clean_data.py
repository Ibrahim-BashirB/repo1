#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 14:59:28 2020

@author: ibrahimbashir
"""


import pandas as pd

df = pd.read_csv('glassdoor_data.csv')
df


#salary parsing


salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2


#df.info()

#company name text only

#df['company text'] = df.apply(lambda x: x['Company Name'] if ['Rating'] < 0 else x['Company Name'][:-3], axis=1)
df['company text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)

df['Job_Location'] = df['Location'].apply(lambda x: x.split(',')[0])
#print(df.Job_Location.value_counts())

#state field
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#age of company

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)


#parsing of job desc (python)
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

# R studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

df = df.drop(['Unnamed: 0'], axis=1)


