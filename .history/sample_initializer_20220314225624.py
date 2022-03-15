# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:02:27 2019

@author: Jacob
"""
import numpy as np

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
            
        sampleNum = int(input(f'Enter the sample number : '))
        model = str(input('Enter the model (prolate, oblate, cylinder) to be used: '))
           
        try:
            sample = dictionary_of_samples[sampleName][sampleNum - 1]
        except KeyError:
            print("Incorrect name entered.")
            exit()
        
        
        name,T,D_tr,D_rot = sample
    
    
        return model, T, D_tr, D_rot
        
    if loop_or_not == '1':
        model = str(input('Enter the model (prolate, oblate, cylinder) to be used: '))

#        names_list, T_list, Dtr_list, Drot_list = np.transpose(dictionary_of_samples[sampleName])
#        T_list = [float(t) for t in T_list]
#        Dtr_list = [eval(d) for d in Dtr_list]
#        Drot_list = [eval(d) for d in Drot_list]
#        
        temp_dic = dictionary_of_samples[sampleName]
        for j in temp_dic:
            j[0] = model
            # replacement to fit the return scheme
#        model_list, T_list, Dtr_list, Drot_list = temp_dic
        return temp_dic # model_list, T_list, Dtr_list, Drot_list
        