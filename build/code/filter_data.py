# -*- coding: utf-8 -*-

import cPickle

def filter_low_routes_by_carrier(year, quarter, threshold):
    
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
    
    for key in data:
        
        carrier = key.split('_')[2]
        
        if carrier not in routesByCarrierFilter:
            
            data2[key] = data[key]
            
        else:
            
            print '\t'+'removed', carrier
    
    data = data2
    
    del data2
    
    f = open(dst, 'wb')
    cPickle.dump(data, f)
    f.close()

    return None
