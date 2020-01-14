# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:02:27 2019

@author: Jacob
"""


# D_rot are in units 1/us so 1e-4 * 1e6 puts it in 1e2 
# D_tr is in nm^2/us
#stocksPhil = [['no. 5', 298.15, 3.07* (1e-9)**2/(1e-6), 111],
#              ['no. 3', 298.15, 4.5 * (1e-9)**2/(1e-6), 487],
#              ['no. 7', 293.15, 3.55* (1e-9)**2/(1e-6), 272]] # [name, T [K]], D_tr, D_rot]
#
#stocksAndrew = [['Tsyn=40.5', 328.15, 1.232065* (1e-9)**2/(1e-6), 100.850],
#                ['Tsyn=44.0', 328.15, 1.70863 * (1e-9)**2/(1e-6), 441.838],
#                ['Tsyn=45.5', 328.15, 2.04668 * (1e-9)**2/(1e-6), 222.333],
#                ['Tsyn=48.0', 328.15, 2.77062 * (1e-9)**2/(1e-6), 150.889],
#                ['Tsyn=49.5', 328.15, 2.00009 * (1e-9)**2/(1e-6), 149.906],
#                ['Tsyn=51.5', 328.15, 2.40505 * (1e-9)**2/(1e-6), 173.33]]


def initiator(dictionary_of_samples):
    #dictionary_of_samples = FileReader()
    
    possible_names = dictionary_of_samples.keys()
    ex=""
    for name in possible_names:
        ex += name + "\n"
    print("The possible names are: \n" + ex)
    sampleName = str(input('Enter the sample name: '))
    sampleNum = int(input('Enter the sample number (0-5 or 0-2): '))
    model = str(input('Enter the model (prolate, oblate, cylinder) to be used: '))
    
    
    
    try:
        sample = dictionary_of_samples[sampleName][sampleNum]
    except KeyError:
        print("Incorrect name entered.")
        exit()
    
    #if sampleName == 'Andrew':
    #    try:
    #        sample = stocksAndrew[sampleNum]
    #    except IndexError:
    #        print('Index must be between 0 and ' + str(len(stocksAndrew)))
    #    except NameError:
    #        print('Incorrect inputs.')
    #if sampleName == 'Phil':
    #    try:
    #        sample = stocksPhil[sampleNum]
    #    except IndexError:
    #        print('Index must be between 0 and ' + str(len(stocksPhil)))
    #if sampleName == 'DrS':
    #    try:
    #        sample = stocksDrS[sampleNum]
    #    except IndexError:
    #        print('Index must be between 0 and ' + str(len(stocksDrS)))
    #else:
    #    print('Enter a valid sample name')    
    
    name,T,D_tr,D_rot = sample

    
    #whos_sample = ''
    #if sample in stocksPhil:
    #    whos_sample = 'Phil\'s'
    #if sample in stocksAndrew:
    #    whos_sample = 'Andrew\'s'
    #    
    #print(whos_sample + " sample: " + name)
    return model, T, D_tr, D_rot
    
