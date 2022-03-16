# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:04:00 2019

@author: Jacob
"""

# PLOTTER
import numpy as np
from grapher_tools import sphere_plotter, cylinder_plotter

RESOLUTION = 256
pi=np.pi



def grapher(length, width, model, T, D_tr, D_rot):
    rho = length/width
    width *= 1e9
    length *= 1e9 # convert them from nm

    if model == 'cylinder':
        
        cylinder_plotter(f'{model}_{rho}', width/2, length)

    if model == 'oblate':

        rz=min(width,length)/2
        rx=max(width,length)/2
        ry=max(width,length)/2
        sphere_plotter(f'{model}_{rho}', rx, ry, rz)

    if model == 'prolate':
        
        rz=max(width, length)/2
        rx=min(width, length)/2
        ry=min(width, length)/2
        sphere_plotter(f'{model}_{rho}', rx, ry, rz)
