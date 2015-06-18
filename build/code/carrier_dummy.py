# -*- coding: utf-8 -*-

import cPickle

def add_dummies(year, quarter):

    src = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    dst = '..\\temp\\data_' + str(year) + '_' + str(quarter) + '.bin'
    
    f = open(src, 'rb')
    data = cPickle.load(f)
    f.close()
    
    carrierList = []
    
    for key in data:
        
        carrier = key.split('_')[2]
        
        if carrier not in carrierList:
            carrierList.append(carrier)
    
    carrierList.sort()
    
    for key in data:
        
        carrier = key.split('_')[2]
        
        for item in carrierList:
            
            if carrier == item:
                data[key][item] = 1
            else:
                data[key][item] = 0
    
    f = open(dst, 'wb')
    cPickle.dump(data, f)
    f.close()
    
    return None
