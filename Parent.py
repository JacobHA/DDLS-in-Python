# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:54:21 2020

@author: Jacob
"""

from data_file_writer import writer
from data_file_reader import FileReader
from Calculations import runner
from sample_initializer import initiator

sample_dictionary = FileReader()
newdata = input("If you would like to add a new dataset, type \"yes\" and press enter. Otherwise, press any other key.\n")
if newdata == 'yes':
    writer()
    print("Data added. Exiting...")
    #exit()
else:
    model = initiator(sample_dictionary)
    print(['model', 'Temperature [K]', 'D_tr [nm^2/us]', 'D_rot [10^-4 / us]'])
    for i in model:
        print(i)
        try:
            runner(*i)
        except TypeError:
            print("Failed to plot the figure, continuing.")
#    for i in model
    
