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
    print("Data added. Re-run file to analyze this data. Exiting...")

else:
    # Let the user select the model on dataset(s) of choice:
    is_looped, model = initiator(sample_dictionary)
    try:
        if is_looped:
            for model_params in model:
                print(model_params)

                runner(*model_params)
        else:
            runner(*model)

    except Exception as err:
        print(f'An error has occured: {err}')
        print("Model analysis failed. Exiting...")

