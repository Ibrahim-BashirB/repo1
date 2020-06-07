#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:06:23 2020

@author: ibrahimbashir
"""


import glassdoor_scraper as gs
import pandas as pd

path = "/Users/ibrahimbashir/Documents/ds_salary_proj/chromedriver"

#df = gs.get_jobs(keyword, num_jobs, verbose, path, slp_time)
df = gs.get_jobs('data scientist', 80, False, path, 60)
df.to_csv('glassdoor_data.csv')
