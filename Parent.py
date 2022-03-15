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
    # Proceed to add new data:
    writer()
    print("Data added. Re-run file to analyze. Exiting...")

else:
    # Let the user select the model on dataset(s) of choice:
    model = initiator(sample_dictionary)
    
    try:
        runner(*model)
    except:
        print("Model analysis failed. Exiting...")

