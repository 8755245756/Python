# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 06:56:16 2021

@author: vivek
"""
#credited:
#vivek.choudhary
import os
import glob
import pandas as pd
#set working directory
a=os.chdir("C:\\Users\\Administrator\\Desktop\\ip addr\\v\\")
#find all csv files in the folder
#use glob pattern matching -> extension = 'csv'
#save result in list -> all_filenames
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#print(all_filenames)

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
