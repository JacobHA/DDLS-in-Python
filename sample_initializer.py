# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:02:27 2019

@author: Jacob
"""
import numpy as np

MODELS_ALLOWED = ['prolate','oblate', 'cylinder']

def initiator(dictionary_of_samples):
    #dictionary_of_samples = FileReader()
    
    possible_names = dictionary_of_samples.keys()
    print("The possible names are: \n")
    for name in possible_names:
       print(name)
    sampleName = str(input('Enter the desired sample name: '))
    
    loop_or_not = str(input('If you would like to loop over the dataset, enter \'1\'. Otherwise, you can perform a model on a single sample. To do this, you can type any other key.\n'))
    if loop_or_not != '1':
        
        print('Available samples are below.\n')
         #{[tuple([1,len(j)]) for j in FileReader().values()]}
        
        counter = 1
        for title in np.transpose(dictionary_of_samples[sampleName])[0]:
            print(f'Sample number {counter}: {title}')
            counter+=1
            
        sampleNum = int(input(f'Enter the sample number to analyze: '))
        model = str(input('Enter the model to be used: '))
        assert model in MODELS_ALLOWED, f'User entry \"{model}\" is not a valid model.\nPlease enter a valid model: {MODELS_ALLOWED}.'

        try:
            sample = dictionary_of_samples[sampleName][sampleNum - 1]
        except KeyError:
            print("Incorrect name entered.")
            exit()
        
        name,T,D_tr,D_rot = sample
    
        return False, [model, T, D_tr, D_rot]
        
    if loop_or_not == '1':
        model = str(input('Enter the model to be used: '))
        assert model in MODELS_ALLOWED, f'User entry \"{model}\" is not a valid model.\nPlease enter a valid model: {MODELS_ALLOWED}.'

        temp_dic = dictionary_of_samples[sampleName]
        for j in temp_dic:
            j[0] = model
            # replacement to fit the return scheme

        return True, temp_dic 
        