# -*- coding: utf-8 -*-

import cPickle, numpy, math
import matplotlib.pyplot as plt

def analysis():
    
    src = '..\\output\\data_full_with_network.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    analysis = dict()
    x_axis = range(1, 61)
    analysis['density_WN'] = [x_axis, [numpy.nan] * len(x_axis)]
    analysis['edges_WN'] = [x_axis, [numpy.nan] * len(x_axis)]
    analysis['nodes_WN'] = [x_axis, [numpy.nan] * len(x_axis)]
    analysis['diameter_WN'] = [x_axis, [numpy.nan] * len(x_axis)]
    
    for key in data:
        
        data_s = key.split('_')
        
        origin = data_s[0]
        destination = data_s[1]
        route = origin + '_' + destination
        carrier = data_s[2]
        year = data_s[3]
        quarter = data_s[4]
        
        counter = data[key]['time'] - 24
        
        if carrier == 'WN':
            if math.isnan(analysis['density_WN'][1][counter]):
                analysis['density_WN'][1][counter] = data[key]['density']
                analysis['edges_WN'][1][counter] = data[key]['edges']
                analysis['nodes_WN'][1][counter] = data[key]['nodes']
                analysis['diameter_WN'][1][counter] = data[key]['diameter']
    
    plt.figure()
    plt.plot(analysis['density_WN'][0], analysis['density_WN'][1])
    plt.xlabel('time', fontsize=16)
    plt.ylabel('density', fontsize=16)
    plt.show()
    
    plt.figure()
    plt.plot(analysis['edges_WN'][0], analysis['edges_WN'][1])
    plt.xlabel('time', fontsize=16)
    plt.ylabel('edges', fontsize=16)
    plt.show()
    
    plt.figure()
    plt.plot(analysis['nodes_WN'][0], analysis['nodes_WN'][1])
    plt.xlabel('time', fontsize=16)
    plt.ylabel('nodes', fontsize=16)
    plt.show() 
    
    plt.figure()
    plt.plot(analysis['diameter_WN'][0], analysis['diameter_WN'][1])
    plt.xlabel('time', fontsize=16)
    plt.ylabel('diameter', fontsize=16)
    plt.show()
    
    return None
