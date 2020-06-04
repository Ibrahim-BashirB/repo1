#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:06:23 2020

@author: ibrahimbashir
"""


import glassdoor_scraper as gs
import pandas as pd

path = "/Users/ibrahimbashir/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)

