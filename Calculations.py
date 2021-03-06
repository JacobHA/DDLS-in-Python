# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:31:36 2019

@author: Jacob
"""
import warnings

from geometric_functions_for_DDLS import GeneralDims, OptimizingFunction
import numpy as np
from scipy.optimize import fsolve
from statistics import mode
from statistics import StatisticsError
from modelGrapher import grapher

### SOLVER: 

warnings.filterwarnings("ignore")
print("Note: All warnings in python Calculation module are being suppressed.")
amtg = 300 # amount of starting guesses
digits = 6 # desired digits when solving

def Solver(modelname, T, D_tr, D_rot):
    zeros=[]
    if modelname == 'prolate':
        for val in np.linspace(1.000001, 80.9,amtg):
                zeros.append(fsolve(OptimizingFunction(modelname, T, D_tr, D_rot), val)[0])

    if modelname == 'oblate':
        for val in np.linspace(.000001,0.99999,amtg):
                zeros.append(fsolve(OptimizingFunction(modelname, T, D_tr, D_rot), val)[0])

    if modelname == 'cylinder':
        for val in np.linspace(0.01,9.9,amtg):
            zeros.append(fsolve(OptimizingFunction(modelname, T, D_tr, D_rot), val)[0])
    
    try:
        rho = mode([round(z,digits) for z in zeros])
        print("Aspect ratio: " + str(rho))
        print("Length: " + str(round(10**9 * GeneralDims(modelname,rho, T, D_tr, D_rot)[0])) + "nm")
        print("Width: " + str(round(10**9 * GeneralDims(modelname,rho, T, D_tr, D_rot)[1])) + "nm")
        return rho

    except StatisticsError or RuntimeWarning:
        print("No solution.")
        
def runner(model, T, D_tr, D_rot):
    grapher(Solver(model, T, D_tr, D_rot), model, T, D_tr, D_rot)
