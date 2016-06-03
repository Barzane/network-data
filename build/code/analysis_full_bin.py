# -*- coding: utf-8 -*-

import cPickle, numpy, math

import matplotlib.pyplot as plt

def analysis():
    
    print '\nanalyzing full-sample data .bin'
    
    src = '..\\output\\data_full_with_network.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    analysis = dict()
    x_axis = range(1, 61)
    
#    carrier_choice = 'WN'
#    carrier_name = 'Southwest Airlines'
    
    carrier_choice = 'F9'
    carrier_name = 'Frontier Airlines'
    
    airport_choice = 'DEN'
    airport_name = 'Denver International'
    
    name_list = [name + '_' + carrier_choice for name in ['density', 'edges', 'nodes', 'diameter']]
    centrality_list = [name + '_' + carrier_choice for name in ['origindegree', 'origincloseness', 'originbetweenness', 'origineigenvector']]
    
    for name in name_list:
        
        analysis[name] = [x_axis, [numpy.nan] * len(x_axis)]
        
    for name in centrality_list:
        
        analysis[name] = [x_axis, [numpy.nan] * len(x_axis)]
    
    x_labels = [str(x) for x in range(1999, 2014) for y in range(1, 5)]
    
    for i in range(len(x_labels)):
        if i % 8 != 0:
            x_labels[i] = ''    
        
    for key in data:
        
        data_s = key.split('_')
        
        origin = data_s[0]
        destination = data_s[1]
        route = origin + '_' + destination
        carrier = data_s[2]
        year = data_s[3]
        quarter = data_s[4]
        
        counter = data[key]['time'] - 24
        
        if carrier == carrier_choice:
            if math.isnan(analysis[name_list[0]][1][counter]):
                
                for name in name_list:
                
                    analysis[name][1][counter] = data[key][name.split('_')[0]]    
    
        if carrier == carrier_choice:
            if origin == airport_choice:
                if math.isnan(analysis[centrality_list[0]][1][counter]):
                    
                    for name in centrality_list:
                
                        analysis[name][1][counter] = data[key][name.split('_')[0]]
    
    for name in name_list:
        
        fig = plt.figure()
        plt.plot(analysis[name][0], analysis[name][1])
        plt.title(carrier_name)
        plt.xlabel('time', fontsize=16)
        plt.ylabel(name.split('_')[0], fontsize=16)
        plt.xticks(x_axis, x_labels)
        fig.savefig('..\\output\\' + name + '.png')

    for name in centrality_list:
        
        fig = plt.figure()
        plt.plot(analysis[name][0], analysis[name][1])
        plt.title(carrier_name + ' (' + airport_name + ')')
        plt.xlabel('time', fontsize=16)
        plt.ylabel(name.split('_')[0], fontsize=16)
        plt.xticks(x_axis, x_labels)
        axes = plt.gca()
#        http://stackoverflow.com/questions/2821072/is-there-a-better-way-of-making-numpy-argmin-ignore-nan-values
        axes.set_ylim([0.95 * numpy.nanmin(analysis[name][1]), 1.05 * numpy.nanmax(analysis[name][1])])
        fig.savefig('..\\output\\' + name + '.png')
        
    return None
