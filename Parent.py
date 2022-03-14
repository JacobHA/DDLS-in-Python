# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:04:00 2019

@author: Jacob
"""

# PLOTTER
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # need this still to plot
import matplotlib.pyplot as plt
from geometric_functions_for_DDLS import GeneralDims
import os

RESOLUTION = 256
pi=np.pi

def grapher(aspect_ratio, model, T, D_tr, D_rot):
    length,width = GeneralDims(model, aspect_ratio, T, D_tr, D_rot)
    width *= 1e9
    length *= 1e9 # convert them from nm
             
    fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
    ax = fig.add_subplot(111, projection='3d')

    if model == 'cylinder':
        
        def data_for_cylinder_along_z(center_x,center_y,radius,height_z): ## FROM SE
            z = np.linspace(-height_z/2, height_z/2, 50)
            theta = np.linspace(0, 2*pi, 50)
            theta_grid, z_grid=np.meshgrid(theta, z)
            x_grid = radius*np.cos(theta_grid) + center_x
            y_grid = radius*np.sin(theta_grid) + center_y
            return x_grid,y_grid,z_grid
                
        Xc,Yc,Zc = data_for_cylinder_along_z(0.,0.,width/2, length)
        
        phi = np.linspace(0,2*pi, RESOLUTION).reshape(RESOLUTION, 1) # the angle of the projection in the xy-plane
        theta = np.linspace(0, pi, RESOLUTION).reshape(-1, RESOLUTION) # the angle from the polar axis, ie the polar angle
       
        # top and bottom surfaces:
        ax.plot_surface(width/2*np.sin(theta)*np.cos(phi), width/2*np.sin(theta)*np.sin(phi), length/2+np.zeros(np.shape(phi)), color = 'b')
        ax.plot_surface(width/2*np.sin(theta)*np.cos(phi), width/2*np.sin(theta)*np.sin(phi), -length/2+np.zeros(np.shape(phi)), color = 'b')
        
        ax.plot_surface(Xc, Yc, Zc, color = 'b')
        axbound=max(width,length)
        
        for axis in 'xyz':
            getattr(ax, 'set_{}lim'.format(axis))((-axbound/2,axbound/2))
        
        #plt.show()
        aspect_ratio_str = str(aspect_ratio).replace('.','_') # so that we can save the filetype correctly
        
    if model == 'oblate' or model == 'prolate':
        
        phi = np.linspace(0,2*pi, RESOLUTION).reshape(RESOLUTION, 1) # the angle of the projection in the xy-plane
        theta = np.linspace(0, pi, RESOLUTION).reshape(-1, RESOLUTION) # the angle from the polar axis, ie the polar angle
        rx, ry, rz = 0.5*width, 0.5*width, 0.5*length # give radii 
        
        # Transformation formulae for a spherical coordinate system.
        x = rx*np.sin(theta)*np.cos(phi)
        y = ry*np.sin(theta)*np.sin(phi)
        z = rz*np.cos(theta)

        rbound=max(rx,ry,rz)
        
        ax.plot_surface(x, y, z, color='b')
        
        for axis in 'xyz':
            getattr(ax, 'set_{}lim'.format(axis))((-rbound,rbound))
            
        aspect_ratio_str = str(aspect_ratio).replace('.','_') # so that we can save the filetype correctly
    plt.savefig(f'.//{model}_plot_aspect_ratio_{aspect_ratio_str}')
    print(f'File saved at {os.getcwd()}\{model}_plot_aspect_ratio_{aspect_ratio_str}.png')
# Animation:
            
#    for angle in range(0, 180,2): 
#        ax.view_init(10, angle)#azim=0)
#        #ax.elev = 20 + angle
#        ax.azim = 60*np.sin(pi*angle/180+0.7)
#        ax.elev = 20*np.sin(5*pi*angle/180)
#    
#        plt.draw()
#        plt.show(block=False)
#        plt.pause(.07)
#        plt.gca()
        
    #for angle in range(100, 180): 
    #    ax.view_init(angle, azim=15)
    #    #ax.elev = 20 + angle
    #    ax.azim = 115 - angle
    #    plt.draw()
    #    plt.pause(.01)
    return
