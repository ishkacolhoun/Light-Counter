#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:31:45 2021

@author: ishka
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

# opens the ambient light training file 

with open(input('Name of training file:'),newline='') as csvfile:
    file_reader = csv.reader(csvfile)
    Am_lit_data_list = [row for row in file_reader]
am_lit_data_array = np.array(Am_lit_data_list[1:],dtype = 'float64')

# finds the max value of intensity from the ambient light

am_max =max(am_lit_data_array[:,1])

#opens the data file and assigns it to a list

with open(input('Name of test file:'),newline='') as csvfile:
    file_reader = csv.reader(csvfile)
    data_list = [row for row in file_reader]
    
#turns the list into an array

data_array = np.array(data_list[1:],dtype = 'float64')

plt.plot(data_array[1:,0],data_array[1:,1],'g') # plots intensity versus time

#gives a value of 1(on) or 0(off) to the data

for i in range(len(data_array)):
    if data_array[i,1] <= am_max:
        data_array[i,1] = 0
    if data_array[i,1] > am_max:
        data_array[i,1] = 1

#creates a list of on/off signals
list_on_off = [line for line in data_array[:,1]]


#makes sure the last signal is an off signal

if list_on_off[len(list_on_off)-1] == 1:
    list_on_off.append(0)



# creates the simp_list(removes duplicates if they are alongside each other)
simp_list = []

for i in range(len(list_on_off)-1):
    if list_on_off[i] != list_on_off[i+1]:
        simp_list.append(list_on_off[i])
        
#prints the count of how many times the light was on
print('The light was on',simp_list.count(1),'times.')



