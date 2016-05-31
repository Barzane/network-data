# -*- coding: utf-8 -*-

import cPickle

def filter_low_routes_by_carrier(year, quarter, threshold):
    
    print '\nremove carriers with low number of routes (threshold = ' + str(threshold) + '), save to \\temp'
    
    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'

    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()

    routesByCarrier = {}
    
    for key in data:
        
        carrier = key.split('_')[2]
        
        if carrier not in routesByCarrier:
            routesByCarrier[carrier] = 1
        else:
            routesByCarrier[carrier] += 1
    
    routesByCarrierFilter = []
    
    for item in routesByCarrier:
        
        if routesByCarrier[item] < threshold:
            routesByCarrierFilter.append(item)
    
    data2 = {}    
    output_filter = {}
    
    for key in data:
        
        carrier = key.split('_')[2]
        
        if carrier not in routesByCarrierFilter:
            
            data2[key] = data[key]
            
        else:
            
            if carrier not in output_filter:
                
                output_filter[carrier] = 1
                
            else:
                
                output_filter[carrier] += 1
                
    if output_filter != {}:
        
        for carrier in output_filter:
            
            print 'removed', carrier, '# routes', output_filter[carrier]
    
    data = data2
    
    del data2
    
    f = open(dst, 'wb')
    cPickle.dump(data, f)
    f.close()

    return None
