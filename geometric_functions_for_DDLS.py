# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:35:09 2019

@author: Jacob
"""
import numpy as np


# Boltzmann Constant:
kB = 1.3806488E-23
pi = np.pi

def viscosity(T):
    A_visc = 2.414e-5
    B_visc = 247.8
    C_visc = 140 
    # ^numerical constants for viscosity calculation defined in Mathcad file ...
    return A_visc * 10**(B_visc/(T-C_visc))

def coeffs(T, D_tr, D_rot):
    base = kB*T/(3*pi*viscosity(T))
    tr_coe = base/D_tr
    rot_coe = 9*base/D_rot
    return tr_coe, rot_coe # Just so we don't have to calculate multiple times


# https://doi.org/10.1021/jp211533d
# See equations 8, 11

# PROLATE ELLIPSOID
def F_pro(x):
    return x*np.log(x+np.sqrt(x**2 - 1))/np.sqrt(x**2 - 1)

def G_pro(x):
    return 0.5*x**2 * (((2*x**2 - 1) / x**2) * (x*np.log(x+np.sqrt(x**2 - 1))/np.sqrt(x**2 - 1)) - 1) / (x**2 - 1)



# OBLATE ELLIPSOID
def F_obl(x):
    return (np.sqrt(1-x**2)/x)*np.arctan(np.sqrt(1-x**2)/x)
def G_obl(x):
    return ((2*x-1)*np.sqrt(1-x**2)*np.arctan(np.sqrt(1-x**2)/x) - 1)/(x**2 - 1)


# https://doi.org/10.1021/jp211533d
# See equations 7a and 10a

# CYLINDER
def F_cyl(x):
    return np.log(x) + (0.312 + 0.565*x**(-1) - 0.1*x**(-2))
def G_cyl(x):
    return np.log(x) +  (-0.662 + 0.917*x**(-1) - 0.050*x**(-2))

# TODO: Concatenate the equations with 7b, 10b: for aspect ratios 0.1-20


# The general optimization function:
def GeneralOpt(F,G,x, T, D_tr, D_rot):
    tr, rot = coeffs(T, D_tr, D_rot)
    return tr*F(x) - (rot*G(x))**(1/3)

# The model chooser:
def ModelChoice(model_name):

    if model_name == 'oblate':
        F, G = F_obl, G_obl

    if model_name == 'prolate':
        F, G = F_pro, G_pro

    if model_name == 'cylinder':
        F, G = F_cyl, G_cyl

    if model_name == '':
        print("Please enter a name for the model to use. I.e.: \'prolate\', \'oblate\', or \'cylindrical\'.")
        exit()
    
    return F,G

# The optimization function with applied model:
def OptimizingFunction(model_name, T, D_tr, D_rot):
    F,G = ModelChoice(model_name)
    return lambda x: GeneralOpt(F, G, x, T, D_tr, D_rot)

# The general dimensions with applied model:
def GeneralDims(model_name, rho, T, D_tr, D_rot):
    F,G = ModelChoice(model_name)
    axis1 = 3*np.sqrt(D_tr/D_rot * G(rho) / F(rho))
    return axis1, axis1/rho
