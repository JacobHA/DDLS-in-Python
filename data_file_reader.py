# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:06:52 2020

@author: Jacob
"""

# This script will be used to write new data into the sample_data file in this directory


def FileReader():
    # Open a file
    fo = open("sample_data.txt", "r") # rw+ necc to add data
    lines = fo.readlines()
    
    
    beginning_of_samples, end_of_samples = [],[]
    for i in range(len(lines)):
        if '===' in lines[i]:
            beginning_of_samples.append(i)
        if '...' in lines[i]:
            end_of_samples.append(i)
            
    if len(beginning_of_samples) != len(end_of_samples):
        print('Data logging error. Check sample_data.txt for errors...')
    
    
    # We push the text file into a dictionary based on delimiters ... and ===
    sample_dictionary = {}
    
    new=[]
    for i in range(len(beginning_of_samples)):
        new.append([beginning_of_samples[i], end_of_samples[i]])
    
    for start_end in new:
        saved_array = []
        name = lines[start_end[0]+1:start_end[0]+2][0]
        name = name.replace('\n', '')
        sample_dictionary[name] = []
        for line in lines[start_end[0]+2:start_end[1]]: # +2 to skip naming line, turn this into dict later
            saved_array = line
            saved_array = [line.replace('\n','') for i in saved_array]
            saved_array = saved_array[0].split(',')
            saved_array = [saved_array[0]]+ [eval(saved_array[i]) for i in range(1,len(saved_array))]
            
            sample_dictionary[name] += [saved_array]
    
    
    fo.close()
    return sample_dictionary