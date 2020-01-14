# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:09:39 2020

@author: Jacob
"""

def _catchable_input(input_type):
    try:
        x=input(f"Now enter your data in the same format below.\n({input_type}):\t")
        if input_type != "D_tr":
            return x
        else:
            return x + " * (1e-9)**2/(1e-6)"

    except KeyboardInterrupt:
        print("Exiting...")
        
        

def AddMoreData():
    data_array = []
    dataset_string=""
    stock_name = input("Please type the name of the new dataset and press Enter.\n(e.g. stocksAndrew):\n")
    
    print("""The following shows an example of how the dataset must be saved.
          \n(title)\t(temp.[K])\t(D_translation [nm^2/us])\t(D_rotational [10^-4/us])
          \nno.5\t 298.15\t\t 3.07 \t\t 111\n\n""")
    
    exit_word=""
    while exit_word != "stop":
        try:
            for keyword in ["title", "temp.", "D_tr", "D_rot"]:
                dataset_string += _catchable_input(keyword) + ", "
            exit_word = input("Type \"stop\" if you have reached the end of your dataset. Otherwise, press any key.\n")
        except KeyboardInterrupt:
            print("broke out of loop")
            break
        
        data_array.append(dataset_string[:-2])
        dataset_string = ""
    return stock_name, data_array

        
        
def WriteToFile(name,data_array):
    fo = open("sample_data.txt", "a+") # a+ necc to append data
    fo.write(f"\n===\n{name}\n")
    for dataset_string in data_array:
        fo.write(f"{dataset_string}\n")
    fo.write('...\n')
    
def writer():
    WriteToFile(*AddMoreData())