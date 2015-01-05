#Author : Pranav Jain

#!/usr/bin/python
# -*- coding : utf-8 -*-


import random


def appliance_switching():
    
    NUMBER_OF_RANDOMS = 5           # Number of random numbers for each appliance

    list_of_appliances = ['ac', 'tv', 'light' , 'fan']  # Finite List of appliances 

    dict_of_appliances = {}              # The dictionary to hold the random streams of the appliances

    for i in list_of_appliances:         
        dict_of_appliances[i] = [random.randint(0, 200) for j in range(NUMBER_OF_RANDOMS)]

    #print dict_of_appliances             # Debugging Statement

    #print dict_of_appliances['tv']       # Debugging Statement

    
    dict_of_switch = {}                   # The dicitonary to hold the switiching event information

    for x in dict_of_appliances:
        dict_of_switch[x] = mark_switch_event(dict_of_appliances[x])

    #print dict_of_appliances           # debugging statement
    #print dict_of_switch               # debugging statment


    bitwise_and(dict_of_switch)

        

def mark_switch_event(random_stream):
    """Function to detect switching . Takes as input the random data stream associated with each appliance"""
    temp = [] 
    for i in range(len(random_stream)-1):
        t_1 = random_stream[i]   
        t = random_stream[i-1]
        if abs(t - t_1)>40:
            temp.append(1)
        else:
            temp.append(0)
    return temp


def bitwise_and(dictionary):
    """Function to detect switching . Takes as input the dictionary of switiching """
    jlt = [] 
    for x in dictionary:
        zipped = list(zip(*dictionary.values()))

    #print zipped    # debugging statement

    for i in zipped:
        jlt.append(all(i))

    #print jlt  # debugging statement
        
    cnt = 0
    for iterator in jlt:
        if iterator == True:
            cnt = cnt + 1

    print cnt




appliance_switching()
